# inbox.md 機制分析報告

**日期**: 2026-01-13  
**分析範圍**: 維也納至米蘭旅程美食研究工作流程  
**問題**: inbox.md 的機制是否需要存在？

---

## 執行摘要

**結論**: ✅ **建議保留 inbox.md 機制，但需要明確規範其生命週期和使用方式**

**核心理由**:
1. 初期研究需要「快速筆記空間」，不適合立即填入結構化表格
2. 符合 Progressive Disclosure 原則，作為最底層探索工具有其價值
3. 5個城市實際使用證明有效（總計985行，平均197行/城市）

**需要改進**:
1. 明確 inbox.md 的生命週期（探索 → 轉移 → 清理）
2. 在 AGENTS.md 中補充完成研究後的處理方式
3. 在完成標準中加入「inbox.md 已清理或標記為歷史記錄」的檢查

---

## 1. 當前角色分析

### 1.1 AGENTS.md 中的定義

**Required Repository Structure (Per City)**:
```
gourmet/YYYY-MM-DD-city/
├── overview.md
├── inbox.md          ← 必需文件
├── candidates.md
├── notes.md
├── top-places.md
└── excluded.md
```

**Progressive Disclosure 層級**:
```
overview.md       ← START HERE: Context, strategy, progress (5 min)
    ↓
top-places.md     ← ACTIONABLE: Final recommendations (10 min)
    ↓
candidates.md     ← SUMMARY: Quick scan table (5-10 min)
    ↓
notes.md          ← EVIDENCE: Detailed research (30+ min)
    ↓
inbox.md          ← RAW DATA: Working notes (exploratory)  👈 最底層
    ↓
excluded.md       ← REJECTED: What was excluded and why (5 min)
```

**描述**: "Working space (exploratory, always in flux)"

### 1.2 Workflow 中的用途

**Step 1: Discovery — Candidate Collection**
> Record raw findings in:
> - inbox.md (unstructured, fast capture with quick notes)
> - and/or candidates.md (structured table)

**建議結構**:
```
## Category (e.g., 傳統羅馬餐廳)
1. **Place Name**
   - 位置：area
   - 特色：key dishes/unique features
   - 注意：constraints
   - 來源：source type
```

---

## 2. 實際使用情況

### 2.1 各城市使用統計

| 城市 | 行數 | 研究狀態 | candidates.md 中 inbox 項目 | 使用模式 |
|------|------|----------|---------------------------|----------|
| Vienna | 107 | ✅ 已完成 | 0 | 已完成清單 + 新增 brunch 候選 |
| Rome | 244 | ✅ 已完成 | 2 | 詳細分類清單 + brunch，2項待處理 |
| Florence | 205 | ✅ 已完成 | 0 | 結構化候選清單 + brunch |
| Venice | 70 | ✅ 已完成 | 0 | 簡潔候選清單 + brunch |
| Milan | 359 | ✅ 已完成 | 3 | 最詳細分類，3項待處理 |
| **總計** | **985** | - | **5** | 平均 197 行/城市 |

### 2.2 使用模式觀察

#### 初期收集階段 ✅ 效果良好
- 快速記錄 web_search 結果
- 按類別分組（傳統餐廳、披薩、甜點、brunch等）
- 包含簡短筆記（位置、特色、注意事項、來源）
- 不需要立即填寫完整表格

#### 研究完成後 ⚠️ 狀態不一致
- **Vienna**: 保留歷史清單 + 新增研究項目
- **Rome**: 保留完整候選清單（244行），但有2個 tiramisu 店未轉移到 candidates.md
- **Florence**: 保留完整候選清單，所有項目已處理
- **Venice**: 簡潔清單，所有項目已處理
- **Milan**: 保留詳細清單（359行），但有3個糕點店未轉移到 candidates.md

**問題**: 沒有明確的「完成後處理」指引，各城市做法不一

---

## 3. 優缺點分析

### 3.1 優點 ✅

#### 1. 快速收集效率高
- **場景**: 初期 web_search 快速收集20-30個候選
- **好處**: 不需要立即格式化，降低心理門檻
- **證據**: 5個城市平均收集197行候選（相當於30-50個地點）

#### 2. 符合 Progressive Disclosure 原則
- 提供最底層的「探索性工作空間」
- 不強迫使用者在不確定時填寫結構化資料
- 支援「先發散、後收斂」的研究流程

#### 3. 彈性高
- 可自由組織分類（傳統餐廳、披薩、甜點、brunch等）
- 可隨時新增筆記而不破壞 candidates.md 的表格結構
- 可用作「暫存區」測試不同的組織方式

#### 4. 降低 candidates.md 的維護負擔
- candidates.md 保持簡潔（僅摘要表格）
- 避免在表格中插入大量未研究項目
- 清楚區分「已研究」(candidates.md) vs「待評估」(inbox.md)

### 3.2 缺點 ❌

#### 1. 重複工作
- 候選地點需要從 inbox.md **手動複製**到 candidates.md
- 同一地點可能在兩個文件中都有資訊（容易不同步）

#### 2. 資訊分散
- 查找特定候選時需要檢查兩個文件
- 不清楚某個候選是在 inbox.md 還是 candidates.md

#### 3. 維護負擔
- 研究完成後不清楚 inbox.md 該如何處理：
  - 保留？（變成歷史檔案）
  - 清空？（失去研究軌跡）
  - 合併到其他文件？（增加工作量）

#### 4. 不一致性
- 各城市使用方式不同（107-359行差異大）
- 沒有標準的「退出機制」（完成後該做什麼）

#### 5. 容易過時
- Research完成後，inbox.md 內容可能與 candidates.md 不一致
- 新加入的研究者可能不清楚 inbox.md 的狀態（是否最新？是否已處理？）

---

## 4. 替代方案評估

### 方案A：完全移除 inbox.md ❌ **不推薦**

**做法**:
- 移除 inbox.md 作為必需文件
- 所有候選直接在 candidates.md 中以 `status: inbox` 記錄

**優點**:
- ✅ 消除重複工作
- ✅ 單一資訊來源
- ✅ 簡化文件結構

**缺點**:
- ❌ **違反 AGENTS.md 的 Required Repository Structure**
- ❌ 失去「快速筆記」的彈性（表格格式較嚴格）
- ❌ candidates.md 表格會混合「已研究」和「待評估」項目（違反漸進式揭露）
- ❌ 初期 brainstorming 困難（需要立即決定分類、區域等欄位）

**結論**: 不適合，違反核心設計原則

---

### 方案B：保留但明確定義用途 ✅ **推薦**

**做法**:
1. **保留 inbox.md** 作為「初期探索」工具
2. **明確生命週期**:
   - **Phase 1: 探索階段** (status: 📝 研究中)
     - 快速收集 web_search 結果
     - 自由組織分類和筆記
     - 無需結構化
   - **Phase 2: 轉移階段** (status: 🔄 待完成)
     - 將優先候選轉移到 candidates.md（帶 `status: inbox`）
     - 開始詳細研究
   - **Phase 3: 清理階段** (標記 ✅ 已完成前)
     - 確認所有候選已轉移到 candidates.md 或 excluded.md
     - inbox.md 清空或標記為「歷史記錄（已轉移）」
3. **更新 AGENTS.md**:
   - 在 Workflow Step 1 中補充 inbox.md → candidates.md 的轉移流程
   - 在 Step 6 (Post-Research Updates) 中加入 inbox.md 清理指引
4. **更新完成標準**:
   - 加入檢查項：「inbox.md 已清理或標記為歷史記錄」

**優點**:
- ✅ 保持初期研究的彈性和效率
- ✅ 符合 Progressive Disclosure 原則
- ✅ 明確的使用場景和退出機制
- ✅ 減少「完成後不知如何處理」的困惑
- ✅ 維持 AGENTS.md 的 Required Structure 一致性

**缺點**:
- ⚠️ 需要更新 AGENTS.md 和 PROGRESS.md（一次性工作）
- ⚠️ 需要處理 Rome 和 Milan 的5個剩餘 inbox 項目

**成本**:
- 文件更新：30分鐘
- 處理剩餘項目：15-20分鐘/項 × 5 = 75-100分鐘
- **總計**: ~2小時

**結論**: 最佳方案，值得投資

---

### 方案C：改為可選文件 ⚠️ **不推薦**

**做法**:
- 從 AGENTS.md 的 Required Structure 中移除
- 改為 Optional 文件，使用者可選擇是否使用

**優點**:
- ✅ 給予使用者選擇權
- ✅ 減少對不需要此工具的使用者的負擔

**缺點**:
- ❌ 可能造成不一致（有些城市有，有些沒有）
- ❌ 違反標準化原則
- ❌ 新研究者不清楚「最佳實踐」是什麼

**結論**: 不推薦，標準化比彈性更重要

---

## 5. 最終建議

### 5.1 建議方案：方案B（保留 + 明確規範）✅

**核心改進**:
1. **明確 inbox.md 生命週期**
2. **更新 AGENTS.md 工作流程說明**
3. **更新 PROGRESS.md 完成標準**
4. **處理剩餘的 inbox 項目**

### 5.2 具體行動計劃

#### Action 1: 更新 AGENTS.md

**在 Section 7.1 (Discovery — Candidate Collection) 中補充**:

```markdown
### inbox.md 生命週期

inbox.md 是初期探索的工作空間，其生命週期如下：

1. **探索階段** (研究開始 → 收集完成)
   - 快速記錄 web_search 結果
   - 自由組織分類（傳統餐廳、披薩、甜點等）
   - 包含簡短筆記（位置、特色、注意事項、來源）
   - 無需立即結構化

2. **轉移階段** (收集完成 → 研究中)
   - 將優先候選（3-5個）轉移到 candidates.md
   - 在 candidates.md 中設置 `status: inbox`
   - 保留 inbox.md 中的其他候選作為「待評估清單」

3. **清理階段** (研究完成 → 標記完成前)
   - 確認所有相關候選已轉移到：
     - candidates.md (已研究或待研究)
     - excluded.md (明確排除)
   - 選項A：清空 inbox.md，在頂部註明「已轉移至 candidates.md」
   - 選項B：保留 inbox.md 作為歷史記錄，在頂部註明「歷史記錄（已轉移）」
   - **不可接受**：保留未處理的候選在 inbox.md 中

### inbox.md vs candidates.md

| 特性 | inbox.md | candidates.md |
|------|----------|---------------|
| 格式 | 自由筆記 | 結構化表格 |
| 目的 | 初期探索收集 | 候選摘要與狀態追蹤 |
| 時機 | 研究初期 | 研究全程 |
| 狀態 | 暫時性 | 永久性 |
| 完成時 | 清空或標記 | 保留所有記錄 |
```

**在 Section 7.6 (Post-Research Updates) 中補充**:

```markdown
5. **清理 inbox.md**:
   - 確認所有候選已轉移到 candidates.md 或 excluded.md
   - 選擇清空或標記為歷史記錄
   - 在 overview.md 檢查清單中標記完成
```

#### Action 2: 更新 PROGRESS.md

**在「研究完成標準」中加入第5項**:

```markdown
### 5. inbox.md 已清理

- `inbox.md` 不得包含未處理的候選地點
- 所有候選必須：
  - 已轉移到 `candidates.md` (任何 status)
  - **或**已明確移至 `excluded.md` 並註明原因
- `inbox.md` 應該：
  - 選項A：清空並在頂部註明「已轉移至 candidates.md」
  - 選項B：保留作為歷史記錄，在頂部註明「歷史記錄（已轉移）」

**驗證命令**:
```bash
# 手動檢查 inbox.md 頂部是否有「已轉移」或「歷史記錄」標記
head -5 inbox.md

# 檢查是否有候選尚未轉移（需人工判斷）
# 比對 inbox.md 中的地點名稱是否都出現在 candidates.md 或 excluded.md
```
```

#### Action 3: 處理剩餘 inbox 項目

**Rome (2項)**:
- Two Sizes (提拉米蘇專門店)
- Tiramisù Merisù (提拉米蘇專門店)

**Milan (3項)**:
- Sant Ambroeus (歷史糕點店)
- Cova Montenapoleone (最古老糕點店)
- Peck (美食殿堂)

**處理方式**:
1. 每個項目進行快速研究（15-20分鐘）
2. 評分並更新 candidates.md 狀態
3. 更新 notes.md 和 top-places.md（如適用）
4. 或明確排除並記錄於 excluded.md

#### Action 4: 驗證並更新進度

1. 執行完成標準檢查（包括新增的 inbox.md 檢查）
2. 更新 PROGRESS.md 狀態
3. 確認所有城市符合完成標準

---

## 6. 預期成果

### 6.1 改進後的清晰度

**使用者視角**:
- ✅ 清楚知道 inbox.md 的用途（初期探索）
- ✅ 清楚知道何時該轉移候選（開始詳細研究時）
- ✅ 清楚知道完成時該如何處理（清空或標記）

**工作流程視角**:
- ✅ 保持初期研究的彈性和效率
- ✅ 明確的轉移和退出機制
- ✅ 減少「完成後困惑」

**文件結構視角**:
- ✅ 符合 Progressive Disclosure 原則
- ✅ 清楚的文件責任劃分
- ✅ 一致的跨城市標準

### 6.2 投資回報

**一次性成本**: ~2小時（文件更新 + 處理剩餘項目）

**長期收益**:
- 減少未來研究的困惑（每個城市節省15-30分鐘思考時間）
- 提高文件一致性（減少維護負擔）
- 明確的完成標準（更容易驗證研究是否完成）

**ROI**: 高（一次投資，長期受益）

---

## 7. 結論

### 7.1 核心建議

✅ **保留 inbox.md 機制，但補充明確的使用規範和生命週期說明**

### 7.2 理由

1. **初期探索確實需要彈性工具** - 實際使用證明有效（985行，5個城市）
2. **符合設計原則** - Progressive Disclosure 的最底層
3. **投資回報高** - 2小時投資，長期減少困惑和維護負擔
4. **保持一致性** - 維持 Required Repository Structure 標準

### 7.3 必要改進

1. **更新 AGENTS.md** - 補充生命週期說明和轉移流程
2. **更新 PROGRESS.md** - 加入 inbox.md 清理檢查標準
3. **處理剩餘項目** - Rome 2項 + Milan 3項
4. **驗證完成** - 確保所有城市符合新標準

### 7.4 不建議的方案

- ❌ 完全移除 inbox.md（違反設計原則，失去彈性）
- ❌ 改為可選文件（破壞標準化）

---

## 附錄：剩餘 inbox 項目清單

### Rome (2項)
1. **Two Sizes** - tiramisù specialist (Centro)
2. **Tiramisù Merisù** - tiramisù specialist (Trastevere)

### Milan (3項)
1. **Sant Ambroeus** - 歷史糕點店 (Corso Giacomo Matteotti 7)
2. **Cova Montenapoleone** - 歷史糕點店 (Via Montenapoleone 8)
3. **Peck** - 美食殿堂 (Centro Storico)

**建議處理順序**:
1. Milan 項目（3個糕點店可一起研究）
2. Rome 項目（2個提拉米蘇店可一起研究）
