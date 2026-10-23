import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium', args:['--allow-file-access-from-files']});
const names={1:'01-character-creation',2:'02-video-generation',3:'03-editing'};
for (const v of [1,2,3]) {
  const p = await b.newPage({viewport:{width:794,height:1123}});
  await p.goto('file://'+process.cwd()+`/vol${v}.html`);
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg,i)=>{const r=pg.getBoundingClientRect();let m=0;pg.querySelectorAll('*').forEach(e=>{if(e.classList.contains('num')||e.classList.contains('run'))return;const b=e.getBoundingClientRect();m=Math.max(m,b.bottom-r.top)});return m>1075?`p${i+1}:${Math.round(m)}`:null}).filter(Boolean));
  console.log('vol',v,'overflow',JSON.stringify(over));
  const n = await p.locator('.page').count();
  for (let i=0;i<n;i++) await p.locator('.page').nth(i).screenshot({path:`v${v}-${String(i+1).padStart(2,'0')}.png`});
  await p.pdf({path:`/home/user/solen-backend/design/guide-cutscene/you-met-me-style-${names[v]}.pdf`,format:'A4',printBackground:true,preferCSSPageSize:true});
  await p.close();
}
await b.close();
