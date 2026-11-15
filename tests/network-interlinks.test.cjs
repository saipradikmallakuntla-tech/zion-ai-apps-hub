/* Bounded, dependency-free source checks. Place the four owned checkouts side by side.
   node tests/network-interlinks.test.cjs [--engines]
   Optional pure-engine self-tests have a 10-second timeout per process. No browser or network. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict'),cp=require('node:child_process');
const root=path.resolve(__dirname,'..'),network=path.dirname(root),origin='https://saipradikmallakuntla-tech.github.io/',repo='zion-ai-apps-hub',hub=origin+repo+'/';
const tools=['llm-stream-inspector','agent-retry-safety-lab','cors-cookie-doctor'],locales={en:'',es:'es/',pt:'pt/'};
const read=(r,p)=>fs.readFileSync(path.join(network,r,p),'utf8');
let checks=0,ownedLinks=0;const check=(ok,label)=>{checks++;assert.ok(ok,label);};
const candidates=['structured-output-portability-checker','citation-span-verifier','conversation-portability-inspector','webhook-signature-fixture-lab','csp-policy-explainer','cron-dst-previewer'];
const pages=[];
for(const [lang,pre] of Object.entries(locales)){
 const html=read(repo,pre+'changelog.html'),home=read(repo,pre+'index.html');
 check(html.includes('<html lang="'+lang+'">'),'document language');
 check(html.includes('<link rel="canonical" href="'+hub+pre+'changelog.html">'),'self canonical');
 check((html.match(/<link rel="alternate"/g)||[]).length===4,'exactly four alternates');
 for(const [l,p] of Object.entries({...locales,'x-default':''}))check(html.includes('<link rel="alternate" hreflang="'+l+'" href="'+hub+p+'changelog.html">'),'alternate '+l);
 check((html.match(/<main\b/g)||[]).length===1 && (html.match(/<h1>/g)||[]).length===1,'single main and h1');
 check(html.includes('href="#main"') && /<main[^>]*id="main"[^>]*tabindex="-1"/.test(html),'focusable skip target');
 for(const id of ['architecture','changelog','roadmap','release'])check(html.includes('id="'+id+'"') && html.includes('href="#'+id+'"'),'native section navigation');
 const ids=Array.from(html.matchAll(/\bid="([^"]+)"/g),m=>m[1]);check(new Set(ids).size===ids.length,'unique IDs');
 check(!/<script\b/i.test(html.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/g,'')),'no runtime JavaScript');
 const schema=JSON.parse(html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
 check(schema.inLanguage===lang && schema.url===hub+pre+'changelog.html','localized JSON-LD');
 check(JSON.stringify(Array.from(html.matchAll(/data-candidate="([^"]+)"/g),m=>m[1]))===JSON.stringify(candidates),'six reconciled candidate identities');
 check((html.match(/data-change=/g)||[]).length===4,'four dated changes');
 check((html.match(/data-node=/g)||[]).length===4,'four architecture nodes');
 check((html.match(/aria-current="page"/g)||[]).length===1,'one current language');
 check((home.match(/<article data-category=/g)||[]).length===3,'three utility cards');
 check(home.indexOf('id="architecture-roadmap"')>=0 && home.indexOf('id="architecture-roadmap"')<home.indexOf('<section id="apps"'),'promotion outside filters');
 check(home.includes('./case-studies.html') && home.includes('./legal-compliance-care.html'),'existing showcases');
 for(const p of ['index.html','changelog.html','case-studies.html','legal-compliance-care.html'])pages.push([repo,pre+p]);
}
for(const r of tools){
 const html=read(r,'index.html');check((html.match(/data-scenario=/g)||[]).length===3,'three practical scenarios');
 for(const file of ['index.html','README.md','NETWORK.md']){
  const text=read(r,file);
  for(const pre of Object.values(locales))check(text.includes(hub+pre+'changelog.html#architecture'),'localized changelog return');
  for(const sibling of tools.filter(x=>x!==r))check(text.includes(origin+sibling+'/#diagnostic-notes'),'contextual sibling link');
  check(text.includes('Setup:')||text.includes('**Setup:**'),'setup notes');
  check(text.includes('Expected finding:'),'expected findings');check(text.includes('Interpretation and limits:'),'limitations');
 }
 pages.push([r,'index.html']);
}
for(const r of [repo,...tools])for(const other of [repo,...tools].filter(x=>x!==r))check(read(r,'index.html').includes('href="'+origin+other+'/"'),'directed graph edge');
for(const [r,p] of pages){
 const html=read(r,p),base=origin+r+'/'+p;
 for(const m of html.matchAll(/<a\b[^>]*\bhref="([^"]+)"/g)){
  const u=new URL(m[1].replaceAll('&amp;','&'),base);if(u.origin!==new URL(origin).origin)continue;
  const bits=u.pathname.slice(1).split('/'),targetRepo=bits.shift();check([repo,...tools].includes(targetRepo),'owned destination');
  let target=bits.join('/');if(!target||target.endsWith('/'))target+='index.html';
  check(!u.search,'no navigation inputs');const dest=read(targetRepo,target);ownedLinks++;
  if(u.hash)check(dest.includes('id="'+decodeURIComponent(u.hash.slice(1))+'"'),'existing native fragment');
 }
}
const pinned={
 'zion-ai-apps-hub/app.js':'7e12a12f6f4d4edbe457d9d160ccba26a6b78f51','zion-ai-apps-hub/styles.css':'8d8e544caeb4a20dad4ebefe160d1b136174504d',
 'llm-stream-inspector/app.js':'5db9e188d24b0485c72795c05d151d5cd0716f3b','llm-stream-inspector/styles.css':'8121090b66979aef1b7179aa69e5cce48e7814e2',
 'agent-retry-safety-lab/app.js':'97f50f921915b767624df314e567cc7d081f9863','agent-retry-safety-lab/styles.css':'a88c31ca331ede8ba6e893acdf6a176be6e17569',
 'cors-cookie-doctor/app.js':'242fd131dbfa0c37eaa81873e4820c9fce88b17d','cors-cookie-doctor/styles.css':'5ae532999334aa999140c29126aca11551b38d72',
 'zion-ai-apps-hub/case-studies.html':'337e578203feda22094e8db8f9861199521cbdbc','zion-ai-apps-hub/es/case-studies.html':'ca80686844bc3403aa0d3da9d5be433fc3f2f924','zion-ai-apps-hub/pt/case-studies.html':'13d5ab47533e20e4d24be4eee138d8f6eae3f40c',
 'zion-ai-apps-hub/legal-compliance-care.html':'178a0e1140935cf13550f6a9cb81e3377725e96e','zion-ai-apps-hub/es/legal-compliance-care.html':'e408d5b6e26a5d771268141f897535a9b66f2312','zion-ai-apps-hub/pt/legal-compliance-care.html':'4ebab21a6c778c354a6ab8d695f229e30537d6f8'};
for(const [file,expected] of Object.entries(pinned)){
 const b=fs.readFileSync(path.join(network,file)),h=crypto.createHash('sha1').update(Buffer.from('blob '+b.length+'\0')).update(b).digest('hex');check(h===expected,'preserved '+file);
}
const engines=[];
if(process.argv.includes('--engines'))for(const r of tools){
 const file=path.join(network,r,'app.js'),code='const t=require('+JSON.stringify(file)+').selfTest();console.log(JSON.stringify({total:t.length,passed:t.filter(x=>x.pass).length}));if(t.some(x=>!x.pass))process.exit(1)';
 try{const text=cp.execFileSync(process.execPath,['-e',code],{timeout:10000,encoding:'utf8'});engines.push({repo:r,status:'passed',...JSON.parse(text)});}
 catch(e){engines.push({repo:r,status:e.code==='ETIMEDOUT'?'timeout_not_passed':'failed',error:String(e.message).slice(0,300)});process.exitCode=1;}
}
console.log(JSON.stringify({static_assertions:checks,owned_link_checks:ownedLinks,directed_network_edges:12,node:process.version,engines,rendered_browser_qa:'skipped_not_claimed'},null,2));
