"""Wiki lint：斷連結、孤兒頁、缺來源標記、預設值一致性、禁止詞。"""
import re, pathlib, sys
root = pathlib.Path(sys.argv[1])
pages = {p.stem: p for p in root.rglob("*.md")}
links, problems = {}, []
for name, p in pages.items():
    t = p.read_text()
    links[name] = set(re.findall(r"\[\[([^\]]+)\]\]", t))
    for l in links[name]:
        if l not in pages:
            problems.append(f"[斷連結] {name} → [[{l}]]")
    if p.parent.name == "concepts":
        for ln in t.splitlines():
            if ln.startswith("- ") and "[S" not in ln and "[[" not in ln and "待查" not in ln \
               and "慣例" not in ln and not ln.startswith("- `.") and "~~" not in ln:
                problems.append(f"[缺來源] {name}: {ln.strip()[:40]}")
linked = set().union(*links.values())
for name in pages:
    if name not in linked and name not in ("index",):
        problems.append(f"[孤兒頁] {name}")
alltext = "\n".join(p.read_text() for p in pages.values())
for key, want in [("duration", "0.5"), ("ease", "power1.out")]:
    found = set(re.findall(rf"預設 {key}[^\n]*?(\d\.\d|power\d\.\w+)", alltext, re.I))
    if found and found != {want}:
        problems.append(f"[預設值不一致] {key}: {found}")
for name, p in pages.items():
    txt=p.read_text()
    if "gsap.set(" in txt and not re.search(r"(沒寫|沒有|待查|沒講)[^\n]*gsap\.set|gsap\.set[^\n]*(沒寫|沒有|待查|沒講)", txt):
        problems.append(f"[來源未覆蓋] {name} 提到 gsap.set() 但無來源")
print(f"pages={len(pages)}  problems={len(problems)}")
print("\n".join(problems) or "✅ 全部通過")
