import os, json
K='/home/user/solen-backend/design/clone-wolf-kit'
os.makedirs(K+'/learn-example',exist_ok=True)
css=open('fonts-all.css').read()
P='<path d="M17.47 0.00 L55.47 0.00 L45.47 11.00 L13.47 11.00 Z"/><path d="M65.47 0.00 L51.64 38.00 L42.82 32.00 L54.47 0.00 Z"/><path d="M48.00 48.00 L10.00 48.00 L20.00 37.00 L52.00 37.00 Z"/><path d="M0.00 48.00 L13.83 10.00 L22.65 16.00 L11.00 48.00 Z"/>'
def mark(w): return f'<svg width="{w}" height="{round(w*48/65.47)}" viewBox="0 0 65.47 48" fill="#fff">{P}</svg>'
BG="background:#040A06;background-image:linear-gradient(rgba(126,240,165,0.05) 1px,transparent 1px),linear-gradient(90deg,rgba(126,240,165,0.05) 1px,transparent 1px);background-size:54px 54px"
GLOW='<div style="position:absolute;left:50%;top:45%;width:1500px;height:1500px;transform:translate(-50%,-50%);background:radial-gradient(closest-side,rgba(43,208,122,0.28),rgba(43,208,122,0))"></div>'
def wrap(inner,n):
    open(f'f{n}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div id="c" style="position:relative;width:1080px;height:1920px;overflow:hidden;font-family:\'Inter Tight\';color:#EEF5F0;{BG}">{GLOW}{inner}</div></body></html>')
def pill(t): return f'<div style="position:absolute;left:0;right:0;top:230px;display:flex;justify-content:center"><span style="font-family:\'JetBrains Mono\';font-weight:600;font-size:30px;letter-spacing:.18em;text-transform:uppercase;color:#7EF0A5;border:2px solid #183323;background:#07130C;border-radius:999px;padding:14px 34px">{t}</span></div>'
def caption(parts):
    h=''.join(f'<span style="color:#7EF0A5">{t}</span> ' if hl else f'{t} ' for t,hl in parts)
    return f'<div style="position:absolute;left:90px;right:90px;top:1340px;text-align:center;font-weight:800;font-size:84px;line-height:1.05;letter-spacing:-.03em;text-transform:uppercase;text-shadow:0 8px 30px rgba(0,0,0,.75)">{h}</div>'
def logo_small(): return f'<div style="position:absolute;left:0;right:0;bottom:200px;display:flex;justify-content:center;align-items:center;gap:18px;opacity:.9">{mark(62)}<span style="font-family:Archivo;font-stretch:125%;font-weight:800;font-size:42px;line-height:1">Solen</span></div>'
def ring(x,y,w,h): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border:6px solid #2BD07A;border-radius:22px;box-shadow:0 0 0 10px rgba(43,208,122,.18),0 0 60px rgba(43,208,122,.55)"></div>'
def card(ring_html=''):
    return f'''<div style="position:absolute;left:150px;top:420px;width:780px;height:860px;background:#07130C;border:2px solid #183323;border-radius:36px;padding:44px;box-sizing:border-box;box-shadow:0 40px 120px rgba(0,0,0,.6)">
<div style="height:300px;border-radius:24px;background:linear-gradient(135deg,#12301F,#0A1D12);border:2px solid #183323"></div>
<div style="margin-top:34px;height:30px;width:420px;border-radius:8px;background:#26402F"></div>
<div style="margin-top:26px;display:flex;align-items:center;gap:20px"><span style="color:#2BD07A;font-size:40px;letter-spacing:6px">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span style="font-family:'JetBrains Mono';font-size:28px;color:#93AA9C">reviews</span></div>
<div style="margin-top:20px;font-weight:800;font-size:60px;letter-spacing:-.03em">Price</div>
<div style="margin-top:34px;height:96px;border-radius:20px;background:#2BD07A;display:flex;align-items:center;justify-content:center;color:#040A06;font-weight:800;font-size:38px">Add to cart</div>
<div style="margin-top:26px;display:flex;gap:18px"><div style="height:24px;width:300px;border-radius:8px;background:#26402F"></div><div style="height:24px;width:260px;border-radius:8px;background:#26402F"></div></div>
{ring_html}</div>'''
# hook
wrap(pill('Learn')+f'<div style="position:absolute;left:90px;right:90px;top:520px;text-align:center;font-weight:800;font-size:128px;line-height:1.02;letter-spacing:-.045em">Before you A/B test anything, check <span style="font-style:italic;background:linear-gradient(90deg,#B6F5C8,#2BD07A);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:8px">3 things</span></div>'+caption([('Most stores skip',False),('number one',True)])+logo_small(),1)
# step 1: ring on stars+price (relative to card: inside card coords)
wrap(pill('1 of 3')+card(ring(36,420,560,166))+caption([('Reviews',True),('and price,',False),('first screen',False)])+logo_small(),2)
wrap(pill('2 of 3')+card(ring(36,600,704,112))+caption([('One',False),('clear',False),('button',True)])+logo_small(),3)
wrap(pill('3 of 3')+card(ring(36,722,704,44))+caption([('Returns',True),('and delivery',False),('near the button',False)])+logo_small(),4)
# cta
wrap(f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:58px;text-align:center;padding:0 90px"><div style="display:flex;align-items:center;gap:36px">{mark(190)}<span style="font-family:Archivo;font-stretch:125%;font-weight:800;font-size:128px;line-height:1">Solen</span></div><div style="font-weight:800;font-size:104px;letter-spacing:-.04em;line-height:1.04">Want us to check <span style="font-style:italic;background:linear-gradient(90deg,#B6F5C8,#2BD07A);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:6px">your page?</span></div><div style="font-family:\'JetBrains Mono\';font-weight:600;font-size:66px;background:#7EF0A5;color:#040A06;padding:24px 56px;border-radius:24px">Comment AUDIT</div></div>',5)
json.dump([[f'f{n}.html',f'{K}/learn-example/frame-0{n}.png',1080,1920,False] for n in range(1,6)],open('jobs2.json','w'))
