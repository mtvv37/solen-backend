import sys
base=open('story-banner-en.html').read()
style=base[base.find('<style>')+7:base.find('</style>')]
W,H=1080,1920;cx,cy=540,960;S=104
def im(n,css): return f'<img src="{n}" style="{css}">'
L={'slip':im('slip-crop.png','height:84px;width:auto'),
'boku':im('boku-word-crop.png','width:80px;height:auto;mix-blend-mode:multiply'),
'arn':im('arntreal-word-crop.png','width:80px;height:auto;mix-blend-mode:multiply'),
'gym':im('gymshark-symbol-crop.png','width:66px;height:auto;mix-blend-mode:multiply'),
'glo':im('glossier-crop.png','height:66px;width:auto;mix-blend-mode:multiply'),
'hor':im('horace-crop.png','width:82px;height:auto;mix-blend-mode:multiply'),
'jac':im('jacquemus-crop.png','width:84px;height:auto;mix-blend-mode:multiply'),
'pol':im('polene-crop.png','height:60px;width:auto;mix-blend-mode:multiply'),'':''}
def build(order,out,head,sub,offer,hsize=80):
    pos=[(300,430,-6),(850,350,6),(130,720,4),(960,800,-3),(190,1350,-4),(890,1340,5),(400,1500,-5),(700,1580,4)]
    chips=[(x,y,r,L[k]) for (x,y,r),k in zip(pos,order)]
    p=''
    for x,y,r,c in chips:
        dx=x-cx;dy=y-cy
        c1=(cx+dx*0.2+(110 if dx>=0 else -110),cy+dy*0.5);c2=(x-dx*0.3,y-dy*0.35)
        ex=max(-60,min(1140,x+dx*0.9));ey=max(-60,min(1980,y+dy*0.9))
        s2=(x+dx*0.45+(40 if dx>=0 else -40),y+dy*0.45)
        p+=f'<path d="M{cx} {cy} C{c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} {x} {y} S{s2[0]:.0f} {s2[1]:.0f} {ex:.0f} {ey:.0f}"/>'
    for a in ['M-20 540 C250 440 480 700 760 570 S1000 400 1100 450','M-20 1230 C260 1330 420 1110 700 1210 S980 1350 1100 1250']: p+=f'<path d="{a}"/>'
    ch=''.join(f'<div style="position:absolute;left:{x-S//2}px;top:{y-S//2}px;width:{S}px;height:{S}px;border-radius:26px;background:linear-gradient(160deg,#FFFFFF,#DDEFE3);box-shadow:0 0 0 1px rgba(126,240,165,0.5),0 0 40px rgba(43,208,122,0.5);display:flex;align-items:center;justify-content:center;transform:rotate({r}deg)">{c}</div>' for x,y,r,c in chips)
    html=f'''<!doctype html><html><head><meta charset="utf-8"><style>{style}</style></head><body>
<div id="c" style="position:relative;width:{W}px;height:{H}px;background:radial-gradient(ellipse 80% 45% at 50% 50%, #0C2416 0%, #040A06 75%);overflow:hidden;font-family:'Inter Tight'">
<svg width="{W}" height="{H}" style="position:absolute;inset:0"><defs><filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter><linearGradient id="ln" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1F9D5C" stop-opacity="0.25"/><stop offset="0.5" stop-color="#7EF0A5" stop-opacity="0.9"/><stop offset="1" stop-color="#1F9D5C" stop-opacity="0.25"/></linearGradient></defs><g fill="none" stroke="url(#ln)" stroke-width="2.4" filter="url(#glow)">{p}</g></svg>
<div style="position:absolute;left:40px;top:690px;width:1000px;height:640px;background:radial-gradient(ellipse closest-side, rgba(4,10,6,0.95) 60%, rgba(4,10,6,0))"></div>
{ch}
<div style="position:absolute;left:0;right:0;top:730px;display:flex;flex-direction:column;align-items:center;gap:22px;text-align:center">
<div style="display:flex;align-items:center;gap:12px"><svg width="54" height="40" viewBox="0 0 65.47 48.00"><g fill="#FFFFFF"><path d="M17.47 0.00 L55.47 0.00 L45.47 11.00 L13.47 11.00 Z"/><path d="M65.47 0.00 L51.64 38.00 L42.82 32.00 L54.47 0.00 Z"/><path d="M48.00 48.00 L10.00 48.00 L20.00 37.00 L52.00 37.00 Z"/><path d="M0.00 48.00 L13.83 10.00 L22.65 16.00 L11.00 48.00 Z"/></g></svg><span style="font-family:'Archivo';font-stretch:125%;font-weight:800;color:#FFF;font-size:36px">Solen</span></div>
<p style="margin:0;font-size:{hsize}px;font-weight:700;letter-spacing:-0.04em;line-height:1.02;color:#EEF5F0">{head}</p>
<p style="margin:0;font-size:31px;font-weight:500;color:#B9CFC0;line-height:1.28">{sub}</p>
<p style="margin:4px 0 0;font-size:34px;font-weight:700;color:#7EF0A5;line-height:1.15">{offer}</p>
</div>
<div style="position:absolute;left:0;right:0;bottom:190px;text-align:center;font-family:'JetBrains Mono';font-size:17px;color:#6F8A78">Logos : marques de leurs propriétaires. Aucune affiliation.</div>
</div></body></html>'''
    open(out+'.html','w').write(html)
build(['slip','boku','arn','jac','gym','pol','glo','hor'],'story-offre-v1',
 'On a analysé<br><i>1 500+ pages</i><br>produit.','Avis, livraison, retours, paiement :<br>on a relevé ce que font les boutiques.','On audite ta page produit<br>sur cette base. 49 €.')
build(['arn','jac','boku','hor','pol','slip','gym','glo'],'story-offre-v2',
 'On a quadrillé<br><i>leurs pages</i><br>produit.','Pas pour les copier :<br>pour voir ce qu’elles font vraiment.','On audite ta page pour 49 €.<br>Tu repars avec une roadmap<br>à appliquer sur toutes tes pages.',hsize=84)
build(['arn','hor','boku','jac','pol','slip','gym','glo'],'story-offre-v3',
 'On a analysé<br><i>Arntreal, Horace,</i><br><i>Boku</i>…','et 300+ autres boutiques :<br>1 500+ pages produit au total.','On audite ta page produit<br>sur cette base. 49 €.',hsize=76)
build(['slip','boku','arn','jac','gym','pol','glo','hor'],'story-offre-v1-sans-prix',
 'On a analysé<br><i>1 500+ pages</i><br>produit.','Avis, livraison, retours, paiement :<br>on a relevé ce que font les boutiques.','On audite ta page produit<br>sur cette base.')
build(['arn','jac','boku','hor','pol','slip','gym','glo'],'story-offre-v2-sans-prix',
 'On a quadrillé<br><i>leurs pages</i><br>produit.','Pas pour les copier :<br>pour voir ce qu’elles font vraiment.','On audite ta page.<br>Tu repars avec une roadmap<br>à appliquer sur toutes tes pages.',hsize=84)
build(['arn','hor','boku','jac','pol','slip','gym','glo'],'story-offre-v3-sans-prix',
 'On a analysé<br><i>Arntreal, Horace,</i><br><i>Boku</i>…','et 300+ autres boutiques :<br>1 500+ pages produit au total.','On audite ta page produit<br>sur cette base.',hsize=76)
for suffix,offer in [('','On audite ta page produit<br>sur cette base. 49 €.'),('-sans-prix','On audite ta page produit<br>sur cette base.')]:
    build(['arn','hor','gym','jac','pol','slip','boku','glo'],'story-offre-v4'+suffix,
     'On a analysé<br><i>Arntreal, Horace,</i><br><i>Gymshark</i>…','et 300+ autres boutiques :<br>1 500+ pages produit au total.',offer,hsize=72)
