"""Optional release QA: pip install playwright; playwright install chromium.
Serve four adjacent checkouts for local QA; pass the github.io origin for deployed QA.
No credentials, third-party writes, or certificate-verification bypasses are used.
"""
import argparse, datetime, hashlib, json, pathlib, sys
from urllib.parse import urljoin, urlsplit
from playwright.sync_api import sync_playwright

p=argparse.ArgumentParser()
p.add_argument('--base-url',default='https://saipradikmallakuntla-tech.github.io/')
p.add_argument('--site-root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[2])
p.add_argument('--output',type=pathlib.Path,default=pathlib.Path('legal-browser-results.json'))
a=p.parse_args()
base=a.base_url.rstrip('/')+'/'
hub='zion-ai-apps-hub/'
locales={'en':'','es':'es/','pt':'pt/'}
show='legal-compliance-care.html'
satellites={'llm-stream-inspector':9,'agent-retry-safety-lab':10,'cors-cookie-doctor':14}
routes=[hub+pre+f for pre in locales.values() for f in ['',show]]+[r+'/' for r in satellites]
widths=[320,390,768,900,1440]
report={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_url':base,'pages':[],'assets':[],'errors':[],'unexpected_requests':[],'page_errors':[],'no_js_language_switches':0,'no_js_satellite_returns':0}

def need(condition,message):
    if not condition: raise AssertionError(message)

with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,args=['--no-sandbox'])
    report['browser']=browser.version
    context=browser.new_context(viewport={'width':1440,'height':1000},ignore_https_errors=False)
    nojs=browser.new_context(java_script_enabled=False,viewport={'width':1440,'height':1000},ignore_https_errors=False)
    for c in [context,nojs]:
        c.on('request',lambda r: report['unexpected_requests'].append({'url':r.url,'type':r.resource_type}) if r.resource_type in ['fetch','xhr','websocket','eventsource'] or urlsplit(r.url).netloc!=urlsplit(base).netloc else None)
        c.on('page',lambda page: page.on('pageerror',lambda error:report['page_errors'].append(str(error))))
    for route in routes:
        row={'route':route,'url':urljoin(base,route)}
        report['pages'].append(row)
        page=context.new_page()
        try:
            response=page.goto(row['url'],wait_until='networkidle')
            row['http_status']=response.status
            need(response.status==200,'HTTP 200')
            expected_path=route+'index.html' if route.endswith('/') else route
            body=response.body();row['sha256']=hashlib.sha256(body).hexdigest()
            need(body==(a.site_root/expected_path).read_bytes(),'deployed HTML differs from expected source')
            row['source_bytes_match']=True
            row['metadata']=page.evaluate('''() => ({lang:document.documentElement.lang,canonical:document.querySelector('link[rel="canonical"]').href,alternates:Object.fromEntries([...document.querySelectorAll('link[rel="alternate"]')].map(a=>[a.hreflang,a.href])),structured:JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)})''')
            is_hub=route.startswith(hub)
            locale=next((l for l,pre in locales.items() if pre and route.startswith(hub+pre)),'en')
            need(row['metadata']['lang']==locale,'HTML language')
            need(row['metadata']['canonical']==urljoin('https://saipradikmallakuntla-tech.github.io/',route),'canonical')
            suffix=show if route.endswith(show) else ''
            alts={l:urljoin('https://saipradikmallakuntla-tech.github.io/',hub+pre+suffix) for l,pre in locales.items()} if is_hub else {'en':urljoin('https://saipradikmallakuntla-tech.github.io/',route)}
            alts['x-default']=alts['en']
            need(row['metadata']['alternates']==alts,'hreflang/x-default')
            need(row['metadata']['structured']['inLanguage']==locale,'structured language')
            await_skip=page.locator('a.skip')
            page.keyboard.press('Tab')
            need(await_skip.evaluate('(e)=>e===document.activeElement'),'first Tab reaches skip link')
            need(await_skip.is_visible(),'skip link visible on focus')
            page.keyboard.press('Enter')
            need(page.locator('#main').evaluate('(e)=>e===document.activeElement'),'skip link focuses main')
            page.goto(row['url'],wait_until='domcontentloaded')
            count=page.locator('header a').count();seen=set()
            for i in range(count+6):
                page.keyboard.press('Tab')
                focus=page.evaluate('''() => {let e=document.activeElement,all=[...document.querySelectorAll('header a')],s=getComputedStyle(e);return {index:all.indexOf(e),outline:s.outlineStyle,width:parseFloat(s.outlineWidth)}}''')
                if focus['index']>=0:
                    seen.add(focus['index']);need(focus['outline']!='none' and focus['width']>=2,'visible keyboard focus')
                if len(seen)==count:break
            need(len(seen)==count,'keyboard reaches every header link')
            row['keyboard_header_links']=count
            row['viewport_checks']=[]
            for width in widths:
                page.set_viewport_size({'width':width,'height':1000})
                need(page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),'horizontal overflow '+str(width))
                row['viewport_checks'].append(width)
            if is_hub and not suffix:
                need(page.locator('#app-cards article:visible').count()==3,'three live utilities')
                page.locator('#query').fill('zzzz_missing')
                need(page.locator('#app-cards article:visible').count()==0 and page.locator('#no-results').is_visible(),'empty state')
                page.locator('button[type="reset"]').click()
                page.locator('#query').fill('repetição')
                need(page.locator('#app-cards article:visible').count()==1,'accent-insensitive search')
                page.locator('button[type="reset"]').click()
                need(page.locator('#app-cards article:visible').count()==3,'reset')
                row['filter_regression']='passed'
            if not is_hub:
                repo=route.rstrip('/')
                page.locator('#run-tests').click()
                passed=page.locator('#test-results .pass').count()
                total=page.locator('#test-results li').count()
                need(passed==total==satellites[repo],'satellite UI regression')
                row['engine_tests']={'passed':passed,'total':total}
            row['passed']=True
        except Exception as error:report['errors'].append({'route':route,'error':str(error)})
        finally:page.close()
    for route in routes:
        page=nojs.new_page()
        try:
            url=urljoin(base,route);page.goto(url,wait_until='domcontentloaded')
            is_hub=route.startswith(hub);suffix=show if route.endswith(show) else ''
            if is_hub and suffix:need(page.locator('[data-practice]').count()==9,'no-JS content')
            if is_hub and not suffix:
                need(page.locator('#tool-filter').is_hidden(),'inactive filters hidden without JS')
                need(page.locator('#app-cards article:visible').count()==3,'no-JS cards')
            for width in widths:
                page.set_viewport_size({'width':width,'height':1000})
                need(page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),'no-JS overflow')
            if is_hub:
                for locale,pre in locales.items():
                    page.goto(url,wait_until='domcontentloaded')
                    page.locator('nav.languages a[hreflang="'+locale+'"]').click()
                    page.wait_for_load_state('domcontentloaded')
                    need(page.url==urljoin(base,hub+pre+suffix),'native language destination')
                    need(page.locator('html').get_attribute('lang')==locale,'native language content')
                    report['no_js_language_switches']+=1
            elif base.startswith('https:'):
                page.locator('header a[href$="/'+show+'"]').click()
                page.wait_for_load_state('domcontentloaded')
                need(page.url==urljoin(base,hub+show),'native satellite return')
                need(page.locator('[data-practice]').count()==9,'satellite return content')
                report['no_js_satellite_returns']+=1
            next(r for r in report['pages'] if r['route']==route)['no_js_passed']=True
        except Exception as error:report['errors'].append({'route':route,'no_js_error':str(error)})
        finally:page.close()
    for repo in ['zion-ai-apps-hub',*satellites]:
        for file in ['styles.css','app.js']:
            route=repo+'/'+file
            response=context.request.get(urljoin(base,route))
            body=response.body();match=body==(a.site_root/route).read_bytes()
            report['assets'].append({'route':route,'status':response.status,'source_bytes_match':match,'sha256':hashlib.sha256(body).hexdigest()})
            if response.status!=200 or not match:report['errors'].append({'asset':route,'error':'asset HTTP/byte mismatch'})
    browser.close()
report['passed']=not(report['errors'] or report['unexpected_requests'] or report['page_errors'])
a.output.parent.mkdir(parents=True,exist_ok=True)
a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'passed':report['passed'],'pages':len(report['pages']),'assets':len(report['assets']),'viewport_checks':sum(len(r.get('viewport_checks',[])) for r in report['pages'])*2,'no_js_language_switches':report['no_js_language_switches'],'no_js_satellite_returns':report['no_js_satellite_returns'],'errors':report['errors'],'unexpected_requests':report['unexpected_requests'],'page_errors':report['page_errors']},ensure_ascii=False))
sys.exit(0 if report['passed'] else 1)
