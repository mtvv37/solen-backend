import os, json
K='/home/user/solen-backend/design/clone-wolf-kit'
os.makedirs(K+'/logo',exist_ok=True)
P='<path d="M17.47 0.00 L55.47 0.00 L45.47 11.00 L13.47 11.00 Z"/><path d="M65.47 0.00 L51.64 38.00 L42.82 32.00 L54.47 0.00 Z"/><path d="M48.00 48.00 L10.00 48.00 L20.00 37.00 L52.00 37.00 Z"/><path d="M0.00 48.00 L13.83 10.00 L22.65 16.00 L11.00 48.00 Z"/>'
cols={'white':'#FFFFFF','green':'#2BD07A','dark':'#040A06'}
for n,c in cols.items():
    open(f'{K}/logo/solen-mark-{n}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 65.47 48" width="654" height="480"><g fill="{c}">{P}</g></svg>\n')
css=open('fonts-all.css').read()
def page(name,w,h,inner,bg='transparent'):
    open(f'{name}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}html,body{{background:transparent}}</style></head><body><div id="c" style="width:{w}px;height:{h}px;background:{bg};display:flex;align-items:center;justify-content:center">{inner}</div></body></html>')
def mark(c,w): return f'<svg width="{w}" height="{round(w*48/65.47)}" viewBox="0 0 65.47 48"><g fill="{c}">{P}</g></svg>'
def lock(c,s=1): 
    return f'<div style="display:flex;align-items:center;gap:{round(42*s)}px">{mark(c,round(300*s))}<span style="font-family:Archivo;font-stretch:125%;font-weight:800;font-size:{round(220*s)}px;line-height:1;color:{c};letter-spacing:-0.01em">Solen</span></div>'
jobs=[]
for n,c in cols.items():
    page(f'm-{n}',1024,751,mark(c,1024)); jobs.append((f'm-{n}.html',f'{K}/logo/solen-mark-{n}.png',1024,751,True))
    page(f'l-{n}',2200,520,lock(c)); jobs.append((f'l-{n}.html',f'{K}/logo/solen-lockup-{n}.png',2200,520,True))
json.dump(jobs,open('jobs.json','w'))
tokens={"name":"solen","colors":{"bg":"#040A06","card":"#07130C","line":"#183323","green":"#1F9D5C","greenBright":"#2BD07A","greenLight":"#7EF0A5","text":"#EEF5F0","muted":"#93AA9C","warn":"#FFB45B"},
"fonts":{"headline":"Inter Tight 800","wordmark":"Archivo Expanded 800 (font-stretch 125%)","label":"JetBrains Mono 400/600","body":"Inter Tight 400/500/600"},
"canvas":{"width":1080,"height":1920},"background":{"gridSize":36,"gridColor":"rgba(126,240,165,0.05)","glow":"radial-gradient(closest-side, rgba(43,208,122,0.30), rgba(43,208,122,0))"},
"radius":{"card":24,"pill":999,"urlBox":12}}
json.dump(tokens,open(K+'/tokens.json','w'),indent=2)
