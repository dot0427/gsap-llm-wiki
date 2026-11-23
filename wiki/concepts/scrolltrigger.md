# scrolltrigger｜捲動觸發

讓動畫在「捲到某處」才發生，或跟著捲軸進度播放的外掛 [S4]。

## 一定要先註冊 [S4]
```js
gsap.registerPlugin(ScrollTrigger);
```

## start / end 怎麼讀 [S4]
`start: "top center"` = **元素的 top** 碰到 **畫面的 center** 時開始。
第一個字 = 元素，第二個字 = 畫面。預設 start `"top bottom"`、end `"bottom top"`。

## 兩種模式 [S4]
| | toggleActions | scrub |
|---|---|---|
| 行為 | 碰到線就播一次 | 捲多少播多少（像拖進度條） |
| 預設 | `"play none none none"` | `true` 或秒數（平滑） |
| 例子 | 區塊淡入 | 視差、橫向捲動 |

## 其他 [S4]
- `pin: true`：把元素釘住；**要動子元素，不要動被釘的元素本身** [S4]
- `markers: true`：開發時看起訖線 [S4]
- 多段動畫：把一個 ScrollTrigger 掛在 [[timeline]] 上，**不要每個子 tween 各掛一個**

## 常見錯誤 [S4]
忘記註冊、建立順序不是由上到下、祖先有 `transform` 讓 pin 壞掉、React 卸載沒清理。

相關：[[plugins-and-install]]
