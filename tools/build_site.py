import pathlib, re, markdown, json
root = pathlib.Path(__file__).resolve().parent.parent
GRAPH = '''<svg viewBox="0 0 900 560" style="width:100%;max-width:900px;font-family:'Noto Sans TC',sans-serif" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="#93a0b4"/></marker>
<marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="#ffb86b"/></marker></defs>
<style>.n rect{fill:#191e28;stroke:#2a3140;stroke-width:1.5}.n text{fill:#eef1f6;font-size:14px;text-anchor:middle}.e{stroke:#93a0b4;stroke-width:1.6;fill:none;marker-end:url(#ar)}.b{stroke:#ffb86b;stroke-width:1.6;fill:none;stroke-dasharray:5 4;marker-end:url(#ar2)}.l{fill:#ffb86b;font-size:12px}.g{fill:none;stroke:#7cc4ff;stroke-dasharray:3 4;stroke-width:1.2}.gt{fill:#7cc4ff;font-size:12px}.new rect{stroke:#b8f34a;stroke-width:2.2}</style>
<rect class="g" x="20" y="20" width="860" height="120" rx="14"/><text class="gt" x="34" y="40">🔁 Ingest loop（每篇來源跑一次 ×6）</text>
<g class="n"><rect x="40" y="60" width="170" height="54" rx="10"/><text x="125" y="92">① 取得資料 raw/</text></g>
<g class="n"><rect x="250" y="60" width="170" height="54" rx="10"/><text x="335" y="84">② 先討論</text><text x="335" y="104" style="font-size:12px;fill:#93a0b4">3 個問題</text></g>
<g class="n"><rect x="460" y="60" width="170" height="54" rx="10"/><text x="545" y="92">③ 寫來源頁</text></g>
<g class="n"><rect x="670" y="60" width="190" height="54" rx="10"/><text x="765" y="84">④ 更新概念頁</text><text x="765" y="104" style="font-size:12px;fill:#93a0b4">index / log・行內 [S#]</text></g>
<path class="e" d="M210 87H250"/><path class="e" d="M420 87H460"/><path class="e" d="M630 87H670"/>
<path class="b" d="M765 60V48H125V60"/><text class="l" x="400" y="44">下一篇</text>
<g class="n"><rect x="670" y="180" width="190" height="54" rx="10"/><text x="765" y="212">⑤ Lint 健康檢查</text></g>
<path class="e" d="M765 114V180"/>
<path class="b" d="M860 207H885V87H860"/><text class="l" x="830" y="160">失敗 → 回 ④</text>
<g class="n"><rect x="430" y="180" width="190" height="54" rx="10"/><text x="525" y="204">⑥ Query</text><text x="525" y="224" style="font-size:12px;fill:#93a0b4">學習順序 → synthesis</text></g>
<path class="e" d="M670 207H620"/><text x="636" y="198" style="fill:#b8f34a;font-size:12px">通過</text>
<g class="n new"><rect x="160" y="180" width="220" height="54" rx="10"/><text x="270" y="204">⑦ 大綱＋claim 對應</text><text x="270" y="224" style="font-size:12px;fill:#b8f34a">v2 新增（檢查往前移）</text></g>
<path class="e" d="M430 207H380"/>
<path class="b" d="M270 180V160H500V180"/><text class="l" x="300" y="155">對不到 → 補 Wiki / 重 query</text>
<g class="n"><rect x="160" y="300" width="220" height="54" rx="10"/><text x="270" y="332">⑧ 生成 HTML 簡報</text></g>
<path class="e" d="M270 234V300"/>
<g class="n"><rect x="430" y="300" width="220" height="54" rx="10"/><text x="540" y="324">⑨ 自動檢查</text><text x="540" y="344" style="font-size:12px;fill:#93a0b4">對應 / API / console</text></g>
<path class="e" d="M380 327H430"/>
<g class="n"><rect x="430" y="420" width="220" height="54" rx="10"/><text x="540" y="444">⑩ 人工看畫面</text><text x="540" y="464" style="font-size:12px;fill:#93a0b4">語意 / 版面 / demo</text></g>
<path class="e" d="M540 354V420"/>
<path class="b" d="M480 300V280H300V300"/><text class="l" x="330" y="275">失敗 → 回 ⑧</text>
<path class="b" d="M430 447H270V354"/><text class="l" x="290" y="440">失敗 → 回 ⑧</text>
<g class="n"><rect x="700" y="420" width="160" height="54" rx="10" style="fill:#b8f34a;stroke:#b8f34a"/><text x="780" y="452" style="fill:#10131a;font-weight:700">✅ 發佈</text></g>
<path class="e" d="M650 447H700"/>
<text x="40" y="530" style="fill:#93a0b4;font-size:13px">橘色虛線＝會重複執行的回圈・綠框＝第一次執行後新增的節點</text>
</svg>'''
sections = [("作業說明", [("about", "report/about.md", "作業總覽"), ("graph", "report/graph.md", "loop / graph 設計"),
             ("runlog", "report/runlog.md", "實際執行紀錄"), ("reflection", "report/reflection.md", "反思"), ("claims", "report/claims.md", "簡報↔Wiki 對應表")]),
            ("Wiki", [("index", "wiki/index.md", "index 目錄"), ("overview", "wiki/overview.md", "overview 總覽"), ("log", "wiki/log.md", "log 操作紀錄")]),
            ("概念頁", [(n, f"wiki/concepts/{n}.md", n) for n in ["tween", "timeline", "easing", "scrolltrigger", "plugins-and-install"]]),
            ("整合頁", [("learning-path", "wiki/synthesis/learning-path.md", "learning-path")]),
            ("來源頁", [(p.stem, f"wiki/sources/{p.name}", p.stem) for p in sorted((root / "wiki/sources").glob("*.md"))]),
            ("Schema / Raw", [("schema", "CLAUDE.md", "CLAUDE.md"), ("raw", "raw/sources.md", "raw/sources.md")])]
nav, pages = [], {}
for title, items in sections:
    nav.append(f'<div class="sec">{title}</div>')
    for slug, path, label in items:
        md = (root / path).read_text()
        md = re.sub(r"\[\[([^\]]+)\]\]", lambda m: f'<a class="wl" href="#{m.group(1)}">{m.group(1)}</a>', md)
        h = markdown.markdown(md, extensions=["tables", "fenced_code"])
        h = h.replace("<p>%%GRAPH%%</p>", GRAPH)
        h = re.sub(r"\[(S\d)\]", r'<span class="src">\1</span>', h)
        pages[slug] = h
        nav.append(f'<a href="#{slug}" data-s="{slug}">{label}</a>')
html = f'''<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GSAP LLM Wiki</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
:root{{--bg:#10131a;--panel:#161a23;--ink:#eef1f6;--mute:#93a0b4;--acc:#b8f34a;--acc2:#7cc4ff;--line:#2a3140}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Noto Sans TC",sans-serif;display:flex;min-height:100vh}}
nav{{width:250px;flex:0 0 250px;background:var(--panel);border-right:1px solid var(--line);padding:22px 14px;position:sticky;top:0;height:100vh;overflow:auto}}
nav .brand{{font-weight:900;font-size:20px;margin:0 8px 4px}}nav .sub{{color:var(--mute);font-size:12px;margin:0 8px 14px}}
nav .sec{{color:var(--acc);font-size:12px;letter-spacing:.1em;margin:16px 8px 6px;font-weight:700}}
nav a{{display:block;color:#cfd6e2;text-decoration:none;padding:6px 10px;border-radius:8px;font-size:14px}}nav a:hover{{background:#202634}}nav a.on{{background:#232b1a;color:var(--acc)}}
main{{flex:1;min-width:0;padding:40px 6vw 80px;max-width:1080px}}
h1{{font-size:32px;font-weight:900;margin-top:0}}h2{{margin-top:2em;font-size:22px;border-left:4px solid var(--acc);padding-left:10px}}
p,li{{line-height:1.8;color:#d5dbe5}}a{{color:var(--acc2)}}a.wl{{background:#1d2633;padding:1px 7px;border-radius:6px;text-decoration:none}}
code{{font-family:"JetBrains Mono",monospace;background:#232a37;padding:1px 6px;border-radius:5px;font-size:.9em;color:#e6f7c7}}
pre{{background:#0b0e13;border:1px solid var(--line);border-radius:10px;padding:14px 18px;overflow:auto}}pre code{{background:none;padding:0}}
table{{border-collapse:collapse;width:100%;margin:12px 0;font-size:14.5px}}td,th{{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}}th{{background:#1a1f2a;color:var(--mute)}}
blockquote{{border-left:3px solid var(--acc2);margin:0;padding:4px 16px;color:var(--mute)}}
.src{{display:inline-block;font-size:11px;font-weight:700;background:#232b1a;color:var(--acc);padding:0 6px;border-radius:5px;margin:0 1px}}
@media(max-width:760px){{body{{flex-direction:column}}nav{{width:100%;height:auto;position:static;flex:none}}}}
</style></head><body>
<nav><div class="brand">GSAP LLM Wiki</div><div class="sub">豆特・NIU 資工四・6 sources / 15 pages</div>{"".join(nav)}</nav>
<main id="main"></main>
<script>
const P={json.dumps(pages, ensure_ascii=False)};
function show(){{let s=location.hash.slice(1);if(!P[s])s="about";document.getElementById("main").innerHTML=P[s];
document.querySelectorAll("nav a").forEach(a=>a.classList.toggle("on",a.dataset.s===s));scrollTo(0,0);}}
addEventListener("hashchange",show);show();
</script></body></html>'''
(root / "gsap-wiki.html").write_text(html)
print("built", len(pages), "pages")
