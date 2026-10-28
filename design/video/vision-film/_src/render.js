const {chromium}=require('playwright');const fs=require('fs');
const mode=process.argv[2];
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const mk=async()=>{const pg=await b.newPage({viewport:{width:1920,height:1080}});
   const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
   await pg.goto('file://'+process.cwd()+'/film.html');await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(300);
   if(errs.length)console.log('ERR',errs);return pg;};
 if(mode==='range'){const fps=30;const [a,b]=process.argv.slice(3).map(Number);fs.mkdirSync('frames2',{recursive:true});const pages=[];for(let i=0;i<4;i++)pages.push(await mk());let next=a;await Promise.all(pages.map(async pg=>{while(true){const f=next++;if(f>b)break;await pg.evaluate(t=>render(t),f/fps);await pg.screenshot({path:`frames2/c_${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});}}));console.log('range done',a,b);}
 else if(mode==='stills'){
   const pg=await mk();const total=await pg.evaluate(()=>TOTAL);console.log('total',total, JSON.stringify(await pg.evaluate(()=>sceneTimes())));
   const SD=process.env.SD||'stills';fs.mkdirSync(SD,{recursive:true});
   for(const t of process.argv.slice(3).map(Number)){await pg.evaluate(t=>render(t),t);await pg.screenshot({path:`${SD}/s_${String(Math.round(t*100)).padStart(5,'0')}.jpg`,type:'jpeg',quality:80});}
 } else {
   const fps=30;const pg0=await mk();const total=await pg0.evaluate(()=>TOTAL);const N=Math.round(total*fps);
   fs.mkdirSync('frames',{recursive:true});const W=4;const pages=[pg0];for(let i=1;i<W;i++)pages.push(await mk());
   let next=0;await Promise.all(pages.map(async pg=>{while(true){const f=next++;if(f>=N)break;await pg.evaluate(t=>render(t),f/fps);await pg.screenshot({path:`frames/f_${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});if(f%300===0)console.log('frame',f,'/',N);}}));
   console.log('done',N);
 }
 await b.close();})();
