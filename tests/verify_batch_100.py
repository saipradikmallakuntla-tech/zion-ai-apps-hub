#!/usr/bin/env python3
"""Batch 100 link contract. Standard library only; no app inputs or GitHub API calls."""
import argparse, concurrent.futures, datetime, hashlib, json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
OWNER = "saipradikmallakuntla-tech"
BASE = "https://" + OWNER + ".github.io/"
HUB = "zion-ai-apps-hub"
REPOS = [HUB, "llm-stream-inspector", "agent-retry-safety-lab", "cors-cookie-doctor", "prompt-token-budget-lab", "tool-schema-drift-auditor", "webhook-replay-guard"]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.ids = []; self.links = []; self.sections = {}; self.active = None; self.depth = 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.append(a["id"])
        if tag == "section":
            if self.active: self.depth += 1
            elif a.get("data-batch") == "100":
                self.active = a.get("id"); self.depth = 1; self.sections[self.active] = []
        if tag == "a" and "href" in a:
            self.links.append(a)
            if self.active: self.sections[self.active].append(a)
    def handle_endtag(self, tag):
        if tag == "section" and self.active:
            self.depth -= 1
            if not self.depth: self.active = None

def main():
    ap = argparse.ArgumentParser(); mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--directory", type=Path); mode.add_argument("--live", action="store_true")
    ap.add_argument("--output", type=Path); args = ap.parse_args()
    paths = [(r, "index.html") for r in REPOS] + [(HUB, "es/index.html"), (HUB, "pt/index.html"), (HUB, "homepage-promotion-batch-100.html")]
    def load(item):
        repo, path = item
        url = BASE + repo + "/" + ("" if path == "index.html" else path.replace("/index.html", "/"))
        if args.live:
            with urlopen(Request(url, headers={"User-Agent": "Zion-Batch-100-Link-Check", "Cache-Control": "no-cache"}), timeout=45) as response:
                data = response.read(); status = response.status; final = response.url
            assert status == 200 and final.startswith(BASE + repo + "/"), (url, status, final)
        else:
            data = (args.directory / repo / path).read_bytes(); status = None; final = url
        return item, data, {"url": url, "final_url": final, "http_status": status, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
    loaded = list(concurrent.futures.ThreadPoolExecutor(max_workers=7).map(load, paths))
    pages = {item: Page(data.decode("utf-8")) for item, data, receipt in loaded}
    checks = 0
    for repo in REPOS:
        page = pages[repo, "index.html"]
        assert len(page.ids) == len(set(page.ids)), (repo, "duplicate IDs")
        for other in REPOS:
            if other != repo:
                assert any(a["href"].startswith(BASE + other + "/") for a in page.links), (repo, other)
                checks += 1
        assert any(a["href"] == "https://ziontechgroup.com/" for a in page.links), repo
        section = "homepage-showcase" if repo == HUB else "next-tool-guidance"
        assert page.ids.count(section) == 1 and section in page.sections, (repo, section)
        for link in page.sections[section]:
            u = urlsplit(link["href"])
            assert not u.query and u.scheme != "javascript", link
            if u.hostname == OWNER + ".github.io":
                parts = u.path.strip("/").split("/")
                if len(parts) == 1 and u.fragment:
                    assert u.fragment in pages[parts[0], "index.html"].ids, link
            if link["href"].startswith("https://"):
                assert link.get("referrerpolicy") == "no-referrer", link
        if repo != HUB:
            contextual = [a for a in page.sections[section] if a["href"].endswith("/#next-tool-guidance")]
            assert len(contextual) == 3 and len({a["href"] for a in contextual}) == 3, repo
    for path in ["index.html", "es/index.html", "pt/index.html"]:
        page = pages[HUB, path]; links = page.sections["homepage-showcase"]
        for repo in REPOS[1:]:
            assert any(a["href"] == BASE + repo + "/" for a in links), (path, repo)
        assert any(a["href"].endswith("homepage-promotion-batch-100.html") for a in links), path
    fragment = pages[HUB, "homepage-promotion-batch-100.html"]
    for repo in REPOS[1:]:
        assert any(a["href"] == BASE + repo + "/" for a in fragment.links), repo
    receipt = {"batch": 100, "mode": "live" if args.live else "static", "verified_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "pages": [r for _, _, r in loaded], "directed_network_links": checks, "contextual_routes": 18, "new_section_anchors": 9, "homepage_backlinks": 7, "result": "passed", "scope": "HTML/link contracts; not a full browser or engine regression suite"}
    if args.output: args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
if __name__ == "__main__": main()
