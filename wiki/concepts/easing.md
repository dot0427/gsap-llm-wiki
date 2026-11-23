# easing｜緩動

控制動畫「節奏」的函數，是改變手感最主要的方法 [S5]。

- **預設 "power1.out"** [S2][S5]（兩來源一致 ✅）
- 寫法：`ease: "名稱.變化"`，例如 `"power2.out"`、`"back.inOut"`；線性用 `"none"` [S5]
- 改全域預設：`gsap.defaults({ ease: "power2.in" })`；或 timeline 的 `defaults` [S5]

## 核心 ease [S5]
`none`、`power1`~`power4`、`back`、`bounce`、`circ`、`elastic`、`expo`、`sine`、`steps`

## in / out / inOut
> S5 只列出變化、沒解釋意思。以下為一般動畫慣例（非 S5 原文）：
- `.out`：開始快、結尾慢 → 自然停下，最適合 UI 進場
- `.in`：開始慢、結尾快 → 適合離場
- `.inOut`：兩頭慢中間快

相關：[[tween]]
