# GSAP LLM Wiki — Schema（給 LLM 看的維護規則）

主題：GSAP 網頁動畫（GreenSock Animation Platform）
目的：讓我（豆特）從零學會用 GSAP 做作品集、活動投影頁、抽獎頁的動畫。

## 三層結構
- `raw/`：原始資料清單（網址＋擷取日期）。**不可改寫**，是唯一事實來源。
- `wiki/`：LLM 寫、我讀的知識頁。
  - `sources/`：一篇來源一頁（重點＋先討論紀錄）
  - `concepts/`：一個概念一頁（Tween、Timeline、Easing、ScrollTrigger、外掛與安裝）
  - `synthesis/`：Query 後值得留下的整合答案
  - `index.md`：內容目錄（Query 時先讀這裡）
  - `log.md`：時間序操作紀錄
- `CLAUDE.md`：本檔。

## Ingest 流程（先討論、後生成）
1. 讀來源 → **先列 3 個討論問題**跟我討論（我在乎什麼？跟現有頁面有沒有衝突？）
2. 討論有結論後才寫 `sources/xx.md`
3. 更新相關 `concepts/` 頁，每條事實後面標來源 `[S#]`
4. 更新 `index.md`、在 `log.md` 追加一筆

## Query 流程
先讀 `index.md` → 找相關頁 → 回答並標 `[S#]`；有價值的答案存進 `synthesis/`。

## Lint 規則（健康檢查）
- 每條事實都要有 `[S#]`，沒有就標「待查」
- 不可有斷掉的 `[[連結]]`、不可有孤兒頁（沒被任何頁連到）
- 預設值（duration、ease、toggleActions…）在不同頁必須一致
- 來源沒講的東西不准寫成事實（例：S2 沒講 `gsap.set()`）

## v2 修改（第一次執行後）
- Ingest 寫概念頁時，**每一行事實當下就標 [S#]**（不要只標在標題）
- 生成簡報前必須先做「大綱＋claim 對應」：每句說法 ↔ Wiki 一行；對不到就不准寫，或先回去補 Wiki（附來源）
- lint：討論紀錄中「來源沒講 X」屬於註記，不算事實
