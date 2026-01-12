# Google Maps 連結修復指南

本指南說明如何使用自動化工具修復專案中的 Google Maps 連結問題。

## 問題背景

專案中使用了大量的 Search API 連結 (`google.com/maps/search/?api=1`)，這類連結：
- ❌ 不符合專案規範
- ❌ 不穩定（搜尋結果可能變化）
- ❌ 可能指向錯誤的商家

正確的做法是使用**直接連結**（從 Google Maps 的 Share 按鈕取得）。

## 快速開始

### 方法 1: 自動轉換 (推薦) ⭐

適用於有網路存取權限的環境。

#### Step 1: 安裝依賴

```bash
pip install requests
```

#### Step 2: 掃描並測試

```bash
cd /path/to/vienna-to-milan-2026
python3 tools/convert_search_api_links.py scan
```

這會顯示：
- ✅ 哪些連結可以自動轉換
- ❌ 哪些連結需要手動處理

#### Step 3: 執行轉換

確認結果後，執行實際轉換：

```bash
python3 tools/convert_search_api_links.py convert
```

系統會詢問確認，輸入 `yes` 繼續。

#### Step 4: 處理手動修復清單

工具會產生 `manual_fix_list.md`，列出無法自動轉換的連結。

對每個連結：
1. 打開 Google Maps
2. 搜尋餐廳名稱（清單中有提供）
3. 選擇正確的商家
4. 點擊 "Share" 按鈕
5. 複製短連結 (`maps.app.goo.gl/...`)
6. 更新對應檔案

#### Step 5: 驗證結果

```bash
python3 tools/fix_google_maps_links.py scan
```

應該顯示 `總計: 0 個 Search API 連結需要修復`。

### 方法 2: 純手動修復

適用於無網路存取或自動工具無法使用的情況。

#### Step 1: 掃描問題連結

```bash
python3 tools/fix_google_maps_links.py scan
```

#### Step 2: 逐一修復

對每個連結：
1. 在 Google Maps 搜尋餐廳
2. 選擇正確的商家
3. 點擊 "Share" 按鈕
4. 複製短連結
5. 編輯對應的 markdown 檔案，替換舊連結

優先順序：
1. Top Picks (status: top) 
2. Shortlisted
3. Researching / Inbox

## 工作原理

### 自動轉換工具的運作方式

```
Search API 連結
  ↓
HTTP GET 請求
  ↓
Google Maps 重定向
  ↓
直接連結 (place 或 short link)
  ↓
更新檔案
```

範例：

```
輸入:  https://www.google.com/maps/search/?api=1&query=Pompi+Tiramisu+Rome
       ↓ (HTTP 重定向)
輸出:  https://maps.app.goo.gl/abc123xyz
```

## 連結格式規範

### ✅ 正確格式

```
https://maps.app.goo.gl/X7yZh5KNJqF4vL6Z9         (Share 短連結)
https://www.google.com/maps/place/Restaurant+Name (Place 連結)
https://goo.gl/maps/abc123                         (舊版短連結)
```

### ❌ 不正確格式

```
https://www.google.com/maps/search/?api=1&query=Restaurant+Name
```

## 常見問題

### Q: 自動轉換的成功率有多高？

A: 預期 70-90%。大部分餐廳的 Search API 連結都能正確重定向到 place 連結。

### Q: 為什麼有些連結無法自動轉換？

A: 可能原因：
- 餐廳名稱拼寫錯誤
- 餐廳已關閉或搬遷
- Google Maps 搜尋結果有多個選項
- 網路連線問題

### Q: 自動轉換會不會改壞檔案？

A: 不會。工具會：
1. 只替換完全匹配的 URL
2. 先以 `scan` 模式測試
3. `convert` 模式會要求確認
4. 所有變更都會進入 git，可以隨時回復

### Q: 如何驗證轉換結果是否正確？

A: 
1. 查看 git diff 確認變更
2. 抽查幾個連結確認指向正確的商家
3. 使用瀏覽器開啟新連結測試

## 時間估算

- **自動轉換**: 5-10 分鐘
- **手動補充**: 15-30 分鐘（約 10-30 個連結）
- **驗證**: 5 分鐘

**總計: 25-45 分鐘** (vs 純手動 2.5-3.5 小時)

## 相關文件

- `docs/GOOGLE_MAPS_LINK_ISSUE.md` - 完整問題分析
- `tools/README.md` - 工具說明
- `AGENTS.md` - 專案規範（包含 Google Maps 連結要求）
