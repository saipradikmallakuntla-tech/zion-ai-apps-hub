#!/usr/bin/env python3
"""Batch 22: dependency-free source checks; no network, browser or app mutation.
Place all four owned checkouts side by side. Run with a 15-second outer timeout.
"""
import argparse, hashlib, json, re
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
NETWORK = ROOT.parent
OWNER = "saipradikmallakuntla-tech"
ORIGIN = "https://" + OWNER + ".github.io/"
REPOS = ["zion-ai-apps-hub", "llm-stream-inspector", "agent-retry-safety-lab", "cors-cookie-doctor"]
LOCALES = {"en": "", "es": "es/", "pt": "pt/"}
IDS = ["overview", "pattern-stream", "pattern-retry", "pattern-browser", "recipe-stream", "recipe-retry", "recipe-browser", "recipe-composed", "evidence-contract", "limits", "continue"]
PINS = {'zion-ai-apps-hub/.nojekyll': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391', 'zion-ai-apps-hub/app.js': '7e12a12f6f4d4edbe457d9d160ccba26a6b78f51', 'zion-ai-apps-hub/case-studies.html': '337e578203feda22094e8db8f9861199521cbdbc', 'zion-ai-apps-hub/changelog.html': 'b7a2da2a6ae679675f9aa93f747da7f346e38fc5', 'zion-ai-apps-hub/diagnostics-matrix.html': 'aaa01e9a9b991ff926bc9eb5e0ebc22a6bb2210f', 'zion-ai-apps-hub/es/case-studies.html': 'ca80686844bc3403aa0d3da9d5be433fc3f2f924', 'zion-ai-apps-hub/es/changelog.html': '19338faa658979681d613a27537de9f347e07ae0', 'zion-ai-apps-hub/es/diagnostics-matrix.html': 'ae0c3bc8fec499f67e2d7a832c585fa53c7f2052', 'zion-ai-apps-hub/es/legal-compliance-care.html': 'e408d5b6e26a5d771268141f897535a9b66f2312', 'zion-ai-apps-hub/legal-compliance-care.html': '178a0e1140935cf13550f6a9cb81e3377725e96e', 'zion-ai-apps-hub/pt/case-studies.html': '13d5ab47533e20e4d24be4eee138d8f6eae3f40c', 'zion-ai-apps-hub/pt/changelog.html': '52e56aff2daa067781ed6ae7e6d3eab9d2a7deec', 'zion-ai-apps-hub/pt/diagnostics-matrix.html': '4db72cfd1113d0e8e98dc8cfeb55bf1e1b523cc3', 'zion-ai-apps-hub/pt/legal-compliance-care.html': '4ebab21a6c778c354a6ab8d695f229e30537d6f8', 'zion-ai-apps-hub/styles.css': '8d8e544caeb4a20dad4ebefe160d1b136174504d', 'llm-stream-inspector/.nojekyll': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391', 'llm-stream-inspector/app.js': '5db9e188d24b0485c72795c05d151d5cd0716f3b', 'llm-stream-inspector/styles.css': '8121090b66979aef1b7179aa69e5cce48e7814e2', 'agent-retry-safety-lab/.nojekyll': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391', 'agent-retry-safety-lab/app.js': '97f50f921915b767624df314e567cc7d081f9863', 'agent-retry-safety-lab/styles.css': 'a88c31ca331ede8ba6e893acdf6a176be6e17569', 'cors-cookie-doctor/.nojekyll': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391', 'cors-cookie-doctor/app.js': '242fd131dbfa0c37eaa81873e4820c9fce88b17d', 'cors-cookie-doctor/styles.css': '5ae532999334aa999140c29126aca11551b38d72'}
checks = links = 0

def check(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)

@lru_cache(None)
def read(repo, path):
    return (NETWORK / repo / path).read_text(encoding="utf-8")

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
    handle_startendtag = handle_starttag
    def find(self, tag):
        return [a for t, a in self.elements if t == tag]
    @property
    def ids(self):
        return [a["id"] for _, a in self.elements if "id" in a]

@lru_cache(None)
def page(repo, path):
    return Page(read(repo, path))

pages = []
shapes = []
for lang, pre in LOCALES.items():
    path = pre + "architecture-patterns.html"
    text, p = read(REPOS[0], path), page(REPOS[0], path)
    expected = ORIGIN + REPOS[0] + "/" + path
    check(p.find("html") == [{"lang": lang}], "document language " + lang)
    check(len(p.find("h1")) == len(p.find("main")) == 1, "one h1/main")
    check(p.find("main")[0].get("id") == "main" and p.find("main")[0].get("tabindex") == "-1", "focusable main")
    check(any(a.get("href") == "#main" and "skip" in a.get("class", "").split() for a in p.find("a")), "native skip link")
    check(len(p.ids) == len(set(p.ids)), "unique suite IDs")
    check(not any(p.find(tag) for tag in ["script", "form", "iframe", "object", "embed"]), "no active runtime or form")
    check(not any(k.lower().startswith("on") for _, attrs in p.elements for k in attrs), "no inline event handlers")
    check(not any(a.get("http-equiv", "").lower() == "refresh" for a in p.find("meta")), "no scripted/refresh navigation")
    check(any(a.get("name") == "description" and len(a.get("content", "")) > 100 for a in p.find("meta")), "localized description")
    check(any(a.get("charset", "").lower() == "utf-8" for a in p.find("meta")), "UTF-8")
    check(any(a.get("name") == "viewport" for a in p.find("meta")), "viewport")
    check(any("script-src 'none'" in a.get("content", "") and "connect-src 'none'" in a.get("content", "") for a in p.find("meta")), "no-network CSP")
    check([a.get("href") for a in p.find("link") if a.get("rel") == "canonical"] == [expected], "self canonical")
    alternates = [a for a in p.find("link") if a.get("rel") == "alternate"]
    check(len(alternates) == 4, "exactly four alternates")
    for l, prefix in dict(LOCALES, **{"x-default": ""}).items():
        check(any(a.get("hreflang") == l and a.get("href") == ORIGIN + REPOS[0] + "/" + prefix + "architecture-patterns.html" for a in alternates), "reciprocal alternate " + l)
    check(sum(a.get("aria-current") == "page" for a in p.find("a")) == 1, "one active language")
    for l, prefix in LOCALES.items():
        check(any(a.get("lang") == l and a.get("hreflang") == l and a.get("href") == ORIGIN + REPOS[0] + "/" + prefix + "architecture-patterns.html" for a in p.find("a")), "native language destination " + l)
    for id in IDS:
        check(p.ids.count(id) == 1 and any(a.get("href") == "#" + id for a in p.find("a")), "native section " + id)
    check(len(p.find("ol")) == 4, "four integration recipes")
    check(len(re.findall(r"<ol><li>.*?</ol>", text)) == 4, "four populated step lists")
    for ol in re.findall(r"<ol>(.*?)</ol>", text):
        check(ol.count("<li>") == 3, "three steps per recipe")
    for value in ["demo-op-001", "completion=unknown", "action=reconcile", "source=synthetic", "contains_payload=false", "https://app.example", "https://api.example", "Access-Control-Allow-Credentials: true", "Idempotency-Key", "Vary: Origin", "SameSite=None", "HttpOnly", "Secure"]:
        check(value in text, "localized machine example " + value)
    for repo in REPOS[1:]:
        check(any(a.get("href") == ORIGIN + repo + "/#batch-22-integration" for a in p.find("a")), "suite-to-app link")
    shape = [tag for tag, _ in p.elements]
    shapes.append(shape)
    home = read(REPOS[0], pre + "index.html")
    check(home.count('id="batch-22"') == 1, "one homepage feature")
    check(home.index('id="batch-22"') < home.index('id="diagnostics-matrix"') < home.index('id="apps"'), "feature above prior guides and filters")
    check(home.count("<article data-category=") == 3, "three utility cards retained")
    for old in ["diagnostics-matrix", "legal-compliance-care", "enterprise-case-studies", "architecture-roadmap"]:
        check(home.count('id="' + old + '"') == 1, "prior feature retained " + old)
    check('href="./architecture-patterns.html"' in home, "localized feature destination")
    for file in ["index.html", "architecture-patterns.html", "diagnostics-matrix.html", "case-studies.html", "changelog.html", "legal-compliance-care.html"]:
        pages.append((REPOS[0], pre + file))
check(shapes[0] == shapes[1] == shapes[2], "full translated structural parity")
for repo, anchor in zip(REPOS[1:], ["recipe-stream", "recipe-retry", "recipe-browser"]):
    for file in ["index.html", "README.md", "NETWORK.md"]:
        text = read(repo, file)
        marker = 'id="batch-22-integration"' if file.endswith(".html") else "## Batch 22 — Production architecture integration"
        check(text.count(marker) == 1, "exactly one satellite batch section")
        block = text[text.index(marker):]
        for lang, pre in LOCALES.items():
            check(ORIGIN + REPOS[0] + "/" + pre + "architecture-patterns.html#" + anchor in block, "three-language suite return")
        check(ORIGIN + REPOS[0] + "/" in block, "hub return")
        for sibling in REPOS[1:]:
            if sibling != repo:
                check(ORIGIN + sibling + "/#batch-22-integration" in block, "batch sibling return")
        for statement in ["manually reviewed", "never encode inputs in navigation URLs", "no automatic sanitizer", "English-only"]:
            check(statement in block, "satellite safety boundary")
    check(read(repo, "index.html").count("data-scenario=") == 3, "existing scenarios preserved")
    pages.append((repo, "index.html"))
for repo in REPOS:
    p = page(repo, "index.html")
    for other in REPOS:
        if other != repo:
            check(any(a.get("href") == ORIGIN + other + "/" for a in p.find("a")), "existing directed graph edge")
for repo, path in pages:
    p = page(repo, path)
    check(len(p.ids) == len(set(p.ids)), "unique IDs " + repo + "/" + path)
    base = ORIGIN + repo + "/" + path
    for a in p.find("a"):
        href = a.get("href", "")
        check(bool(href) and not href.lower().startswith(("javascript:", "data:")), "native nonempty anchor")
        u = urlparse(urljoin(base, href))
        if u.netloc != urlparse(ORIGIN).netloc:
            continue
        check(u.scheme == "https" and not u.query, "HTTPS and no navigation payload")
        bits = u.path.lstrip("/").split("/")
        target_repo = bits[0]
        check(target_repo in REPOS, "owned navigation destination")
        target = "/".join(bits[1:])
        if not target or u.path.endswith("/"):
            target += "index.html"
        check((NETWORK / target_repo / target).is_file(), "existing linked file")
        if u.fragment:
            check(unquote(u.fragment) in page(target_repo, target).ids, "existing linked fragment")
        links += 1
for file, expected in PINS.items():
    b = (NETWORK / file).read_bytes()
    actual = hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()
    check(actual == expected, "preserved file " + file)
result = {"batch": 22, "static_assertions": checks, "owned_link_fragment_checks": links, "canonical_html_pages": len(pages), "suite_locales": list(LOCALES), "patterns_per_locale": 3, "recipes_per_locale": 4, "steps_per_recipe": 3, "directed_network_edges": 12, "satellite_batch_sections": 9, "preserved_file_pins": len(PINS), "browser_qa": "skipped_not_claimed"}
parser = argparse.ArgumentParser()
parser.add_argument("--output")
args = parser.parse_args()
if args.output:
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
