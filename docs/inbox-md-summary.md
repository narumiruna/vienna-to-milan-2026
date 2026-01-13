# inbox.md 機制審查總結

**問題**: inbox.md 的機制是否需要存在？

**結論**: ✅ **建議保留，但需明確規範生命週期和使用方式**

---

## 快速摘要

### 為什麼保留？

1. **初期探索需要彈性工具** - 快速記錄 web_search 結果，不適合立即填入結構化表格
2. **實際使用證明有效** - 5個城市平均收集 197 行候選（總計985行）
3. **符合 Progressive Disclosure 原則** - 作為最底層的探索工具有其價值
4. **投資回報高** - 保持彈性的同時，只需補充使用指引即可

### 主要問題是什麼？

1. ❌ 沒有明確的「完成後處理」指引
2. ❌ 各城市做法不一致（107-359行差異大）
3. ❌ 有些城市留有未處理的候選（Rome: 2項, Milan: 3項）

### 解決方案

**明確 inbox.md 的三階段生命週期**:

```
階段1: 探索 (研究開始)
  ↓ 快速記錄、自由組織、無需結構化
階段2: 轉移 (開始詳細研究)
  ↓ 將優先候選轉移到 candidates.md
階段3: 清理 (標記完成前)
  ✓ 確認所有候選已轉移
  ✓ 清空或標記為歷史記錄
```

---

## 已完成的更新

### ✅ AGENTS.md
- 新增「inbox.md lifecycle」完整說明（三階段）
- 新增 inbox.md vs candidates.md 比較表
- 在 Post-Research Updates 中加入清理步驟

### ✅ PROGRESS.md
- 新增第5項完成標準：「inbox.md 已清理」
- 更新驗證檢查清單（加入 inbox.md 檢查命令）
- 更新進度指南（確保包含 inbox.md 檢查）

### ✅ 詳細分析文檔
- 創建 docs/inbox-md-analysis.md（19頁完整分析）
- 包含使用統計、優缺點分析、替代方案評估、具體行動計劃

---

## inbox.md vs candidates.md

| 特性 | inbox.md | candidates.md |
|------|----------|---------------|
| **格式** | 自由筆記 | 結構化表格 |
| **目的** | 初期探索收集 | 候選摘要與狀態追蹤 |
| **時機** | 研究初期 | 研究全程 |
| **狀態** | 暫時性 | 永久性 |
| **完成時** | 清空或標記 | 保留所有記錄 |

---

## 新的完成標準（5項）

城市標記為「✅ 已完成」必須滿足：

1. ✅ 所有候選已分類（candidates.md 無 `status: inbox`）
2. ✅ excluded.md 無待決定項目
3. ✅ top-places.md 已完成（含用餐策略）
4. ✅ overview.md 檢查清單全部完成
5. ✅ **inbox.md 已清理** ← 新增

---

## 清理 inbox.md 的兩種選擇

### 選項A: 清空並標記
```markdown
# 維也納美食候選 - 已轉移

所有候選已轉移至 candidates.md (2026-01-13)
```

### 選項B: 保留歷史記錄
```markdown
# 維也納美食候選 - 歷史記錄

歷史記錄（已轉移至 candidates.md, 2026-01-13）

以下為初期探索時的原始筆記，保留作為參考...
```

**推薦**: 選項B（保留研究軌跡）

---

## 待處理項目

### Rome (2項 tiramisu 專門店)
- Two Sizes (Centro)
- Tiramisù Merisù (Trastevere)

### Milan (3項歷史糕點店)
- Sant Ambroeus (1936年創立)
- Cova Montenapoleone (1817年創立)
- Peck (1883年創立)

**建議**: 可一起研究（各15-20分鐘），總計約1.5小時

---

## 關鍵要點

1. **inbox.md 是有用的** - 不要移除
2. **但需要明確規範** - 生命週期、清理標準已補充
3. **完成標準已更新** - 從4項增加到5項
4. **文件已同步** - AGENTS.md 和 PROGRESS.md 都已更新

---

## 參考文件

- **完整分析**: [docs/inbox-md-analysis.md](inbox-md-analysis.md)
- **工作流程**: [AGENTS.md](../AGENTS.md#1-discovery--candidate-collection)
- **完成標準**: [PROGRESS.md](../PROGRESS.md#-研究完成標準)

---

**日期**: 2026-01-13  
**狀態**: ✅ 分析完成，文件已更新
