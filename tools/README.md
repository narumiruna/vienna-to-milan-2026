# 工具腳本 (Tools)

本目錄包含專案維護和管理的輔助工具腳本。

## convert_search_api_links.py ⭐ 推薦

**用途**: 自動轉換 Search API 連結為直接連結

### 功能

- 自動掃描所有 Search API 連結
- 透過 HTTP 重定向取得官方直接連結
- 批次更新檔案
- 產生手動修復清單（針對無法自動轉換的連結）

### 使用方式

```bash
# 安裝依賴
pip install requests

# 掃描並測試轉換（試運行，不修改檔案）
python3 tools/convert_search_api_links.py scan

# 實際執行轉換（會修改檔案）
python3 tools/convert_search_api_links.py convert

# 僅檢查哪些可以轉換
python3 tools/convert_search_api_links.py check
```

### 工作原理

1. 掃描所有 `candidates.md` 和 `top-places.md` 檔案
2. 找出所有 Search API 連結 (`google.com/maps/search/?api=1`)
3. 發送 HTTP 請求，跟隨重定向
4. 取得 Google Maps 返回的直接連結（place 或 short link）
5. 更新檔案或記錄失敗項目

### 輸出

- **成功**: 自動更新檔案中的連結
- **失敗**: 產生 `manual_fix_list.md` 供手動處理

### 預期效果

- 成功率: 70-90%
- 時間節省: 從 2-3 小時降至 20-40 分鐘

---

## fix_google_maps_links.py

**用途**: 掃描和檢測 Google Maps 連結問題

### 使用方式

```bash
# 掃描所有問題連結
python3 tools/fix_google_maps_links.py scan
```

### 輸出範例

```
🔍 掃描 Google Maps 連結問題...

================================================================================
掃描結果總覽
================================================================================

📍 2026-02-11-vienna: 11 個連結需要修復
   - candidates.md: 11 個
📍 2026-02-13-rome: 27 個連結需要修復
   - candidates.md: 27 個

總計: 74 個 Search API 連結需要修復
```

---

## 背景資訊

根據 AGENTS.md 的規範，Google Maps 連結必須使用直接連結（direct links），而非搜尋 API 連結。

**✅ 正確格式**:
- `https://maps.app.goo.gl/...` (從 Google Maps Share 按鈕獲得)
- `https://www.google.com/maps/place/...` (place 頁面連結)

**❌ 不正確格式**:
- `https://www.google.com/maps/search/?api=1&query=...` (search API 連結)

### 修復流程

**推薦方式（自動 + 手動）**:
1. 執行 `convert_search_api_links.py scan` 自動轉換大部分連結
2. 對於失敗的連結，查看 `manual_fix_list.md`
3. 手動到 Google Maps 搜尋餐廳
4. 點擊 "Share" 按鈕獲取正確的短連結
5. 更新對應的 markdown 檔案

詳細資訊請參考: `docs/GOOGLE_MAPS_LINK_ISSUE.md`
