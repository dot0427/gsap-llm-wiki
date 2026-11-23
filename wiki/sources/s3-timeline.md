# S3｜Timeline（時間軸）

- 來源：https://gsap.com/docs/v3/GSAP/Timeline
- 連到：[[timeline]]、[[scrolltrigger]]

## 重點
- Timeline 是裝 tween 的容器，可以整組控制。`let tl = gsap.timeline();`
- 串接 `.to()` 會一個接一個播。
- **位置參數**（第三個參數）：數字 = 絕對秒數；`"+=1"` 空 1 秒；`"-=0.5"` 重疊 0.5 秒；`"<"` 跟上一段同時開始；`">"` 上一段結束時；也可以用 label。
- `defaults` 可以把 duration / ease 套給所有子 tween，子 tween 自己寫的會覆蓋。
- 控制：`pause()`、`resume()`、`seek()`、`reverse()`、`play("label")`、`timeScale()`。
- 可以巢狀：大 timeline 裡放小 timeline。
- **為什麼要用**：不用 timeline 就得每段算 delay，改第一段長度後面全部要改；用 timeline 會自動調整。

## 先討論紀錄
| 討論問題 | 結論 |
|---|---|
| 位置參數符號好多，新手最需要哪幾個？ | `"<"`（同時）和 `"-=0.5"`（重疊）最常用，簡報只教這兩個＋預設串接 |
| 跟 S2 的 delay 衝突嗎？ | 不衝突，但 timeline 解決了 delay 連鎖修改的痛點 → 簡報用「delay 地獄 vs timeline」對比 |
| 什麼時候該用 timeline？ | 只要有 2 段以上有先後順序的動畫就用 |
