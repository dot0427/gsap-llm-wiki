# S1｜GSAP 官方文件首頁

- 來源：https://gsap.com/docs/v3/ （文件版本 v3.15）
- 連到：[[overview]]、[[plugins-and-install]]、[[tween]]、[[timeline]]

## 重點
- GSAP 是 JavaScript 動畫函式庫，可以動 CSS 屬性、HTML 屬性、數字、顏色、含數字的字串。
- 兩個核心積木：**Tween**（一段動畫）和 **Timeline**（把動畫排在一起的容器）。
- 核心刻意保持小；額外功能用外掛按需載入：捲動（ScrollTrigger、ScrollSmoother）、文字（SplitText）、SVG（DrawSVG、MorphSVG）、UI（Flip、Draggable）等。
- React 有 `useGSAP()`。
- 清理與響應式：`gsap.context()`／`revert()`、`gsap.matchMedia()`。

## 先討論紀錄
| 討論問題 | 結論 |
|---|---|
| 我要做的東西（作品集、投影頁）需要哪幾塊？ | 先學 core 的 Tween → Timeline，再學 ScrollTrigger；SVG/文字外掛之後再說 |
| 首頁沒寫價格，GSAP 要錢嗎？ | 首頁沒說 → 標「待查」，等 S6 補 |
| 要不要現在就學 React 版 useGSAP？ | 不要，我還沒學 React，先用純 HTML＋JS |
