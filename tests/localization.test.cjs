/* Dependency-free static and progressive-enhancement regression checks. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const slugs=['llm-stream-inspector','agent-retry-safety-lab','cors-cookie-doctor','prompt-token-budget-lab','tool-schema-drift-auditor','webhook-replay-guard'];
for(const [locale,file] of [['en','index.html'],['es','es/index.html'],['pt','pt/index.html']]){
 const html=fs.readFileSync(path.join(root,file),'utf8');
 assert.ok(html.includes('<html lang="'+locale+'">'));
 assert.equal((html.match(/rel="alternate"/g)||[]).length,4);
 assert.equal((html.match(/aria-current="page"/g)||[]).length,1);
 assert.ok(/<form[^>]+id="tool-filter"[^>]+hidden>/.test(html));
 for(const slug of slugs)assert.ok(html.includes('https://saipradikmallakuntla-tech.github.io/'+slug+'/'));
 const schema=JSON.parse(html.match(/<script type="application\/ld\+json">([^]*?)<\/script>/)[1]);
 assert.equal(schema.inLanguage,locale);assert.equal(schema.mainEntity.itemListElement.length,6);
 const handlers={};
 function element(id,value=''){return {value,hidden:false,dataset:{},textContent:'',addEventListener:(type,fn)=>{handlers[id+':'+type]=fn;}};}
 const nodes={ 'tool-filter':element('tool-filter'),query:element('query'),category:element('category','all'),'filter-status':element('filter-status'),'no-results':element('no-results')};
 nodes['filter-status'].dataset.template=html.match(/data-template="([^"]+)"/)[1];
 const cards=[...html.matchAll(/<article data-category="([^"]+)" data-search="([^"]+)">([^]*?)<\/article>/g)].map(m=>({dataset:{category:m[1],search:m[2]},textContent:m[3].replace(/<[^>]*>/g,' '),hidden:false}));
 assert.equal(cards.length,6);
 const document={documentElement:{lang:locale},getElementById:id=>nodes[id],querySelectorAll:()=>cards};
 vm.runInNewContext(fs.readFileSync(path.join(root,'app.js'),'utf8'),{document});
 const visible=()=>cards.filter(c=>!c.hidden).length;
 assert.equal(visible(),6);
 nodes.category.value='ai';handlers['category:change']();assert.equal(visible(),4);
 assert.equal(nodes['filter-status'].textContent,nodes['filter-status'].dataset.template.replace('{shown}','4').replace('{total}','6'));
 nodes.query.value='zzzz_missing';handlers['query:input']();assert.equal(visible(),0);assert.equal(nodes['no-results'].hidden,false);
 handlers['tool-filter:reset']();assert.equal(visible(),6);assert.equal(nodes.query.value,'');assert.equal(nodes.category.value,'all');
 nodes.query.value='stream';handlers['query:input']();assert.equal(visible(),1);
 console.log('PASS '+locale+' metadata, static fallback, graph links, filters, localized counts, empty state, reset, and search');
}
