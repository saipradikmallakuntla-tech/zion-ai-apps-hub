#!/usr/bin/env python3
"""Dependency-free source checks. Put all four owned checkouts side by side.
Run: python3 tests/diagnostics-matrix.test.py [--output results.json]
No network, browser, model calls, or engine self-test execution.
"""
import argparse, hashlib, html, json, re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from functools import lru_cache
from urllib.parse import urljoin, urlparse, unquote

ROOT=Path(__file__).resolve().parents[2]
HUB='zion-ai-apps-hub'
ORIGIN='https://saipradikmallakuntla-tech.github.io/'
LOCALES={'en':'','es':'es/','pt':'pt/'}
TOOLS=['llm-stream-inspector','agent-retry-safety-lab','cors-cookie-doctor']
MODES=['stream-terminal','stream-json','stream-timing','retry-loss','retry-key','retry-budget','cors-preflight','cookie-site','cookie-policy']
HANDOFFS=['triage-stream','triage-retry','triage-cors']
PINNED={'zion-ai-apps-hub/app.js': '7e12a12f6f4d4edbe457d9d160ccba26a6b78f51', 'zion-ai-apps-hub/styles.css': '8d8e544caeb4a20dad4ebefe160d1b136174504d', 'llm-stream-inspector/app.js': '5db9e188d24b0485c72795c05d151d5cd0716f3b', 'llm-stream-inspector/styles.css': '8121090b66979aef1b7179aa69e5cce48e7814e2', 'agent-retry-safety-lab/app.js': '97f50f921915b767624df314e567cc7d081f9863', 'agent-retry-safety-lab/styles.css': 'a88c31ca331ede8ba6e893acdf6a176be6e17569', 'cors-cookie-doctor/app.js': '242fd131dbfa0c37eaa81873e4820c9fce88b17d', 'cors-cookie-doctor/styles.css': '5ae532999334aa999140c29126aca11551b38d72', 'zion-ai-apps-hub/case-studies.html': '337e578203feda22094e8db8f9861199521cbdbc', 'zion-ai-apps-hub/changelog.html': 'b7a2da2a6ae679675f9aa93f747da7f346e38fc5', 'zion-ai-apps-hub/legal-compliance-care.html': '178a0e1140935cf13550f6a9cb81e3377725e96e', 'zion-ai-apps-hub/es/case-studies.html': 'ca80686844bc3403aa0d3da9d5be433fc3f2f924', 'zion-ai-apps-hub/es/changelog.html': '19338faa658979681d613a27537de9f347e07ae0', 'zion-ai-apps-hub/es/legal-compliance-care.html': 'e408d5b6e26a5d771268141f897535a9b66f2312', 'zion-ai-apps-hub/pt/case-studies.html': '13d5ab47533e20e4d24be4eee138d8f6eae3f40c', 'zion-ai-apps-hub/pt/changelog.html': '52e56aff2daa067781ed6ae7e6d3eab9d2a7deec', 'zion-ai-apps-hub/pt/legal-compliance-care.html': '4ebab21a6c778c354a6ab8d695f229e30537d6f8'}
checks=0
owned_links=0
class Doc(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True)
        self.tags=[]
        self.feed(text)
    def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
    def handle_startendtag(self,tag,attrs):self.handle_starttag(tag,attrs)
    def tag(self,name):return [a for t,a in self.tags if t==name]
    def ids(self):return [a['id'] for _,a in self.tags if 'id' in a]
def check(ok,label):
    global checks
    checks+=1
    assert ok,label
@lru_cache(maxsize=None)
def read(repo,p):return (ROOT/repo/p).read_text(encoding='utf-8')
@lru_cache(maxsize=None)
def parsed(repo,p):return Doc(read(repo,p))
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def text(s):return html.unescape(re.sub('<[^>]+>',' ',s)).strip()
pages=[]
for lang,pre in LOCALES.items():
    p=pre+'diagnostics-matrix.html';s=read(HUB,p);d=Doc(s)
    check(d.tag('html')[0].get('lang')==lang,'document language '+lang)
    canonical=[a['href'] for a in d.tag('link') if a.get('rel')=='canonical']
    check(canonical==[ORIGIN+HUB+'/'+p],'self canonical '+lang)
    alternates=[(a.get('hreflang'),a.get('href')) for a in d.tag('link') if a.get('rel')=='alternate']
    check(len(alternates)==4,'four alternates '+lang)
    for l,lp in {**LOCALES,'x-default':''}.items():check((l,ORIGIN+HUB+'/'+lp+'diagnostics-matrix.html') in alternates,'alternate '+l)
    check(len(d.tag('main'))==1 and len(d.tag('h1'))==1,'main/h1 '+lang)
    check(d.tag('main')[0].get('id')=='main' and d.tag('main')[0].get('tabindex')=='-1','focusable skip target')
    check(any(a.get('href')=='#main' for a in d.tag('a')),'native skip link')
    check(not d.tag('script') and not d.tag('form'),'no runtime scripts/forms')
    check(len(d.ids())==len(set(d.ids())),'unique guide IDs')
    for anchor in ['matrix','handoffs','evidence']:
        check(anchor in d.ids() and any(a.get('href')=='#'+anchor for a in d.tag('a')),'native section '+anchor)
    check(len(d.tag('table'))==1 and len(d.tag('caption'))==1,'table and caption')
    check(len(re.findall(r'<caption>\s*[^<]+</caption>',s))==1,'nonempty caption')
    check(sum(a.get('scope')=='col' for a in d.tag('th'))==5,'five column headers')
    check(sum(a.get('scope')=='row' for a in d.tag('th'))==9,'nine row headers')
    check(any(a.get('role')=='region' and a.get('tabindex')=='0' and a.get('aria-labelledby')=='matrix-heading' for a in d.tag('div')),'named keyboard-scroll region')
    rows=re.findall(r'<tr data-mode="([^"]+)">([\s\S]*?)</tr>',s)
    check([key for key,_ in rows]==MODES,'same nine failure identities '+lang)
    for key,row in rows:
        cells=re.findall(r'<(th|td)\b([^>]*)>([\s\S]*?)</\1>',row)
        check(len(cells)==5,'five cells '+key)
        check(cells[0][0]=='th' and 'scope="row"' in cells[0][1],'row scope '+key)
        for _,_,content in cells:check(bool(text(content)),'nonempty localized cell '+key)
    recipes=[a.get('data-handoff') for a in d.tag('article')]
    check(recipes==HANDOFFS,'same three handoff identities '+lang)
    for key in HANDOFFS:check(key in d.ids(),'stable handoff anchor '+key)
    for l,lp in LOCALES.items():check(any(a.get('href')==ORIGIN+HUB+'/'+lp+'diagnostics-matrix.html' and a.get('lang')==l and a.get('hreflang')==l for a in d.tag('a')),'native language '+l)
    check(sum(a.get('aria-current')=='page' for a in d.tag('a'))==1,'one current language')
    for a in d.tag('a'):
        u=urlparse(urljoin(ORIGIN+HUB+'/'+p,a['href']))
        check(u.scheme=='https' and (u.netloc==urlparse(ORIGIN).netloc or (u.netloc=='github.com' and u.path.startswith('/saipradikmallakuntla-tech/zion-ai-apps-hub/'))),'guide destinations are owned HTTPS resources')
        check(not u.query,'no diagnostic query inputs')
    if lang!='en':
        for phrase in ['Evidence to inspect','Carry manually','Start here']:
            check(phrase not in text(s),'no untranslated interface label '+phrase)
    home=read(HUB,pre+'index.html')
    check(home.count('id="diagnostics-matrix"')==1,'one promotion '+lang)
    check(home.index('id="diagnostics-matrix"')<home.index('<section id="apps"'),'promotion outside filters')
    check(home.count('<article data-category=')==3,'preserved three utility cards')
    for route in ['diagnostics-matrix.html','case-studies.html','changelog.html','legal-compliance-care.html']:check('./'+route in home,'preserved/promoted route '+route)
    for route in ['index.html','diagnostics-matrix.html','case-studies.html','changelog.html','legal-compliance-care.html']:pages.append((HUB,pre+route))
for i,repo in enumerate(TOOLS):
    s=read(repo,'index.html');d=Doc(s)
    check(sum(a.get('id')=='cross-app-triage' for _,a in d.tags)==1,'one satellite triage section')
    check(sum('data-handoff' in a for _,a in d.tags)==2,'two satellite handoff recipes')
    check(s.count('data-scenario=')==3,'preserved original scenarios')
    for p in ['index.html','README.md','NETWORK.md']:
        s=read(repo,p)
        for lang,pre in LOCALES.items():check(ORIGIN+HUB+'/'+pre+'diagnostics-matrix.html#'+HANDOFFS[i] in s,'matrix locale return '+repo+' '+p+' '+lang)
        check(ORIGIN+HUB+'/' in s,'hub return')
        for sibling in TOOLS:
            if sibling!=repo:check(ORIGIN+sibling+'/#diagnostic-notes' in s,'sibling handoff')
        check('Carry manually:' in s and 'Next action and limits:' in s,'explicit sanitized handoff fields')
        check('sanitization is not automatic' in s and 'English-only' in s,'honest privacy and locale boundaries')
    pages.append((repo,'index.html'))
for repo,p in pages:
    s=read(repo,p);d=Doc(s);check(len(d.ids())==len(set(d.ids())),'unique IDs '+repo+'/'+p)
    for a in d.tag('a'):
        u=urlparse(urljoin(ORIGIN+repo+'/'+p,a.get('href','')))
        if u.netloc!=urlparse(ORIGIN).netloc:continue
        parts=unquote(u.path).lstrip('/').split('/');target_repo=parts[0]
        check(target_repo in [HUB]+TOOLS,'owned link destination')
        check(u.scheme=='https' and not u.query,'HTTPS navigation with no inputs')
        target='/'.join(parts[1:])
        if not target or target.endswith('/'):target+='index.html'
        check((ROOT/target_repo/target).is_file(),'existing owned target '+target_repo+'/'+target)
        if u.fragment:check(unquote(u.fragment) in parsed(target_repo,target).ids(),'existing fragment '+u.fragment)
        owned_links+=1
for repo in [HUB]+TOOLS:
    s=read(repo,'index.html')
    for other in [HUB]+TOOLS:
        if other!=repo:check('href="'+ORIGIN+other+'/"' in s,'directed network edge')
for p,expected in PINNED.items():check(blob((ROOT/p).read_bytes())==expected,'preserved '+p)
result={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'static_assertions':checks,'owned_link_checks':owned_links,'canonical_html_pages_checked':len(pages),'matrix_rows_per_locale':9,'handoff_sections_per_locale':3,'satellite_handoff_recipes':6,'satellite_matrix_locale_links_html':9,'satellite_matrix_locale_links_all_files':27,'directed_network_edges':12,'preserved_runtime_assets':8,'preserved_prior_showcase_pages':9,'rendered_browser_qa':'skipped_not_claimed','engine_self_tests':'not_run_in_this_content_only_cycle'}
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
