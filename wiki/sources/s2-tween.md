# S2｜Tween（補間動畫）

- 來源：https://gsap.com/docs/v3/GSAP/Tween
- 連到：[[tween]]、[[easing]]

## 重點
- Tween 是「真正做動畫工作的東西」。
- `gsap.to()`：從現在的值 → 你給的值；`gsap.from()`：從你給的值 → 現在的值；`gsap.fromTo()`：起點終點都自己給。
- 預設 `duration` 是 **0.5 秒**；預設 `ease` 是 **"power1.out"**。
- 特殊屬性：`duration`、`delay`、`ease`、`repeat`（-1 = 無限）、`yoyo`、`stagger`、`onComplete`。
- `x`、`y`、`rotation` 是 transform 的簡寫（`x` = `translateX()`）。
- 存成變數可控制：`pause()`、`play()`、`reverse()`、`seek()`、`progress()`。
- Tween 預設建立就播放，播完自動回收。

## 先討論紀錄
| 討論問題 | 結論 |
|---|---|
| to / from 差在哪？哪個比較常用？ | 「進場動畫」用 `from` 最直覺（從看不見 → 原本位置），一般移動用 `to` |
| 文件沒寫 `gsap.set()`，要寫進 wiki 嗎？ | **不寫成事實**，這頁沒講。lint 規則加一條 |
| stagger 對我有什麼用？ | 抽獎卡片、清單一張一張出現 → 簡報要放 demo |
