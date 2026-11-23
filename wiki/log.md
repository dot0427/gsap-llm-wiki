# log｜操作紀錄

- 2026-11-23 22:30 init｜建立 schema（CLAUDE.md）、raw/sources.md
- 2026-11-23 22:32 ingest S1｜討論 3 題 → 建 overview、plugins-and-install；價格標「待查」
- 2026-11-23 22:33 ingest S2｜討論 3 題 → 建 tween；決定不收錄 gsap.set()（來源沒講）
- 2026-11-23 22:34 ingest S3｜討論 3 題 → 建 timeline；更新 tween 相關連結
- 2026-11-23 22:35 ingest S4｜討論 3 題 → 建 scrolltrigger；更新 timeline「搭配捲動」段
- 2026-11-23 22:36 ingest S5｜討論 3 題 → 建 easing；確認預設 ease 與 S2 一致
- 2026-11-23 22:37 ingest S6｜討論 3 題 → 更新 plugins-and-install，移除「待查」，註記舊教學過時
- 2026-11-23 22:40 query｜「新手學習順序？」→ 存成 synthesis/learning-path
- 2026-11-23 22:45 lint #1｜14 個問題：13 行事實只在標題標來源、行內沒標 [S#]；1 個 lint 誤判（s2 討論紀錄寫「文件沒寫 gsap.set()」被當成事實）
- 2026-11-23 22:46 fix｜13 行補上 [S2]/[S3]/[S4]；修 lint 規則：「沒寫/待查 + gsap.set」視為註記不報錯
- 2026-11-23 22:46 lint #2｜✅ 0 問題
- 2026-11-23 23:00 generate｜依 learning-path 產生 15 頁教學 HTML 簡報，每頁標 data-wiki 與 [S#]
- 2026-11-23 23:02 check #1（自動）｜15 頁對應 Wiki ✅、API/ease/屬性皆在 Wiki ✅、瀏覽器 console 0 錯誤 ✅
- 2026-11-23 23:04 check #2（人工看截圖）｜抓到 3 個自動檢查漏掉的問題：① 第 11 頁寫「scrub 原理就是丟給 progress()」→ Wiki 沒有這個說法（生成時自己推論）② 表格第一欄中文直排換行 ③ scrub demo 文字轉到倒過來
- 2026-11-23 23:06 fix｜① 改成註明「demo 用 progress() 模擬、不是真的 ScrollTrigger」② 首欄 nowrap ③ 拿掉旋轉；重跑 check #1 ✅
- 2026-11-23 23:12 workflow v2｜新增「大綱＋claim 對應」節點；ingest 規則改為行內標 [S#]；補跑 claim 對應表 ✅
