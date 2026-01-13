# Google Maps 最低分評價查詢研究

**研究日期**: 2026-01-13  
**研究目的**: 調查是否能夠透過 Google Maps API 查詢特定店家的最低分評價（1星、2星等負面評價）

---

## 執行摘要 (Executive Summary)

**可行性**: ✅ 可行，但有重要限制

**關鍵發現**:
1. **Google 官方 API**: 功能受限，無法直接篩選評分，僅提供少量樣本評價（最多5則）
2. **第三方 API**: 提供完整評價存取與篩選功能（包含 `sort_by=ratingLow` 參數）
3. **法律風險**: 直接抓取 Google Maps 違反服務條款，應謹慎使用

**建議方案**: 
- 若為研究/內部分析用途，可使用第三方 API（SerpApi, Outscraper, Apify）
- 若為商業用途，需評估法律風險
- 若為自家店面，可使用 Google Business Profile API 取得完整評價

---

## 1. Google 官方 API 能力分析

### 1.1 Google Places API / JavaScript API

**評價取得方式**:
```javascript
// 使用 Places API fetchFields 方法
await place.fetchFields({ fields: ['reviews'] });

// 篩選最低評分（需自行實作）
const lowRatings = place.reviews.filter(r => r.rating === 1 || r.rating === 2);
```

**主要限制**:
- ❌ **無直接篩選參數**: API 不提供 `filter_by_rating` 參數
- ❌ **評價數量受限**: 每個地點最多僅回傳 **5 則評價**
- ❌ **樣本偏差**: 回傳的評價是 Google 演算法篩選過的「代表性樣本」，非完整資料
- ⚠️ **不適合大規模分析**: 無法取得所有低分評價進行系統性研究

**適用情境**:
- 僅需展示少數評價於網站/應用程式
- 不需要完整的負面評價分析

**參考文件**:
- [Google Place Reviews 官方文件](https://developers.google.com/maps/documentation/javascript/place-reviews)
- [使用 Google Maps API 取得評價教學](https://elfsight.com/blog/working-with-google-maps-reviews-api/)

---

### 1.2 Google Business Profile API（店家專用）

**適用對象**: 僅限 **店家擁有者/管理員** 存取自家店面的評價

**能力**:
- ✅ 可存取 **所有評價**（無數量限制）
- ✅ 可程式化篩選與排序
- ✅ 可回覆評價、管理店面資訊

**限制**:
- ❌ 僅限自家店面，無法查詢競爭對手或其他店家

**適用情境**:
- 店家想分析自己的負面評價並改善服務
- 客服團隊需要統計與回覆低分評價

**參考文件**:
- [Google Business Profile API 文件](https://developers.google.com/my-business/content/review-data)
- [Google Reviews API 比較文章](https://www.lobstr.io/blog/google-reviews-api)

---

## 2. 第三方 API 解決方案

### 2.1 主要服務商比較

| 服務商 | 評分篩選 | 價格 | 評價數量 | API 品質 |
|--------|----------|------|----------|----------|
| **SerpApi** | ✅ `sort_by=ratingLow` | 中等 | 完整 | 優秀 |
| **Outscraper** | ✅ 支援篩選 | 中等 | 完整 | 優秀 |
| **Apify** | ✅ 支援篩選 | 低-中 | 完整 | 良好 |
| **SearchApi** | ✅ `sort_by=ratingLow` | 中等 | 完整 | 優秀 |
| **Serpdog** | ✅ `sort_by=ratingLow` | 中等 | 完整 | 良好 |
| **Shifter** | ✅ `sort_by=ratingLow` | 中等 | 完整 | 良好 |

---

### 2.2 SerpApi 使用範例（推薦）

**為何選擇 SerpApi**:
- 完整的 API 文件與社群支援
- 提供 `sort_by=ratingLow` 參數直接排序
- 穩定的服務品質與合理價格

#### API 請求範例

**HTTP 請求**:
```
GET https://serpapi.com/search
?engine=google_maps_reviews
&place_id=YOUR_PLACE_ID
&sort_by=ratingLow
&api_key=YOUR_API_KEY
```

**Node.js 程式碼範例**:
```javascript
const axios = require('axios');

async function getLowestRatingReviews(placeId) {
  try {
    const response = await axios.get('https://serpapi.com/search', {
      params: {
        engine: 'google_maps_reviews',
        place_id: placeId,
        sort_by: 'ratingLow',  // 關鍵參數：依評分低到高排序
        api_key: process.env.SERPAPI_KEY
      }
    });
    
    // 篩選 1 星與 2 星評價
    const lowReviews = response.data.reviews.filter(
      review => review.rating === 1 || review.rating === 2
    );
    
    console.log(`找到 ${lowReviews.length} 則低分評價`);
    return lowReviews;
    
  } catch (error) {
    console.error('API 請求失敗:', error.message);
  }
}

// 使用範例
getLowestRatingReviews('ChIJ...');  // 替換為實際的 Google Maps Place ID
```

**Python 程式碼範例**:
```python
import requests
import os

def get_lowest_rating_reviews(place_id):
    """取得指定地點的最低分評價"""
    
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_maps_reviews",
        "place_id": place_id,
        "sort_by": "ratingLow",  # 依評分低到高排序
        "api_key": os.getenv("SERPAPI_KEY")
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # 篩選 1 星與 2 星評價
        low_reviews = [
            review for review in data.get("reviews", [])
            if review.get("rating") in [1, 2]
        ]
        
        print(f"找到 {len(low_reviews)} 則低分評價")
        return low_reviews
        
    except requests.exceptions.RequestException as e:
        print(f"API 請求失敗: {e}")
        return []

# 使用範例
reviews = get_lowest_rating_reviews("ChIJ...")  # 替換為實際的 Place ID
```

#### 其他篩選參數

SerpApi 支援多種參數組合：

```python
params = {
    "engine": "google_maps_reviews",
    "place_id": "ChIJ...",
    "sort_by": "ratingLow",      # 排序方式: ratingLow, ratingHigh, newest, relevance
    "hl": "zh-TW",                # 語言
    "num": 100,                   # 每頁結果數量
    "start": 0,                   # 分頁起始位置
}
```

**參考文件**:
- [SerpApi Google Maps Reviews 文件](https://serpapi.com/google-maps-reviews-api)
- [Serpdog Google Maps Reviews 文件](https://docs.serpdog.io/google-maps-api/google-maps-reviews-api)

---

### 2.3 其他服務商簡介

#### Outscraper
- **特色**: 提供批次處理與資料匯出功能
- **適合**: 需要大量資料分析的研究專案
- **網址**: https://outscraper.com/

#### Apify
- **特色**: 開源爬蟲平台，可自訂爬蟲邏輯
- **適合**: 需要客製化資料擷取的專案
- **網址**: https://apify.com/gordian/google-maps-reviews-scraper

#### SearchApi
- **特色**: 提供多種搜尋引擎 API（Google, Bing, YouTube 等）
- **適合**: 需要整合多平台資料的專案
- **網址**: https://www.searchapi.io/docs/google-maps-reviews

---

## 3. 法律與倫理考量

### 3.1 服務條款限制

⚠️ **重要警告**: 直接抓取 Google Maps 網站資料（web scraping）**違反 Google 服務條款**

**Google 服務條款相關條文**:
> 禁止使用自動化工具（機器人、爬蟲等）存取 Google 服務，除非經過 Google 明確書面許可。

**違規風險**:
- IP 封鎖
- 法律訴訟（理論上可能，實務較少見）
- 資料來源不穩定（Google 可能變更網站結構）

### 3.2 合法使用情境

✅ **可接受的使用方式**:

1. **個人研究與學習**: 
   - 非商業用途的小規模資料分析
   - 學術研究（建議引用資料來源）

2. **內部商業分析**:
   - 競爭對手分析（不公開發布原始資料）
   - 市場研究與趨勢分析

3. **使用官方或授權 API**:
   - Google Places API（受限但合法）
   - 第三方 API 服務商（承擔風險但有保障）

❌ **應避免的使用方式**:

1. **大規模公開資料集**: 發布包含 Google Maps 評價的公開資料庫
2. **商業轉售**: 將抓取的評價資料轉售給第三方
3. **詐欺或惡意用途**: 使用資料進行詐騙、勒索、惡意攻擊

### 3.3 使用第三方 API 的法律定位

**第三方 API（SerpApi, Outscraper 等）的法律地位**:
- 這些服務本身進行資料抓取，並將風險轉嫁給自己
- 使用者透過 API 存取資料，相對降低直接違反 Google ToS 的風險
- **但仍存在灰色地帶**: Google 可能對這些服務商採取法律行動

**建議**:
- 僅用於研究、內部分析等合理用途
- 避免大量、頻繁的請求
- 不公開發布原始抓取資料
- 考慮使用官方 API 作為優先選擇

---

## 4. 實務應用建議

### 4.1 本專案使用建議

**目前專案需求**: 為維也納到米蘭旅程研究餐廳、咖啡館、甜點店的評價

**建議作法**:

#### 選項 A: 手動查看（當前作法）✅ 推薦
- **優點**: 
  - 無法律風險
  - 可同時閱讀評價內容，獲得質化洞察
  - 符合專案規模（每個城市 10-20 間店）
- **缺點**: 
  - 較為耗時
  - 無法系統化分析大量評價

**當前作法已足夠**: 專案文件顯示已透過 Google Maps、Tripadvisor、Reddit 等多來源進行評價研究，並記錄於 `notes.md` 中。

#### 選項 B: 使用第三方 API（進階需求）⚠️ 謹慎使用
- **適用情境**: 
  - 需要系統化分析大量候選店家（50+ 間）
  - 需要統計分析（如「負面評價佔比」、「常見抱怨主題」）
  - 需要自動化監控評分變化
- **實作建議**:
  1. 選擇 SerpApi 或 SearchApi（文件完整、穩定）
  2. 僅針對已列入 `candidates.md` 的店家查詢
  3. 設定合理的 API 請求頻率限制
  4. 將抓取的資料僅用於內部研究，不公開發布

#### 選項 C: 改良手動流程（平衡方案）✅ 推薦
- 在 Google Maps 網頁介面手動操作：
  1. 開啟店家的 Google Maps 頁面
  2. 點選「評論」標籤
  3. 使用網頁內建的「最低評分」篩選功能（若可用）
  4. 或手動瀏覽評論，記錄負面意見主題
- 將關鍵負面評價主題記錄於 `notes.md` 的「Recurring cons」欄位
- **優點**: 合法、免費、可獲得質化洞察

### 4.2 文件記錄建議

**更新研究流程文件** (`references/workflow-detailed.md`):

在「Step 2: Evidence Collection」新增段落：

```markdown
#### 查看低分評價的建議方式

**目的**: 了解店家的主要缺點與風險，作為評分參考

**手動方式**（推薦）:
1. 開啟 Google Maps 店家頁面
2. 點選「評論」，瀏覽 1-2 星評價
3. 記錄常見抱怨主題（如「服務慢」、「價格偏高」、「口味不如預期」）
4. 在 notes.md 的「Recurring cons」欄位記錄

**API 方式**（進階）:
- 若需系統化分析大量店家，可考慮使用第三方 API（SerpApi, Outscraper）
- 注意法律風險，僅用於內部研究
- 參考文件: `docs/google-maps-lowest-rating-research.md`
```

---

## 5. 結論與行動建議

### 關鍵結論

1. ✅ **技術上可行**: 透過第三方 API（SerpApi 等）可查詢並篩選 Google Maps 最低分評價
2. ⚠️ **法律灰色地帶**: 直接抓取違反 Google ToS，使用第三方 API 降低但未消除風險
3. ✅ **當前專案適用手動方式**: 專案規模小（每城市 10-20 間店），手動查看已足夠且無風險

### 具體行動建議

#### 立即行動（本專案）

1. **無需變更當前流程**: 繼續使用 Google Maps、Tripadvisor、Reddit 等多來源手動研究
2. **增強負面評價記錄**: 在 `notes.md` 的「Recurring cons」欄位，更詳細記錄 1-2 星評價的常見主題
3. **更新文件**: 在 `references/workflow-detailed.md` 新增「查看低分評價」的指引段落

#### 未來擴展（若專案規模擴大）

1. **評估 API 需求**: 若研究範圍擴大至 50+ 間店家，考慮使用 SerpApi
2. **建立評價分析工具**: 開發簡易腳本自動化抓取與分類負面評價主題
3. **合規審查**: 若為商業用途，諮詢法律顧問確認使用第三方 API 的風險

---

## 6. 參考資源

### 官方文件
- [Google Place Reviews API 文件](https://developers.google.com/maps/documentation/javascript/place-reviews)
- [Google Business Profile API](https://developers.google.com/my-business/content/review-data)

### 第三方 API 文件
- [SerpApi - Google Maps Reviews](https://serpapi.com/google-maps-reviews-api)
- [SearchApi - Google Maps Reviews](https://www.searchapi.io/docs/google-maps-reviews)
- [Apify - Google Maps Reviews Scraper](https://apify.com/gordian/google-maps-reviews-scraper)
- [Serpdog - Google Maps Reviews API](https://docs.serpdog.io/google-maps-api/google-maps-reviews-api)
- [Shifter - Google Maps Reviews API](https://developers.shifter.io/google-serp-api/search-apis/google-maps-reviews-api)

### 技術教學
- [Elfsight - Working with Google Maps Reviews API](https://elfsight.com/blog/working-with-google-maps-reviews-api/)
- [WiserReview - Google Maps Reviews API Guide](https://wiserreview.com/blog/google-maps-reviews-api/)
- [Lobstr - Google Reviews API Comparison](https://www.lobstr.io/blog/google-reviews-api)

### 法律與倫理
- [Google Maps Terms of Service](https://www.google.com/help/terms_maps/)
- Web Scraping 合法性討論（建議諮詢法律專家）

---

## 附錄：Place ID 取得方式

**Place ID** 是 Google Maps 每個地點的唯一識別碼，查詢評價時需要使用。

### 方法 1: 透過 Google Maps 網址
1. 開啟店家的 Google Maps 頁面
2. 網址格式如: `https://www.google.com/maps/place/...`
3. Place ID 通常不直接顯示於網址，需使用 Place ID Finder

### 方法 2: 使用 Place ID Finder
- **官方工具**: [Google Place ID Finder](https://developers.google.com/maps/documentation/places/web-service/place-id)
- **第三方工具**: 在 Google 搜尋 "Google Maps Place ID Finder"

### 方法 3: 透過 Places API 搜尋
```javascript
// 使用 Places API 搜尋店家
const service = new google.maps.places.PlacesService(map);
service.findPlaceFromQuery({
  query: '店家名稱',
  fields: ['place_id', 'name']
}, (results, status) => {
  if (status === google.maps.places.PlacesServiceStatus.OK) {
    console.log(results[0].place_id);
  }
});
```

---

**文件版本**: 1.0  
**最後更新**: 2026-01-13  
**維護者**: Copilot Coding Agent
