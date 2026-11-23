# S5｜Eases（緩動）

- 來源：https://gsap.com/docs/v3/Eases
- 連到：[[easing]]、[[tween]]

## 重點
- Ease 控制動畫的時間節奏，是改變「手感」的主要方法。
- 預設 `"power1.out"`；可用 `gsap.defaults({ ease: ... })` 或 timeline 的 `defaults` 改。
- 大多有 `in` / `out` / `inOut` 三種變化，寫法 `"名稱.變化"`，例如 `"power2.out"`、`"back.inOut"`。
- 核心 ease：`none`（線性）、`power1`~`power4`、`back`、`bounce`、`circ`、`elastic`、`expo`、`sine`、`steps`。
- `rough`、`slow`、`expoScale` 在 EasePack；CustomEase 等另外打包。

## 先討論紀錄
| 討論問題 | 結論 |
|---|---|
| 文件沒解釋 in/out 的意思，wiki 要怎麼寫？ | 標註「S5 只列出、沒解釋」；解釋用一般動畫常識：out = 開頭快結尾慢（減速停下）、in = 開頭慢結尾快 |
| 跟 S2 的預設值一致嗎？ | 一致，都是 "power1.out" ✅ |
| 簡報要怎麼教 ease？ | 做一個「同時跑 4 顆球」的 demo，用看的比用講的快 |
