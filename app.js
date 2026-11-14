(function(){
'use strict';
const form=document.getElementById('tool-filter');
const query=document.getElementById('query');
const category=document.getElementById('category');
const status=document.getElementById('filter-status');
const empty=document.getElementById('no-results');
const cards=Array.from(document.querySelectorAll('#app-cards article'));
function normalize(value){return value.normalize('NFKC').toLocaleLowerCase().trim();}
function update(){
 const terms=normalize(query.value).split(/\s+/).filter(Boolean);
 let visible=0;
 cards.forEach(card=>{
  const text=normalize(card.dataset.search+' '+card.textContent);
  const matches=(category.value==='all'||card.dataset.category===category.value)&&terms.every(term=>text.includes(term));
  card.hidden=!matches;
  if(matches)visible++;
 });
 status.textContent=visible+' of '+cards.length+' apps shown';
 empty.hidden=visible!==0;
}
form.hidden=false;
form.addEventListener('submit',event=>event.preventDefault());
query.addEventListener('input',update);
category.addEventListener('change',update);
form.addEventListener('reset',()=>{query.value='';category.value='all';update();});
update();
})();
