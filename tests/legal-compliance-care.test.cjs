/* Dependency-free static release checks. Put satellite checkouts beside the hub for graph checks. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),network=path.dirname(root);
const origin='https://saipradikmallakuntla-tech.github.io/',hub=origin+'zion-ai-apps-hub/';
const file='legal-compliance-care.html',locales=['en','es','pt'];
const prefix=l=>l==='en'?'':l+'/';
const tools=['llm-stream-inspector','agent-retry-safety-lab','cors-cookie-doctor'];
const practices=['ai-governance','vendor-contracts','ip-attribution','pii-consent','cors-cookies','retry-rate-limit','stream-reliability','human-escalation','incident-readiness'];
let checks=0;const check=(condition,label)=>{checks++;assert.ok(condition,label);};
function metadata(html,locale,url,alternates){
 check(html.includes('<html lang="'+locale+'">'),'document language');
 check(/<title>[^<]+<\/title>/.test(html),'title');
 check(/<meta name="description" content="[^"]+">/.test(html),'description');
 check(html.includes('<link rel="canonical" href="'+url+'">'),'canonical');
 const links=[...html.matchAll(/<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">/g)];
 check(links.length===Object.keys(alternates).length,'alternate count');
 for(const [lang,destination] of Object.entries(alternates))check(links.some(m=>m[1]===lang&&m[2]===destination),'alternate '+lang);
 const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 check(ids.length===new Set(ids).size,'unique ids');
 for(const m of html.matchAll(/href="#([^"]+)"/g))check(ids.includes(m[1]),'fragment '+m[1]);
 check((html.match(/<h1[ >]/g)||[]).length===1,'single h1');
 check(/<main(?=[^>]*\bid="main")(?=[^>]*\btabindex="-1")[^>]*>/.test(html),'focusable main landmark');
 check(/<a class="skip" href="#main">/.test(html),'native skip link');
 check(!/href="(?:javascript:|#")/i.test(html),'native navigation');
}
for(const locale of locales){
 const p=prefix(locale),home=fs.readFileSync(path.join(root,p+'index.html'),'utf8');
 const html=fs.readFileSync(path.join(root,p+file),'utf8');
 for(const [text,showcase] of [[home,false],[html,true]]){
  const suffix=showcase?file:'',alts=Object.fromEntries(locales.map(l=>[l,hub+prefix(l)+suffix]));alts['x-default']=hub+suffix;
  metadata(text,locale,hub+p+suffix,alts);
  check((text.match(/aria-current="page"/g)||[]).length===1,'one current language');
  const schema=JSON.parse(text.match(/<script type="application\/ld\+json">([^]*?)<\/script>/)[1]);
  check(schema.inLanguage===locale,'structured language');check(schema.url===hub+p+suffix,'structured URL');
  check(schema.mainEntity.numberOfItems===3&&schema.mainEntity.itemListElement.length===3,'three tools or pillars, not additional apps');
 }
 const keys=[...html.matchAll(/data-practice="([^"]+)"/g)].map(m=>m[1]);
 check(JSON.stringify(keys)===JSON.stringify(practices),'all nine localized practices');
 for(const id of ['legal','compliance','care','evidence'])check(html.includes('id="'+id+'"'),'section '+id);
 check(!/<script(?! type="application\/ld\+json")/i.test(html),'no showcase runtime JS');
 check(!/<form|\bonclick=|\blocalStorage\b|\bsessionStorage\b|\bfetch\(/i.test(html),'no collection or runtime APIs');
 check(home.indexOf('id="legal-compliance-care"')<home.indexOf('id="apps"'),'promotion outside filters');
 check((home.match(/<article data-category=/g)||[]).length===3,'preserved utility count');
 for(const slug of tools){check(html.includes('href="'+origin+slug+'/" hreflang="en"'),'live tool '+slug);check(html.includes('href="https://github.com/saipradikmallakuntla-tech/'+slug+'"'),'tool source '+slug);}
 console.log('PASS '+locale+' showcase, homepage, metadata, nine practices, static navigation and privacy boundaries');
}
for(const slug of tools){
 const f=path.join(network,slug,'index.html');if(!fs.existsSync(f)){console.log('SKIP adjacent checkout '+slug);continue;}
 const html=fs.readFileSync(f,'utf8');metadata(html,'en',origin+slug+'/',{en:origin+slug+'/','x-default':origin+slug+'/'});
 for(const other of ['zion-ai-apps-hub',...tools].filter(x=>x!==slug))check(html.includes('href="'+origin+other+'/"'),'preserved network edge');
 check(html.includes('href="'+hub+file+'" hreflang="en"'),'showcase backlink');
 console.log('PASS '+slug+' metadata and reciprocal navigation');
}
console.log('PASS '+checks+' static assertions');
