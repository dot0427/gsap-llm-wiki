# GSAP LLM Wiki → 教學 HTML 簡報

用 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 建立「GSAP 網頁動畫」知識庫，再以 Wiki 為唯一知識來源產生教學型 HTML 簡報。

- 🎞️ 教學簡報：`site/slides.html`
- 📚 Wiki 網站：`site/wiki.html`（含 loop/graph 流程圖、執行紀錄、反思）

## 結構
```
CLAUDE.md          schema：ingest / query / lint 規則（含 v2 修改）
raw/sources.md     6 篇原始資料（不可修改）
wiki/
  sources/         一篇來源一頁（重點＋先討論紀錄）
  concepts/        tween / timeline / easing / scrolltrigger / plugins-and-install
  synthesis/       learning-path（Query 產物＝簡報大綱）
  index.md  log.md
report/            作業說明：graph、runlog、reflection、claims 對應表
tools/
  lint.py          Wiki 健康檢查（斷連結、孤兒頁、缺來源、預設值一致）
  check_slides.py  簡報 ↔ Wiki 對應檢查
  build_site.py    把 Wiki 轉成網站
```

## 流程（v2）
取得資料 → 先討論 → 寫來源頁 → 更新概念頁（🔁 ×6）→ Lint（失敗回上一步）→ Query → **大綱＋claim 對應（v2 新增）** → 生成簡報 → 自動檢查 → 人工看畫面（失敗回生成）

## 重跑檢查
```bash
python3 tools/lint.py wiki
python3 tools/check_slides.py site/slides.html wiki
```

資料來源：GSAP 官方文件（gsap.com/docs/v3）與 GSAP 3.13 公告。
