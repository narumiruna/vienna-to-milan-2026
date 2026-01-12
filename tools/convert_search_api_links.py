#!/usr/bin/env python3
"""
自動轉換 Search API 連結為直接連結

此工具會：
1. 掃描所有 Search API 連結
2. 嘗試透過 HTTP 重定向取得直接的 place 連結
3. 對於成功的連結，可以選擇自動更新檔案
4. 對於失敗的連結，產生手動修復清單
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Optional
import json
from urllib.parse import unquote

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    print("⚠️  未安裝 requests 套件。某些功能將無法使用。")
    print("   安裝方式: pip install requests")


def find_search_api_links_in_file(filepath: Path) -> List[Dict]:
    """找出檔案中所有的 Search API 連結"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    results = []
    
    for i, line in enumerate(lines, 1):
        if 'google.com/maps/search/?api=1' in line:
            # 提取完整 URL
            url_match = re.search(r'(https://www\.google\.com/maps/search/\?api=1[^\s\)|\]]+)', line)
            if url_match:
                url = url_match.group(1)
                
                # 嘗試提取餐廳名稱
                name = None
                if '|' in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) > 1:
                        name = parts[1]
                else:
                    # 從標題行提取
                    name_match = re.search(r'####?\s*([^\n-]+)', line)
                    if name_match:
                        name = name_match.group(1).strip()
                
                # 提取查詢字串
                query_match = re.search(r'query=([^&\s\)|\]]+)', url)
                query = query_match.group(1) if query_match else ''
                
                results.append({
                    'line_num': i,
                    'line_content': line,
                    'name': name or 'Unknown',
                    'old_url': url,
                    'query': query,
                    'search_query': unquote(query).replace('+', ' ')
                })
    
    return results


def get_direct_link_from_search_api(search_url: str, timeout: int = 10) -> Optional[Dict]:
    """
    嘗試透過 Search API URL 取得直接的 place 連結
    
    返回:
    - success: True/False
    - direct_url: 直接連結（如果成功）
    - error: 錯誤訊息（如果失敗）
    """
    if not HAS_REQUESTS:
        return {
            'success': False,
            'error': 'requests module not available'
        }
    
    try:
        # 發送請求並跟隨重定向
        response = requests.get(search_url, allow_redirects=True, timeout=timeout)
        final_url = response.url
        
        # 檢查是否成功重定向到 place 連結
        if 'google.com/maps/place/' in final_url:
            return {
                'success': True,
                'direct_url': final_url,
                'redirects': len(response.history),
                'link_type': 'place'
            }
        elif 'maps.app.goo.gl' in final_url or 'goo.gl/maps' in final_url:
            return {
                'success': True,
                'direct_url': final_url,
                'redirects': len(response.history),
                'link_type': 'short_link'
            }
        else:
            return {
                'success': False,
                'error': f'Redirected to unexpected URL: {final_url}',
                'final_url': final_url
            }
    
    except requests.exceptions.Timeout:
        return {
            'success': False,
            'error': 'Request timeout'
        }
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': str(e)
        }


def scan_and_convert(base_path: Path = Path('gourmet'), dry_run: bool = True):
    """
    掃描並嘗試轉換所有 Search API 連結
    
    Args:
        base_path: 要掃描的基礎目錄
        dry_run: 如果為 True，只顯示結果不實際修改檔案
    """
    cities = sorted([d for d in base_path.iterdir() if d.is_dir()])
    
    results = {
        'success': [],
        'failed': [],
        'total': 0
    }
    
    for city_dir in cities:
        print(f"\n{'='*80}")
        print(f"📍 處理: {city_dir.name}")
        print(f"{'='*80}")
        
        for filename in ['candidates.md', 'top-places.md']:
            filepath = city_dir / filename
            if not filepath.exists():
                continue
            
            links = find_search_api_links_in_file(filepath)
            if not links:
                continue
            
            print(f"\n  檔案: {filename} ({len(links)} 個連結)")
            
            for item in links:
                results['total'] += 1
                print(f"\n  {item['name']}")
                print(f"    原始: {item['old_url']}")
                
                # 嘗試取得直接連結
                convert_result = get_direct_link_from_search_api(item['old_url'])
                
                if convert_result.get('success'):
                    direct_url = convert_result['direct_url']
                    print(f"    ✅ 成功: {direct_url}")
                    print(f"    重定向: {convert_result['redirects']} 次")
                    
                    results['success'].append({
                        'file': str(filepath),
                        'line': item['line_num'],
                        'name': item['name'],
                        'old_url': item['old_url'],
                        'new_url': direct_url,
                        'link_type': convert_result.get('link_type')
                    })
                    
                    if not dry_run:
                        # 實際更新檔案
                        replace_url_in_file(filepath, item['old_url'], direct_url)
                        print(f"    💾 已更新檔案")
                else:
                    error_msg = convert_result.get('error', 'Unknown error')
                    print(f"    ❌ 失敗: {error_msg}")
                    
                    results['failed'].append({
                        'file': str(filepath),
                        'line': item['line_num'],
                        'name': item['name'],
                        'old_url': item['old_url'],
                        'search_query': item['search_query'],
                        'error': error_msg
                    })
    
    return results


def replace_url_in_file(filepath: Path, old_url: str, new_url: str):
    """在檔案中替換 URL"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替換 URL
    new_content = content.replace(old_url, new_url)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)


def print_summary(results: Dict):
    """印出轉換結果摘要"""
    print(f"\n{'='*80}")
    print("轉換結果摘要")
    print(f"{'='*80}")
    print(f"\n總計: {results['total']} 個連結")
    print(f"✅ 成功轉換: {len(results['success'])} 個")
    print(f"❌ 需要手動處理: {len(results['failed'])} 個")
    
    if results['success']:
        print(f"\n成功轉換的連結類型分布:")
        place_count = sum(1 for r in results['success'] if r.get('link_type') == 'place')
        short_count = sum(1 for r in results['success'] if r.get('link_type') == 'short_link')
        print(f"  - Place 連結: {place_count}")
        print(f"  - 短連結: {short_count}")


def save_manual_fix_list(failed_items: List[Dict], output_file: str = 'manual_fix_list.md'):
    """儲存需要手動修復的清單"""
    if not failed_items:
        return
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 需要手動修復的 Google Maps 連結\n\n")
        f.write(f"總計: {len(failed_items)} 個連結需要手動處理\n\n")
        f.write("## 修復步驟\n\n")
        f.write("1. 在 Google Maps 搜尋餐廳名稱\n")
        f.write("2. 選擇正確的商家\n")
        f.write("3. 點擊 'Share' 按鈕\n")
        f.write("4. 複製短連結並更新對應檔案\n\n")
        f.write("---\n\n")
        
        for i, item in enumerate(failed_items, 1):
            f.write(f"## {i}. {item['name']}\n\n")
            f.write(f"- **檔案**: `{item['file']}`\n")
            f.write(f"- **行號**: {item['line']}\n")
            f.write(f"- **搜尋**: {item['search_query']}\n")
            f.write(f"- **原始連結**: {item['old_url']}\n")
            f.write(f"- **錯誤**: {item['error']}\n")
            f.write(f"- **Google Maps**: https://www.google.com/maps/search/{item['search_query'].replace(' ', '+')}\n")
            f.write("\n")
            f.write("[ ] 已完成修復\n\n")
            f.write("---\n\n")
    
    print(f"\n📄 手動修復清單已儲存至: {output_file}")


def main():
    if len(sys.argv) < 2:
        print("使用方式:")
        print("  python convert_search_api_links.py scan           # 掃描並嘗試轉換（試運行）")
        print("  python convert_search_api_links.py convert        # 實際轉換並更新檔案")
        print("  python convert_search_api_links.py check          # 只檢查哪些可以轉換")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if not HAS_REQUESTS and command in ['scan', 'convert', 'check']:
        print("❌ 此功能需要 requests 套件")
        print("   安裝方式: pip install requests")
        sys.exit(1)
    
    if command == 'scan':
        print("🔍 掃描並測試轉換 Search API 連結...")
        print("⚠️  試運行模式 - 不會修改任何檔案")
        results = scan_and_convert(dry_run=True)
        print_summary(results)
        
        if results['failed']:
            save_manual_fix_list(results['failed'])
    
    elif command == 'convert':
        print("🔄 轉換 Search API 連結...")
        response = input("⚠️  這將修改檔案。確定要繼續嗎？(yes/no): ")
        if response.lower() != 'yes':
            print("已取消")
            sys.exit(0)
        
        results = scan_and_convert(dry_run=False)
        print_summary(results)
        
        if results['failed']:
            save_manual_fix_list(results['failed'])
    
    elif command == 'check':
        print("✓ 檢查哪些連結可以自動轉換...")
        # 只測試不修改
        results = scan_and_convert(dry_run=True)
        print_summary(results)
    
    else:
        print(f"❌ 未知命令: {command}")
        sys.exit(1)


if __name__ == '__main__':
    main()
