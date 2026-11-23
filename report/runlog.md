# 一次實際執行紀錄（2026-11-23）

## Ingest（6 篇）
| 來源 | 討論題數 | 產生 / 更新的頁面 |
|---|---|---|
| S1 官方文件首頁 | 3 | 新增 overview、plugins-and-install（價格標「待查」） |
| S2 Tween | 3 | 新增 tween；決定不收錄 `gsap.set()`（來源沒講） |
| S3 Timeline | 3 | 新增 timeline |
| S4 ScrollTrigger | 3 | 新增 scrolltrigger；更新 timeline |
| S5 Eases | 3 | 新增 easing；確認預設 ease 與 S2 一致 |
| S6 免費公告 | 3 | 更新 plugins-and-install，移除「待查」、註記舊教學過時 |

## Lint
**第 1 輪：14 個問題 ❌**
```
[缺來源] tween: - `duration`：秒數，**預設 0.5**
[缺來源] timeline: - `defaults`：子 tween 共用的設定…
[缺來源] scrolltrigger: - `pin: true`：把元素釘住…
…（共 13 行事實只在標題標了 [S2]，行內沒標）
[來源未覆蓋] s2-tween 提到 gsap.set() 但無來源   ← lint 誤判
```
- 修正：13 行補上行內 [S#]；修改 lint 規則，「沒寫／待查＋gsap.set」視為註記
- **第 2 輪：0 問題 ✅**

## 簡報檢查
**自動檢查 #1：全部通過 ✅**
```
slides=15
✅ 對應檢查全部通過（每頁 data-wiki 都存在、API / ease / 屬性都在 Wiki 裡）
console errors: none
```
**人工看截圖 #2：抓到 3 個問題 ❌**
1. 第 11 頁寫「scrub 的原理就是把捲動進度丟給 `progress()`」→ **Wiki 沒有這個說法**，是生成時自己推論的。自動檢查只看到 `progress()` 這個字在 Wiki 裡就放行了。
2. 表格第一欄「行為」「預設」被擠成直排。
3. scrub demo 的方塊會旋轉，文字轉到倒過來。

修正後重跑自動檢查 ✅。完整時間序見 [[log]]。
