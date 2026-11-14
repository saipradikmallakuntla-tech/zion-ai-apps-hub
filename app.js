/* Progressive enhancement: locale copy lives in each HTML document. */
(function(){
'use strict';
const form=document.getElementById('tool-filter');
if(!form)return;
const query=document.getElementById('query');
const category=document.getElementById('category');
const status=document.getElementById('filter-status');
const empty=document.getElementById('no-results');
const cards=Array.from(document.querySelectorAll('#app-cards article'));
const locale=document.documentElement.lang||'en';
const template=status.dataset.template;
function normalize(value){return value.normalize('NFKD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase(locale).trim();}
function update(){
 const terms=normalize(query.value).split(/\s+/).filter(Boolean);
 let shown=0;
 cards.forEach(card=>{
  const text=normalize(card.dataset.search+' '+card.textContent);
  const match=(category.value==='all'||card.dataset.category===category.value)&&terms.every(term=>text.includes(term));
  card.hidden=!match;
  if(match)shown++;
 });
 status.textContent=template.replace('{shown}',String(shown)).replace('{total}',String(cards.length));
 empty.hidden=shown!==0;
}
form.addEventListener('submit',event=>event.preventDefault());
query.addEventListener('input',update);
category.addEventListener('change',update);
form.addEventListener('reset',()=>{query.value='';category.value='all';update();});
form.hidden=false;
update();
})();
