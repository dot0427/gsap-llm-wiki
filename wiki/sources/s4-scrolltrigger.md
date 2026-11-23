# S4｜ScrollTrigger（捲動觸發）

- 來源：https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- 連到：[[scrolltrigger]]、[[plugins-and-install]]、[[timeline]]

## 重點
- 不在核心裡，要 `gsap.registerPlugin(ScrollTrigger)`；忘記註冊，正式版 build 可能失效。
- `start` / `end` 字串 = 「trigger 的哪裡」碰到「畫面的哪裡」。`"top center"` = 元素頂端碰到畫面中間。預設 start `"top bottom"`、end `"bottom top"`。
- `scrub`：動畫進度綁捲軸；數字 = 追上的平滑秒數。
- `pin`：捲動時把元素釘住。**不要動被 pin 的元素本身，要動它的子元素。**
- `markers`：開發時顯示起訖線。
- `toggleActions`：四個時間點（onEnter、onLeave、onEnterBack、onLeaveBack），預設 `"play none none none"`。
- 可以掛在 timeline 上；**不要在 timeline 裡每個子 tween 各掛一個 ScrollTrigger。**
- 常見錯誤：建立順序要由上到下、祖先元素有 transform 會讓 pin 壞掉、React 卸載時要清理。

## 先討論紀錄
| 討論問題 | 結論 |
|---|---|
| scrub 和 toggleActions 差在哪？ | toggleActions = 碰到就「播一次」；scrub = 捲多少播多少，像拖影片進度條 |
| "top center" 新手最容易搞混什麼？ | 第一個字是元素、第二個字是畫面 → 簡報畫圖解釋 |
| 作品集要用哪個？ | 區塊淡入用 toggleActions；橫向捲動展示用 pin + scrub |
