/* Client enhancements only; all research content remains accessible without JS */
(function(){
const nav=location.pathname.split('/').pop()||'index.html';
document.querySelectorAll('.nav-links a').forEach(link=>{
  const target=link.getAttribute('href').split('/').pop();
  if(target===nav||nav.startsWith('step-')&&target==='journey.html') link.setAttribute('aria-current','page');
});
const filterBtns=[...document.querySelectorAll('[data-filter]')];
const input=document.querySelector('#step-search');
const cards=[...document.querySelectorAll('[data-phase]')];
function apply(){
  const btn=filterBtns.find(b=>b.getAttribute('aria-pressed')==='true');
  const phase=btn?.dataset.filter||'all';
  const q=(input?.value||'').toLowerCase().trim();
  let visible=0;
  for(const card of cards){
    const shown=(phase==='all'||card.dataset.phase===phase)&&card.textContent.toLowerCase().includes(q);
    card.hidden=!shown;if(shown)visible++;
  }
  const status=document.querySelector('#filter-result');if(status)status.textContent=visible+' steps shown';
}
filterBtns.forEach(btn=>btn.addEventListener('click',()=>{filterBtns.forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));apply()}));
input?.addEventListener('input',apply);if(cards.length)apply();
document.querySelectorAll('[data-print]').forEach(b=>b.addEventListener('click',()=>window.print()));
})();
