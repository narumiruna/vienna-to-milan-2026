#!/usr/bin/env python3
"""
Google Maps 連結修復工具

此腳本協助修復專案中的 Google Maps 連結：
1. 掃描找出所有使用 Search API 連結的餐廳
2. 提供修復指引  
3. 可選：批次替換連結（需要提供新連結清單）
"""

import re
import sys
from pathlib import Path
from typing import List, Dict
import json


def find_search_api_links(filepath: Path) -> List[Dict]:
    """找出檔案中所有的 Search API 連結"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    results = []
    
    for i, line in enumerate(lines, 1):
        if 'google.com/maps/search/?api=1' in line:
            # 嘗試從 markdown table 中提取餐廳名稱
            if '|' in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 6:
                    name = parts[1]
                    url = parts[5]
                    
                    # 提取查詢字串
                    query_match = re.search(r'query=([^&\s|]+)', url)
                    query = query_match.group(1) if query_match else ''
                    
                    results.append({
                        'line_num': i,
                        'name': name,
                        'old_url': url,
                        'query': query,
                        'search_query': query.replace('+', ' ').replace('%20', ' ')
                    })
    
    return results


def scan_all_cities(base_path: Path = Path('gourmet')):
    """掃描所有城市的連結問題"""
    cities = sorted([d for d in base_path.iterdir() if d.is_dir()])
    
    all_results = {}
    total_count = 0
    
    for city_dir in cities:
        city_results = {}
        
        # 檢查 candidates.md
        candidates_file = city_dir / 'candidates.md'
        if candidates_file.exists():
            results = find_search_api_links(candidates_file)
            if results:
                city_results['candidates.md'] = results
                total_count += len(results)
        
        # 檢查 top-places.md
        top_places_file = city_dir / 'top-places.md'
        if top_places_file.exists():
            results = find_search_api_links(top_places_file)
            if results:
                city_results['top-places.md'] = results
                total_count += len(results)
        
        if city_results:
            all_results[city_dir] = city_results
    
    return all_results, total_count


def main():
    if len(sys.argv) < 2:
        print("使用方式:")
        print("  python fix_google_maps_links.py scan    # 掃描所有問題連結")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'scan':
        print("🔍 掃描 Google Maps 連結問題...")
        all_results, total = scan_all_cities()
        
        print(f"\n{'='*80}")
        print(f"掃描結果總覽")
        print(f"{'='*80}\n")
        
        for city_dir, files in all_results.items():
            city_name = city_dir.name
            count = sum(len(results) for results in files.values())
            print(f"📍 {city_name}: {count} 個連結需要修復")
            for filename, results in files.items():
                print(f"   - {filename}: {len(results)} 個")
        
        print(f"\n總計: {total} 個 Search API 連結需要修復")


if __name__ == '__main__':
    main()
