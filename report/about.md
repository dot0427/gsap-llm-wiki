# 作業總覽：GSAP LLM Wiki → 教學 HTML 簡報

## 1. LLM Wiki 主題與簡介
**主題：GSAP 網頁動畫入門**

我最近在做作品集、處室網頁、活動投影頁、抽獎網頁，都需要「讓網頁動起來」，所以選 GSAP 當主題。
這個 Wiki 依照 Karpathy 的 LLM Wiki 模式建立：

- `raw/`：6 篇原始資料（GSAP 官方文件 5 篇＋官方 3.13 免費公告），不可修改
- `wiki/`：LLM 寫的知識頁（6 篇來源頁、5 篇概念頁、1 篇整合頁、index、log）
- `CLAUDE.md`：schema，規定 ingest / query / lint 怎麼做

每篇資料 ingest 前都先列 3 個討論問題、討論完才生成頁面（先討論、後生成），紀錄在每篇來源頁的「先討論紀錄」表格。

## 2. 成果連結
- 📚 LLM Wiki：就是這個網站（左側選單可瀏覽每一頁）
- 🎞️ 教學 HTML 簡報：另一個連結（15 頁，含 5 個可以按的 GSAP 互動 demo）

## 3. Wiki ↔ 簡報對應
簡報每一頁左下角都標「Wiki 對應：xxx.md・來源 [S#]」，簡報大綱 = Wiki 的 Query 產物 [[learning-path]]。完整對應表見 [[claims]]。
