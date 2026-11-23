# overview｜GSAP 是什麼（總覽）

- GSAP（GreenSock Animation Platform）是 JavaScript 動畫函式庫，可以動 CSS 屬性、HTML 屬性、數字、顏色 [S1]。
- 核心兩塊積木：[[tween]]（一段動畫）與 [[timeline]]（排動畫的容器）[S1]。
- 手感靠 [[easing]] 調整 [S5]；捲動動畫靠外掛 [[scrolltrigger]] [S4]。
- 2025 年起全部免費、可商用 [S6]，安裝見 [[plugins-and-install]]。

## 心智模型（三句話）
1. **選誰動**：CSS 選擇器，例如 `".box"` [S2]
2. **動成怎樣**：屬性物件，例如 `{ x: 200, duration: 1 }` [S2]
3. **什麼時候動**：馬上動（tween）、排隊動（[[timeline]]）、捲到才動（[[scrolltrigger]]）

延伸：[[learning-path]]
