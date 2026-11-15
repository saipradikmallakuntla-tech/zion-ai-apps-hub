/* Dependency-free suite/graph checks and reproducible synthetic reference results.
   Place the three satellite checkouts beside the hub. No network calls. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),network=path.dirname(root),origin='https://saipradikmallakuntla-tech.github.io/',hub=origin+'zion-ai-apps-hub/';
const locales={en:'',es:'es/',pt:'pt/'},tools=['llm-stream-inspector','agent-retry-safety-lab','cors-cookie-doctor'],ids=['sse','retry','cors'];
let checks=0;const check=(ok,label)=>{checks++;assert.ok(ok,label);};
const read=(repo,file)=>fs.readFileSync(path.join(network,repo,file),'utf8');
for(const [lang,pre] of Object.entries(locales)){
 const html=read('zion-ai-apps-hub',pre+'case-studies.html'),home=read('zion-ai-apps-hub',pre+'index.html');
 check(html.includes('<html lang="'+lang+'">'),'document language');
 check(html.includes('<link rel="canonical" href="'+hub+pre+'case-studies.html">'),'canonical');
 check((html.match(/rel="alternate"/g)||[]).length===4,'four alternates');
 for(const [l,p] of Object.entries({...locales,'x-default':''}))check(html.includes('<link rel="alternate" hreflang="'+l+'" href="'+hub+p+'case-studies.html">'),'alternate '+l);
 check((html.match(/aria-current="page"/g)||[]).length===1,'one current locale');
 for(const [l,p] of Object.entries(locales)){
  const relative=(lang==='en'?'./':'../')+p+'case-studies.html';
  check(html.includes('href="'+relative+'" lang="'+l+'" hreflang="'+l+'"'),'native locale '+l);
 }
 const schema=JSON.parse(html.match(/<script type="application\/ld\+json">([^]*?)<\/script>/)[1]);
 check(schema.inLanguage===lang&&schema.url===hub+pre+'case-studies.html','localized structured metadata');
 check(schema.mainEntity.numberOfItems===3&&schema.mainEntity.itemListElement.length===3,'three cases, not products');
 check(JSON.stringify([...html.matchAll(/data-case="([^"]+)"/g)].map(m=>m[1]))===JSON.stringify(ids),'localized case parity');
 const fragments=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 check(fragments.length===new Set(fragments).size,'unique ids');
 for(const m of html.matchAll(/href="#([^"]+)"/g))check(fragments.includes(m[1]),'fragment '+m[1]);
 check(/<main id="main" class="wrap" tabindex="-1">/.test(html)&&html.includes('<a class="skip" href="#main">'),'keyboard skip target');
 check((html.match(/<h1[ >]/g)||[]).length===1,'single h1');
 check(!/<script(?! type="application\/ld\+json")|<form|\bonclick=|\bfetch\(|localStorage|sessionStorage/i.test(html),'static privacy boundary');
 check(html.includes('href="'+(lang==='en'?'./':'../')+'styles.css"'),'local design tokens');
 check(home.includes('href="./case-studies.html"'),'homepage promotion');
 check(home.indexOf('id="enterprise-case-studies"')<home.indexOf('id="apps"'),'promotion outside filters');
 check(home.includes('id="legal-compliance-care"')&&(home.match(/<article data-category=/g)||[]).length===3,'prior showcase and three utility cards retained');
 for(const tool of tools){check(html.includes('href="'+origin+tool+'/" hreflang="en"'),'direct utility');check(html.includes('href="https://github.com/saipradikmallakuntla-tech/'+tool+'"'),'owned utility source');}
 check(html.includes('125 ms')&&html.includes('400 ms')&&html.includes('INVALID_JSON'),'benchmark parity');
 check(html.includes('SameSite=None')&&html.includes('CORS'),'cookie benchmark parity');
}
const immutable={"zion-ai-apps-hub":{"app.js":"7e12a12f6f4d4edbe457d9d160ccba26a6b78f51","styles.css":"8d8e544caeb4a20dad4ebefe160d1b136174504d"},"llm-stream-inspector":{"app.js":"5db9e188d24b0485c72795c05d151d5cd0716f3b","styles.css":"8121090b66979aef1b7179aa69e5cce48e7814e2"},"agent-retry-safety-lab":{"app.js":"97f50f921915b767624df314e567cc7d081f9863","styles.css":"a88c31ca331ede8ba6e893acdf6a176be6e17569"},"cors-cookie-doctor":{"app.js":"242fd131dbfa0c37eaa81873e4820c9fce88b17d","styles.css":"5ae532999334aa999140c29126aca11551b38d72"}};
for(const [repo,files] of Object.entries(immutable))for(const [file,sha] of Object.entries(files)){
 const b=fs.readFileSync(path.join(network,repo,file));check(crypto.createHash('sha1').update(Buffer.concat([Buffer.from('blob '+b.length+'\0'),b])).digest('hex')===sha,'unchanged '+repo+'/'+file);
}
for(const [i,tool] of tools.entries()){
 const html=read(tool,'index.html');
 for(const other of ['zion-ai-apps-hub',...tools].filter(r=>r!==tool))check(html.includes('href="'+origin+other+'/"'),'network edge '+tool+' -> '+other);
 check(html.includes(hub+'legal-compliance-care.html'),'prior showcase return retained');
 for(const file of ['index.html','README.md','NETWORK.md'])for(const pre of Object.values(locales))check(read(tool,file).includes(hub+pre+'case-studies.html#'+ids[i]),'reciprocal '+tool+'/'+file+'/'+pre);
}
const engines=tools.map((repo,i)=>{const api=require(path.join(network,repo,'app.js')),tests=api.selfTest();check(tests.length===[9,10,14][i],'engine count');for(const t of tests)check(t.pass,repo+': '+t.name);return {repo,passed:tests.filter(t=>t.pass).length,total:tests.length,tests};});
const stream=require(path.join(network,tools[0],'app.js')),retry=require(path.join(network,tools[1],'app.js')),cors=require(path.join(network,tools[2],'app.js'));
const oa=stream.analyzeCapture(stream.samples.openai),timed=stream.analyzeCapture(stream.samples.timed);
const sse={city:oa.tools[0].parsed.city,complete:oa.complete,plain_sse_first_text_ms:oa.firstTextMs,truncated_complete:stream.analyzeCapture(stream.samples.truncated).complete,malformed_json_detected:stream.analyzeCapture(stream.samples.malformed).findings.some(f=>f.code==='INVALID_JSON'),timestamped_first_text_ms:timed.firstTextMs,timestamped_duration_ms:timed.durationMs};
check(JSON.stringify(sse)===JSON.stringify({city:'Lisbon',complete:true,plain_sse_first_text_ms:null,truncated_complete:false,malformed_json_detected:true,timestamped_first_text_ms:125,timestamped_duration_ms:400}),'SSE reference outcomes');
const config={...retry.defaults,agentRetries:1,sdkRetries:1,httpRetries:1,clients:1,timeoutMs:100,serviceMs:20,outageMs:1000000,baseDelayMs:0,capDelayMs:0,keyMode:'none'};
const compact=r=>({attempts:r.attempts,side_effects:r.sideEffects,duplicates:r.duplicateSideEffects,deduplicated:r.deduplicated});
const retries={configuration:config,no_key:compact(retry.simulate(config)),stable_retained:compact(retry.simulate({...config,keyMode:'stable',ttlMs:10000})),stable_expired:compact(retry.simulate({...config,keyMode:'stable',ttlMs:100})),rotating:compact(retry.simulate({...config,keyMode:'per-attempt'}))};
check(retries.no_key.attempts===8&&retries.no_key.side_effects===8&&retries.no_key.duplicates===7,'unprotected reference');
check(retries.stable_retained.attempts===8&&retries.stable_retained.side_effects===1&&retries.stable_retained.deduplicated===7,'stable-key reference');
check(retries.stable_expired.duplicates>0&&retries.rotating.duplicates===7,'expiry/rotation reference');
const cr=k=>cors.analyze(cors.samples[k]);
const cookies={credentialed_wildcard_blocked:cr('broken').corsBlocked,explicit_origin_blocked:cr('fixed').corsBlocked,explicit_origin_preflight:cr('fixed').preflightNeeded,explicit_origin_cookie:cr('fixed').cookies[0].eligible,cross_site_lax_cors_blocked:cr('crossLax').corsBlocked,cross_site_lax_cookie:cr('crossLax').cookies[0].eligible,secure_none_cookie:cr('crossNone').cookies[0].eligible,third_party_blocked_cookie:cr('blockedThirdParty').cookies[0].eligible};
check(JSON.stringify(cookies)===JSON.stringify({credentialed_wildcard_blocked:true,explicit_origin_blocked:false,explicit_origin_preflight:true,explicit_origin_cookie:true,cross_site_lax_cors_blocked:false,cross_site_lax_cookie:false,secure_none_cookie:true,third_party_blocked_cookie:false}),'CORS/cookie references');
const report={checked_at_utc:new Date().toISOString(),node:process.version,passed:true,static_assertions:checks,engine_tests_passed:engines.reduce((n,e)=>n+e.passed,0),engine_tests_total:33,engines,benchmarks:{sse,retries,cookies},immutable_runtime_git_blobs:immutable};
const out=process.argv.find(a=>a.startsWith('--output='));if(out)fs.writeFileSync(out.slice(9),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:true,assertions:checks,engine_tests:report.engine_tests_passed+'/33',benchmarks:report.benchmarks},null,2));
