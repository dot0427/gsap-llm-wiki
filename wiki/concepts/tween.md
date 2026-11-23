# tween｜補間動畫

一段「從 A 值變到 B 值」的動畫，是 GSAP 真正做動畫工作的單位 [S2]。

## 三種寫法 [S2]
| 方法 | 意思 | 適合 |
|---|---|---|
| `gsap.to(".box", { x: 100 })` | 現在 → 指定值 | 一般移動 |
| `gsap.from(".box", { opacity: 0 })` | 指定值 → 現在 | 進場動畫 |
| `gsap.fromTo(".box", {x:0}, {x:100})` | 起終點都指定 | 要精準控制時 |

## 常用屬性 [S2]
- `duration`：秒數，**預設 0.5** [S2]
- `delay`：延遲秒數 [S2]
- `ease`：緩動，**預設 "power1.out"**（見 [[easing]]）
- `repeat`：重複次數，`-1` = 無限；`yoyo: true` = 來回 [S2]
- `stagger`：多個目標錯開開始時間 [S2]
- `onComplete`：播完要做的事 [S2]
- `x` / `y` / `rotation`：transform 簡寫（`x` = `translateX()`） [S2]

## 控制 [S2]
```js
let tw = gsap.to(".box", { rotation: 360, duration: 5 });
tw.pause(); tw.play(); tw.reverse(); tw.seek(2); tw.progress(0.5);
```

> ⚠️ `gsap.set()`：S2 沒有說明，暫不收錄（待查）。

相關：[[timeline]]、[[overview]]
