# Google Maps 連結問題分析與修復方案

## 問題描述

在隨機檢查文件中的 Google Maps 連結時，發現部分連結有問題：

1. **Osteria Alla Staffa** 的短連結 `https://maps.app.goo.gl/X7yZh5KNJqF4vL6Z9` 無法正常存取
2. 大量使用 **Search API 連結** (`https://www.google.com/maps/search/?api=1&query=...`)，這類連結不符合專案規範

## 問題規模

經過系統性掃描，發現：

### Search API 連結 (需要修復)
- **Vienna**: 11 個 (candidates.md)
- **Rome**: 27 (candidates.md) + 26 (top-places.md) = 53 個
- **Florence**: 28 (candidates.md) + 24 (top-places.md) = 52 個
- **Venice**: 8 (candidates.md) + 8 (top-places.md) = 16 個
- **Milan**: 8 (top-places.md) + 4 (notes.md) = 12 個

**總計: 144 個 Search API 連結需要修復**

### 按狀態分類 (candidates.md)
- **Top picks (top)**: 20 個 ⭐ 最高優先級
- **Shortlisted**: 43 個
- **Researching**: 4 個
- **Inbox**: 2 個

### 目前正確的連結
- **Place 連結** (`https://www.google.com/maps/place/...`): 18 個 ✅
- **短連結** (`https://maps.app.goo.gl/...`): 6 個 (需驗證)

## 根本原因

根據 AGENTS.md 的規範：

```markdown
**Google Maps Link Requirement**:
- **MUST use DIRECT Google Maps links**, not search API links
- ✅ Acceptable formats:
  - `https://maps.app.goo.gl/...` (short link from Google Maps app)
  - `https://www.google.com/maps/place/...` (place page URL)
  - `https://goo.gl/maps/...` (shortened place link)
- ❌ NOT acceptable:
  - `https://www.google.com/maps/search/?api=1&query=...` (search API link)
```

**使用者偏好方式**:
> 我平常的做法是在 google maps 那間店的頁面中點 share 可以取得完整且乾淨的連結

這是最可靠的方式，因為：
1. Share 功能提供的是 **direct place link**
2. 連結直接指向特定商家頁面，不會有搜尋結果的不確定性
3. 短連結格式 (`maps.app.goo.gl`) 簡潔且易於分享

## Search API 連結的問題

1. **不穩定**: 搜尋結果可能隨時間變化
2. **不精確**: 可能返回多個結果，不一定是目標餐廳
3. **地區差異**: 不同地區搜尋可能得到不同結果
4. **不符規範**: 違反專案中 AGENTS.md 的明確規定

## 修復方案

### 方案 A: 自動轉換 + 手動補充 (推薦) ⭐

**核心概念**: 
利用 Search API 連結的 HTTP 重定向功能，自動取得直接連結。對於無法自動轉換的，再手動處理。

**優點**:
- 大幅節省時間 - 自動處理大部分連結
- 準確性高 - 直接從 Google Maps 取得官方連結
- 可追蹤 - 記錄哪些成功、哪些失敗
- 效率優先 - 只需手動處理失敗的案例

**執行步驟**:

1. **自動轉換階段**:
   ```bash
   # 先測試哪些連結可以自動轉換
   python3 tools/convert_search_api_links.py scan
   
   # 確認後執行實際轉換
   python3 tools/convert_search_api_links.py convert
   ```

2. **手動補充階段**:
   - 工具會產生 `manual_fix_list.md` 列出需要手動處理的連結
   - 對這些連結：
     1. 在 Google Maps 搜尋餐廳
     2. 點擊 "Share" 按鈕
     3. 複製短連結 (maps.app.goo.gl 格式)
     4. 更新對應檔案

**預期效果**:
- 成功率: 70-90% 的連結可以自動轉換
- 時間節省: 從 2-3 小時降至 30-60 分鐘
- 準確性: 自動取得的連結來自 Google 官方重定向

### 方案 B: 純手動修復

**優點**:
- 每個連結都經過人工驗證
- 確保連結指向正確的商家
- 符合使用者偏好的工作流程

**缺點**:
- 需要時間 (估計 2-3 小時完成 144 個連結)

**執行步驟**:
1. 在 Google Maps 搜尋餐廳名稱 + 城市
2. 點選正確的商家
3. 點擊 "Share" 按鈕
4. 複製短連結 (maps.app.goo.gl 格式)
5. 更新對應的文件

**適用情境**:
- 自動工具無法使用時的備用方案
- 需要人工驗證商家資訊時

## 立即行動項目

### Step 1: 執行自動轉換工具

```bash
# 安裝依賴（如果尚未安裝）
pip install requests

# 測試哪些連結可以自動轉換
python3 tools/convert_search_api_links.py scan

# 檢視結果後，執行實際轉換
python3 tools/convert_search_api_links.py convert
```

### Step 2: 處理手動修復清單

工具會產生 `manual_fix_list.md`，列出無法自動轉換的連結。

優先級順序：
1. **Top Picks** (status: top) - 最高優先級
2. **Shortlisted** - 中等優先級  
3. **Researching / Inbox** - 低優先級

### Step 3: 驗證修復結果

```bash
# 檢查是否還有 Search API 連結
python3 tools/fix_google_maps_links.py scan

# 應該顯示 0 個連結需要修復
```

## 預防措施

建議在 CI/CD 中加入檢查：

```bash
# 檢查是否有 Search API 連結
if grep -r "google.com/maps/search/?api=1" gourmet/; then
  echo "❌ Found Search API links. Please use direct place links."
  exit 1
fi
```

## 工具腳本

本專案提供兩個輔助工具：

### 1. `tools/fix_google_maps_links.py` - 連結掃描器

**用途**: 快速掃描所有 Search API 連結

```bash
python3 tools/fix_google_maps_links.py scan
```

### 2. `tools/convert_search_api_links.py` - 自動轉換工具 ⭐

**用途**: 自動將 Search API 連結轉換為直接連結

```bash
# 測試模式 - 不修改檔案
python3 tools/convert_search_api_links.py scan

# 執行轉換 - 會修改檔案
python3 tools/convert_search_api_links.py convert

# 僅檢查哪些可轉換
python3 tools/convert_search_api_links.py check
```

**工作原理**:
1. 讀取每個 Search API 連結
2. 發送 HTTP 請求跟隨重定向
3. 取得 Google Maps 返回的直接連結
4. 更新檔案或產生手動修復清單

**輸出**:
- 成功轉換的連結會自動更新到檔案
- 失敗的連結會列在 `manual_fix_list.md`

## 時間估計

### 使用自動轉換工具 (方案 A)

- **自動轉換階段**: 5-10 分鐘
  - 執行掃描: 2-3 分鐘
  - 執行轉換: 3-5 分鐘
  - 預期成功率: 70-90%

- **手動補充階段**: 15-30 分鐘
  - 處理 10-30 個失敗的連結
  - 每個約 1-2 分鐘

**總計**: 約 20-40 分鐘完成所有修復 ✅

### 純手動方式 (方案 B)

- Phase 1 (Top Picks): 30-40 分鐘 (20 個 × 1-2 分鐘/個)
- Phase 2 (top-places.md): 60-90 分鐘
- Phase 3 (其餘): 60-90 分鐘

**總計**: 約 2.5-3.5 小時完成所有修復

### 結論

**採用方案 A 可節省 2+ 小時的時間** ⏱️
