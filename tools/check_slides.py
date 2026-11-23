"""簡報檢查：(1) 每頁 data-wiki 對得到 Wiki 頁 (2) 簡報可見文字中的 API／ease 都在 Wiki 裡 (3) 預設值與 Wiki 一致"""
import re, sys, pathlib, html
slides_html = pathlib.Path(sys.argv[1]).read_text()
wiki = pathlib.Path(sys.argv[2])
pages = {p.stem for p in wiki.rglob("*.md")}
wtext = "\n".join(p.read_text() for p in wiki.rglob("*.md"))
body = slides_html.split("<main", 1)[1].split("</main>", 1)[0]
secs = re.findall(r'<section class="slide" data-wiki="([^"]+)">(.*?)</section>', body, re.S)
probs = []
print(f"slides={len(secs)}")
for i, (w, s) in enumerate(secs, 1):
    if w not in pages:
        probs.append(f"[對應不到] 第{i}頁 data-wiki={w}")
    txt = html.unescape(re.sub(r"<[^>]+>", " ", s))
    for api in set(re.findall(r"\b(?:gsap\.)?([a-zA-Z]+)\(\)", txt)) | set(re.findall(r"gsap\.([a-zA-Z]+)\(", txt)):
        if api not in wtext:
            probs.append(f"[Wiki 沒有] 第{i}頁 API {api}()")
    for e in set(re.findall(r'"((?:power\d|back|bounce|elastic|expo|sine|circ)\.\w+|none)"', txt)):
        if e.split(".")[0] not in wtext:
            probs.append(f"[Wiki 沒有] 第{i}頁 ease {e}")
    for prop in set(re.findall(r"\b(stagger|pin|scrub|markers|toggleActions|yoyo|repeat|onComplete|rotation)\b", txt)):
        if prop not in wtext:
            probs.append(f"[Wiki 沒有] 第{i}頁 屬性 {prop}")
    m = re.search(r"duration</code>\s*=\s*<b>([\d.]+)", s)
    if m and m.group(1) != "0.5":
        probs.append(f"[預設值不一致] 第{i}頁 duration={m.group(1)}")
print("\n".join(probs) or "✅ 對應檢查全部通過")
