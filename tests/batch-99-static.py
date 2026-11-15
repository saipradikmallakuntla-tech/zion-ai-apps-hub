"""Batch 99 bounded static source checks. Run with seven adjacent checkouts; no browsers."""
import json, hashlib, re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse, unquote
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
OWNER="saipradikmallakuntla-tech"
ORIGIN="https://"+OWNER+".github.io/"
REPOS=["zion-ai-apps-hub","llm-stream-inspector","agent-retry-safety-lab","cors-cookie-doctor","prompt-token-budget-lab","tool-schema-drift-auditor","webhook-replay-guard"]
PINS={'zion-ai-apps-hub/styles.css': '8d8e544caeb4a20dad4ebefe160d1b136174504d', 'zion-ai-apps-hub/legal-compliance-care.html': '178a0e1140935cf13550f6a9cb81e3377725e96e', 'zion-ai-apps-hub/diagnostics-matrix.html': 'aaa01e9a9b991ff926bc9eb5e0ebc22a6bb2210f', 'zion-ai-apps-hub/changelog.html': 'b7a2da2a6ae679675f9aa93f747da7f346e38fc5', 'zion-ai-apps-hub/case-studies.html': '337e578203feda22094e8db8f9861199521cbdbc', 'zion-ai-apps-hub/architecture-patterns.html': '5b23d5b61a98ba1578d31f6a00e25574d38cff8c', 'zion-ai-apps-hub/app.js': '7e12a12f6f4d4edbe457d9d160ccba26a6b78f51', 'zion-ai-apps-hub/.nojekyll': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391', 'zion-ai-apps-hub/pt/legal-compliance-care.html': '4ebab21a6c778c354a6ab8d695f229e30537d6f8', 'zion-ai-apps-hub/pt/diagnostics-matrix.html': '4db72cfd1113d0e8e98dc8cfeb55bf1e1b523cc3', 'zion-ai-apps-hub/pt/changelog.html': '52e56aff2daa067781ed6ae7e6d3eab9d2a7deec', 'zion-ai-apps-hub/pt/case-studies.html': '13d5ab47533e20e4d24be4eee138d8f6eae3f40c', 'zion-ai-apps-hub/pt/architecture-patterns.html': '397caa182f1614097e608606229a179c80d16782', 'zion-ai-apps-hub/es/legal-compliance-care.html': 'e408d5b6e26a5d771268141f897535a9b66f2312', 'zion-ai-apps-hub/es/diagnostics-matrix.html': 'ae0c3bc8fec499f67e2d7a832c585fa53c7f2052', 'zion-ai-apps-hub/es/changelog.html': '19338faa658979681d613a27537de9f347e07ae0', 'zion-ai-apps-hub/es/case-studies.html': 'ca80686844bc3403aa0d3da9d5be433fc3f2f924', 'zion-ai-apps-hub/es/architecture-patterns.html': '25f689ccaf2997c4513a78019d95b382870d3240', 'llm-stream-inspector/styles.css': '8121090b66979aef1b7179aa69e5cce48e7814e2', 'llm-stream-inspector/app.js': '5db9e188d24b0485c72795c05d151d5cd0716f3b', 'llm-stream-inspector/.nojekyll': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391', 'agent-retry-safety-lab/styles.css': 'a88c31ca331ede8ba6e893acdf6a176be6e17569', 'agent-retry-safety-lab/app.js': '97f50f921915b767624df314e567cc7d081f9863', 'agent-retry-safety-lab/.nojekyll': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391', 'cors-cookie-doctor/styles.css': '5ae532999334aa999140c29126aca11551b38d72', 'cors-cookie-doctor/app.js': '242fd131dbfa0c37eaa81873e4820c9fce88b17d', 'cors-cookie-doctor/.nojekyll': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391'}
checks=0
link_checks=0
def check(condition,label):
    global checks
    checks+=1
    if not condition: raise AssertionError(label)
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True)
        self.ids=[];self.tags=[];self.links=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);self.tags.append((tag,a))
        if "id" in a:self.ids.append(a["id"])
        for key in (["href"] if tag in ["a","link"] else ["src"] if tag in ["script","img"] else []):
            if a.get(key):self.links.append((tag,key,a[key]))
def blob(raw):return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
for path,sha in PINS.items():check(blob((WORK/path).read_bytes())==sha,"preserved original bytes "+path)
pages={}
for repo in REPOS:
    check((WORK/repo/".nojekyll").exists(),"nojekyll "+repo)
    for path in (WORK/repo).rglob("*.html"):
        rel=path.relative_to(WORK/repo).as_posix();text=path.read_text();parsed=Page(text);pages[(repo,rel)]=(text,parsed)
        check(len(parsed.ids)==len(set(parsed.ids)),"unique IDs "+str(path))
        check(sum(tag=="h1" for tag,a in parsed.tags)==1,"one h1 "+str(path))
        check(sum(tag=="main" for tag,a in parsed.tags)==1,"one main "+str(path))
        lang="es" if rel.startswith("es/") else "pt" if rel.startswith("pt/") else "en"
        check(any(tag=="html" and a.get("lang")==lang for tag,a in parsed.tags),"HTML language "+str(path))
        canonical=ORIGIN+repo+"/"+(rel[:-10] if rel.endswith("index.html") else rel)
        check(any(tag=="link" and a.get("rel")=="canonical" and a.get("href")==canonical for tag,a in parsed.tags),"canonical "+str(path))
        expected=4 if repo==REPOS[0] else 2
        check(sum(tag=="link" and a.get("rel")=="alternate" for tag,a in parsed.tags)==expected,"alternate count "+str(path))
        for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
            data=json.loads(raw);check(data.get("inLanguage")==lang,"structured language "+str(path))
        for tag,key,value in parsed.links:
            target=urlparse(urljoin(canonical,value))
            if target.netloc!=OWNER+".github.io":continue
            check(target.scheme=="https" and not target.query,"plain HTTPS owned link "+value)
            parts=target.path.strip("/").split("/");dest_repo=parts.pop(0)
            check(dest_repo in REPOS,"owned scope "+value)
            relpath="/".join(parts)
            if not relpath or target.path.endswith("/"):relpath+=("/" if relpath else "")+"index.html"
            dest=WORK/dest_repo/relpath;check(dest.is_file(),"local target "+str(dest));link_checks+=1
            if target.fragment and dest.suffix==".html":check(unquote(target.fragment) in Page(dest.read_text()).ids,"fragment "+value)
for repo in REPOS:
    text,parsed=pages[(repo,"index.html")]
    destinations={urlparse(value).path.strip("/").split("/")[0] for tag,key,value in parsed.links if tag=="a" and value.startswith(ORIGIN) and value.endswith("/")}
    check(set(REPOS)-{repo}<=destinations,"six directed root peers "+repo)
    for name in ["README.md","NETWORK.md"]:
        text=(WORK/repo/name).read_text()
        for other in set(REPOS)-{repo}:check(ORIGIN+other+"/" in text,"document peer "+repo+" "+name+" "+other)
for rel,lang in [("index.html","en"),("es/index.html","es"),("pt/index.html","pt")]:
    text,parsed=pages[(REPOS[0],rel)]
    check(text.count("<article data-category=")==6,"six cards "+lang)
    check(len(re.findall(r'<article data-category="ai"',text))==4,"four AI cards "+lang)
    check(len(re.findall(r'<article data-category="it"',text))==2,"two IT cards "+lang)
    data=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',text,re.S)[1])
    check(data["mainEntity"]["numberOfItems"]==6 and len(data["mainEntity"]["itemListElement"])==6,"six metadata items "+lang)
    check("batch-99-discovery.html" in text,"discovery promotion "+lang)
    count=re.search(r'data-template="([^"]+)"[^>]*>(.*?)</p>',text)
    check(count[2]==count[1].replace("{shown}","6").replace("{total}","6"),"localized six-card fallback "+lang)
for rel in ["batch-99-discovery.html","es/batch-99-discovery.html","pt/batch-99-discovery.html"]:
    text,parsed=pages[(REPOS[0],rel)]
    check(text.count('name="signal"')==6,"six questions "+rel)
    check(text.count('data-app-id=')==6,"six static catalog entries "+rel)
    check('id="mailto-summary" hidden' in text,"mail draft hidden without JS "+rel)
    check("connect-src 'none'" in text,"no runtime connections "+rel)
for repo in REPOS[4:]:
    text=(WORK/repo/"app.js").read_text()
    check(not re.search(r'\b(fetch|XMLHttpRequest|localStorage|sessionStorage|eval)\s*\(',text),"no network/storage/eval APIs "+repo)
    check('innerHTML' not in text,"safe text rendering "+repo)
check(len(pages)==27,"all 27 canonical HTML routes")
print(json.dumps({"staticAssertions":checks,"ownedLinksAndAssetsChecked":link_checks,"canonicalHtmlRoutes":len(pages),"directedRepositoryEdges":42,"pinnedOriginalFiles":len(PINS),"browserWorkers":0}))
