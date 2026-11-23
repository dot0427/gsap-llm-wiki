# timeline｜時間軸

把多個 [[tween]] 排在一起、整組控制的容器 [S3]。

## 為什麼需要 [S3]
- 不用 timeline：每段都要手算 `delay`，改第一段長度 → 後面全部要改。 [S3]
- 用 timeline：時間自動接上，一行就能整組暫停／倒轉／重播。 [S3]

## 基本用法 [S3]
```js
let tl = gsap.timeline({ defaults: { duration: 1 } });
tl.to("#a", { x: 300 })
  .to("#b", { x: 300 })          // 接在後面
  .to("#c", { x: 300 }, "<")     // 跟上一段同時
  .to("#d", { x: 300 }, "-=0.5"); // 提早 0.5 秒（重疊）
```

## 位置參數速查 [S3]
| 寫法 | 意思 |
|---|---|
| （不寫） | 接在最後 |
| `3` | 第 3 秒 |
| `"+=1"` / `"-=0.5"` | 空 1 秒 / 重疊 0.5 秒 |
| `"<"` / `">"` | 上一段開始時 / 結束時 |
| `"label"` | 在標籤位置 |

## 其他 [S3]
- `defaults`：子 tween 共用的設定，子 tween 自己寫的會覆蓋。 [S3]
- 控制：`pause()`、`resume()`、`reverse()`、`seek()`、`timeScale()`。 [S3]
- 可巢狀：`master.add(intro()).add(middle(), "+=2")`。 [S3]
- 搭配捲動：把 ScrollTrigger 掛在 timeline 上，見 [[scrolltrigger]] [S4]。
