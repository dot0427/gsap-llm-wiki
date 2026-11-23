# plugins-and-install｜外掛與安裝

## 價格
- ~~待查（S1 沒寫）~~ → **全部免費、可商用**，含以前付費的 SplitText、MorphSVG 等 [S6]
- ⚠️ 2025 年以前的教學說外掛要付費，已過時 [S6]

## 安裝 [S6]
所有外掛都在公開 npm 套件裡：
```bash
npm install gsap
```
```js
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);
```
不想裝 npm：用 CDN 的 `<script>` 載入（S1 列出 CDN 與 npm 兩種方式）[S1]。

## 外掛地圖 [S1]
| 類別 | 外掛 |
|---|---|
| 捲動 | ScrollTrigger、ScrollTo、ScrollSmoother |
| 文字 | SplitText、ScrambleText、TextPlugin |
| SVG | DrawSVG、MorphSVG、MotionPath |
| UI | Flip、Draggable、Inertia、Observer |
| React | `useGSAP()` |

相關：[[scrolltrigger]]、[[overview]]
