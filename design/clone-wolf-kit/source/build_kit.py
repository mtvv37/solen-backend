K='file:///home/user/solen-backend/design/clone-wolf-kit/'
css=open('fonts-all.css').read()+open('base.css').read()
EX="""
.sw{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:3mm}
.sw div{border:1px solid var(--line);border-radius:3mm;overflow:hidden;background:var(--card)}
.sw i{display:block;height:16mm}
.sw p{padding:2mm 3mm;font-size:8.5pt;line-height:1.35}
.sw b{display:block;font-size:9.5pt}
.sw code{font-family:'JetBrains Mono',monospace;font-size:8pt;color:var(--muted)}
.logobox{border-radius:3mm;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;padding:6mm;height:34mm}
.logobox img{border:0;border-radius:0;width:auto;max-height:100%;max-width:100%}
.dk{background:#040A06}.wh{background:#fff}.gr{background:#1F9D5C}
.zone{position:relative;width:54mm;height:96mm;background:#040A06;border:1px solid var(--line);border-radius:3mm;overflow:hidden;flex:none}
.zone div{position:absolute;left:0;right:0;font-family:'JetBrains Mono',monospace;font-size:6.5pt;display:flex;align-items:center;justify-content:center;text-align:center;color:#EEF5F0}
.row{display:flex;gap:6mm;align-items:flex-start}
.frames{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:2.5mm}
.frames img{border-radius:2mm}
.spec td:first-child{white-space:nowrap}
.crop img{height:58mm;object-fit:cover;object-position:center 38%}
.sample{background:#040A06;border:1px solid var(--line);border-radius:3mm;padding:5mm 6mm}
"""
def pg(n,kicker,title,body):
    return f'<section class="page"><div class="kicker">{kicker}</div><h2>{title}</h2>{body}<div class="run">Solen visual kit</div><div class="num">{n:02d}</div></section>'
pages=[]
# 1 cover
pages.append(f'''<section class="page cover" style="padding:0;gap:0"><div style="height:150mm;position:relative;background:radial-gradient(circle at 50% 55%,#12301F,#040A06 70%);display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--line)"><img src="{K}logo/solen-lockup-white.png" style="width:130mm;border:0;border-radius:0;background:none"></div>
<div style="padding:12mm 18mm 0;display:flex;flex-direction:column;gap:6mm"><div class="kicker">For the Clone Wolf pipeline</div><h1 style="font-size:44pt">Solen visual kit</h1>
<p style="font-size:14pt;line-height:1.4;color:#C9CEDD;max-width:160mm">Logo, colors, type, components and the vertical layout, plus a ready to use &ldquo;Learn&rdquo; post type with a full example. No character, only the brand.</p>
<div style="display:flex;gap:3mm;flex-wrap:wrap"><span class="tag">Logo</span><span class="tag">Colors</span><span class="tag">Type</span><span class="tag">Components</span><span class="tag">1080 x 1920</span><span class="tag">Learn post</span></div></div></section>''')
# 2 inside
pages.append(pg(2,'01 · Inside this kit','What is in the folder and where it goes',f'''
<p>Everything is in <b>design/clone-wolf-kit/</b>. Drop each part where the pipeline expects it.</p>
<table class="spec"><tr><th>Part</th><th>File</th><th>Suggested place</th></tr>
<tr><td>Logos</td><td>logo/solen-mark-*.svg, solen-mark-*.png, solen-lockup-*.png (white, green, dark)</td><td>engine/brand/logos/</td></tr>
<tr><td>Design tokens</td><td>tokens.json (colors, fonts, canvas, grid, radius)</td><td>engine/themes/ (map to your theme format)</td></tr>
<tr><td>Learn post type</td><td>LEARN-POST.md (beats, rules, caption templates)</td><td>engine/SCRIPTING.md and engine/GRAPHICS.md</td></tr>
<tr><td>Example frames</td><td>learn-example/frame-01 to 05.png (1080 x 1920)</td><td>reference for the look</td></tr>
<tr><td>This document</td><td>solen-visual-kit.pdf</td><td>reference</td></tr></table>
<div class="note"><p><b>Honest note.</b> I have only seen the skill instructions, not your engine files. The layout numbers, safe zones and caption position in this kit are my proposal in the Solen look. If <b>style.json</b> or your theme already sets them, keep those and use this kit for the brand parts: logo, colors, type and components.</p></div>
<div class="card"><h3>The look in one sentence</h3><p>Dark fir green, one idea per frame, centered, big bold type, green light and soft glow for depth. Premium comes from light and motion, never from clutter.</p></div>'''))
# 3 logo
pages.append(pg(3,'02 · Logo','The tilted rotating frame',f'''
<p>A square frame cut into four blades and tilted, as if it were turning. Use the <b>mark</b> alone for small spaces and the <b>lockup</b> (mark + wordmark) everywhere else. The wordmark is set in Archivo Expanded 800.</p>
<div class="grid3"><div class="logobox dk"><img src="{K}logo/solen-lockup-white.png"></div><div class="logobox wh"><img src="{K}logo/solen-lockup-dark.png"></div><div class="logobox gr"><img src="{K}logo/solen-lockup-white.png"></div></div>
<div class="grid3"><div class="logobox dk"><img src="{K}logo/solen-mark-white.png"></div><div class="logobox dk"><img src="{K}logo/solen-mark-green.png"></div><div class="logobox wh"><img src="{K}logo/solen-mark-dark.png"></div></div>
<table class="spec"><tr><td>Default</td><td>White lockup on the dark fir background #040A06.</td></tr>
<tr><td>On light</td><td>Dark lockup (#040A06) on white.</td></tr>
<tr><td>On green</td><td>White lockup on #1F9D5C.</td></tr>
<tr><td>Mark only</td><td>Avatars, favicons, corners of a frame. Green mark (#2BD07A) only on dark.</td></tr>
<tr><td>Clear space</td><td>At least the height of one blade (about a quarter of the mark height) on every side.</td></tr>
<tr><td>Minimum size</td><td>Mark 24 px wide on screen. Lockup 90 px wide.</td></tr></table>
<div class="grid2"><div class="card"><h3>Do</h3><ul><li>Keep the original tilt and proportions.</li><li>Use the files in logo/, never redraw it.</li><li>One logo per frame, small and calm.</li></ul></div><div class="card"><h3>Do not</h3><ul><li>Stretch, rotate again, outline or add effects.</li><li>Put the mark on a busy photo with no overlay.</li><li>Use another color than white, green or dark.</li></ul></div></div>'''))
# 4 colors + type
sw=[('Background','#040A06','Every frame'),('Card','#07130C','Panels, mock UI'),('Line','#183323','Borders, grid'),('Green','#1F9D5C','Buttons on light'),('Green bright','#2BD07A','Accent, rings'),('Green light','#7EF0A5','Key words, URL box'),('Text','#EEF5F0','Main text'),('Muted','#93AA9C','Secondary text')]
swh=''.join(f'<div><i style="background:{c}"></i><p><b>{n}</b><code>{c}</code><br><span class="muted">{u}</span></p></div>' for n,c,u in sw)
pages.append(pg(4,'03 · Colors and type','Palette and fonts',f'''
<div class="sw">{swh}</div>
<p class="muted" style="margin-top:1mm">Accent rule: green is the only color. Highlight one word per caption in light green, never more. Warning amber #FFB45B is for notes in documents only, not for videos.</p>
<div class="sample"><div style="font-weight:800;font-size:30pt;letter-spacing:-.04em;line-height:1.05">Before you A/B test anything, check <span style="font-style:italic;background:linear-gradient(90deg,#B6F5C8,#2BD07A);-webkit-background-clip:text;background-clip:text;color:transparent">3 things</span></div><div class="cap" style="margin-top:3mm">Inter Tight 800, tight tracking (-0.04em), one italic gradient word</div></div>
<table class="spec"><tr><th>Role</th><th>Font</th><th>Use</th></tr>
<tr><td>Headline, captions</td><td>Inter Tight 800</td><td>Big, bold, tracking -0.035em to -0.045em, uppercase for punch captions</td></tr>
<tr><td>Body</td><td>Inter Tight 400 / 500 / 600</td><td>Support text in documents and carousels</td></tr>
<tr><td>Wordmark</td><td>Archivo Expanded 800 (font-stretch 125%)</td><td>Only the word &ldquo;Solen&rdquo; next to the mark</td></tr>
<tr><td>Labels, URL, numbers</td><td>JetBrains Mono 400 / 600</td><td>Pills, step counters, URL box, small captions, uppercase with wide tracking</td></tr></table>
<div class="card"><h3>Gradient word</h3><p>One word or short phrase per frame can use the italic gradient from #B6F5C8 to #2BD07A. It is the only gradient on text.</p></div>'''))
# 5 components
pages.append(pg(5,'04 · Components','The building blocks',f'''
<div class="grid2">
<div class="card"><h3>Background</h3><p>Solid #040A06, a 36 px grid at 5% light green, and a soft radial glow (green 30% to transparent) behind the main object.</p><pre>background:#040A06;
grid:rgba(126,240,165,0.05) every 36px
glow:radial-gradient(closest-side,
 rgba(43,208,122,.30),transparent)</pre></div>
<div class="card"><h3>Label pill</h3><p>JetBrains Mono 600, uppercase, wide tracking, light green on card color, 2 px line border, fully rounded. Used for &ldquo;LEARN&rdquo; and &ldquo;1 OF 3&rdquo;.</p><pre>color:#7EF0A5; bg:#07130C;
border:2px solid #183323;
radius:999px</pre></div>
<div class="card"><h3>URL / keyword box</h3><p>Light green fill #7EF0A5, dark text #040A06, JetBrains Mono 600, rounded 12 px. For &ldquo;withsolen.com&rdquo; and &ldquo;Comment AUDIT&rdquo;.</p></div>
<div class="card"><h3>Mock UI card</h3><p>Panel #07130C, 2 px line border, 36 px radius, deep soft shadow. Grey-green blocks stand for images and text, so nothing in the mock can be mistaken for a real brand.</p></div>
<div class="card"><h3>Highlight ring</h3><p>6 px #2BD07A border, 22 px radius, a halo (18% green) and a glow. It circles the exact element the line names. One ring per frame.</p></div>
<div class="card"><h3>Punch caption</h3><p>Inter Tight 800, uppercase, 84 px at 1080 wide, 2 to 4 words per line, black soft shadow, one word in light green.</p></div></div>
<div class="grid3 crop"><div><img src="{K}learn-example/frame-02.png"><div class="cap">Ring + pill + caption</div></div><div><img src="{K}learn-example/frame-01.png"><div class="cap">Hook + gradient word</div></div><div><img src="{K}learn-example/frame-05.png"><div class="cap">URL / keyword box</div></div></div>'''))
# 6 layout
pages.append(pg(6,'05 · Vertical layout','1080 x 1920 zones and motion',f'''
<div class="row"><div class="zone">
<div style="top:0;height:21%;background:rgba(255,80,80,.22)">PLATFORM UI<br>0 to 220</div>
<div style="top:21%;height:6%;background:rgba(43,208,122,.22)">LABEL PILL ~230</div>
<div style="top:27%;height:42%;background:rgba(126,240,165,.10)">MAIN OBJECT<br>one idea, centered<br>420 to 1280</div>
<div style="top:69%;height:12%;background:rgba(43,208,122,.30)">PUNCH CAPTION<br>1340 to 1560</div>
<div style="top:81%;height:7%;background:rgba(238,245,240,.10)">LOGO ~1700</div>
<div style="top:88%;height:12%;background:rgba(255,80,80,.22)">PLATFORM UI<br>1700 to 1920</div></div>
<div style="flex:1;display:flex;flex-direction:column;gap:3mm">
<table class="spec"><tr><td>Canvas</td><td>1080 x 1920, 30 fps</td></tr><tr><td>Side margins</td><td>90 px minimum</td></tr><tr><td>Top, bottom</td><td>Keep text out of the top 220 px and the bottom 360 px: apps put their own buttons there</td></tr><tr><td>Main object</td><td>Centered, about 70% of the width</td></tr><tr><td>Logo</td><td>Small, centered near the bottom, 90% opacity, never on the hook frame if it crowds the headline</td></tr></table>
<div class="card"><h3>Motion</h3><ul><li>Something new on screen by about 2 seconds.</li><li>Animate the verb: the ring draws itself, the number counts up, the object slides in.</li><li>Soft ease, 0.3 to 0.5 s. No bounce, no spin, no flashing.</li><li>Light does the depth: glow behind the object, slow push-in on mock UI.</li><li>No graphic label that repeats the caption.</li></ul></div></div></div>
<div class="note"><p>These zones are a proposal. If your <b>style.json</b> has its own numbers, use them and keep the proportions of this diagram.</p></div>'''))
# 7 learn type
pages.append(pg(7,'06 · Post type','The Learn post: structure',f'''
<p>A short that teaches one thing in about 30 to 40 seconds. The viewer leaves knowing a checklist they can apply today. Educational and honest: things to check and test, never guaranteed results.</p>
<table class="spec"><tr><th>Time</th><th>Beat</th><th>Spoken</th><th>On screen</th></tr>
<tr><td>0 to 3 s</td><td><b>Hook</b></td><td>Promise the checklist, with a clear payoff</td><td>Pill &ldquo;LEARN&rdquo;, big headline, one gradient word</td></tr>
<tr><td>3 to 6 s</td><td><b>Open loop</b></td><td>Tease the one most people skip</td><td>Punch caption only</td></tr>
<tr><td>6 to 30 s</td><td><b>3 steps</b> (about 8 s each)</td><td>The thing, then why it matters, in one or two short sentences</td><td>Pill &ldquo;1 OF 3&rdquo;, mock UI, ring on the element, punch caption</td></tr>
<tr><td>30 to 36 s</td><td><b>Payoff + ask</b></td><td>One line to act on, then the CTA</td><td>CTA frame: logo, question, keyword box</td></tr></table>
<div class="grid2"><div class="card"><h3>Rules</h3><ul><li>3 steps, never more. One idea per frame.</li><li>Show what you name: if the line says &ldquo;button&rdquo;, the ring is on the button.</li><li>Every step answers: what to check, why it matters.</li><li>No invented numbers, no revenue claims, no &ldquo;+X%&rdquo;.</li><li>Money written as words in the script.</li></ul></div>
<div class="card"><h3>Hook formulas</h3><ul><li>Before you [do the expensive thing], check [3 things].</li><li>[Number] things your [page] needs before [goal].</li><li>Most [people] skip number [one].</li><li>Stop [common habit]. Check this instead.</li></ul></div></div>
<div class="card"><h3>CTA</h3><p>Instagram: &ldquo;Comment AUDIT&rdquo; (comment-to-DM). TikTok: &ldquo;Free audit of your product page. Link in bio.&rdquo; Reserve the keyword with keywords.py before the first post, so it does not clash with another automation.</p></div>'''))
# 8 example script
pages.append(pg(8,'07 · Example','Learn post, full script and captions',f'''
<p><b>Topic:</b> what to check on a product page before testing anything. About 85 spoken words, 35 seconds.</p>
<pre>HOOK (0-3 s)
Before you A/B test anything, check these three things.

LOOP (3-6 s)
Most stores skip number one.

STEP 1 (6-14 s)
One: can people see the price and the reviews on the first screen, without scrolling? Trust starts there.

STEP 2 (14-22 s)
Two: is there one clear button? When two buttons compete, people hesitate.

STEP 3 (22-30 s)
Three: are returns and delivery written right next to the button? That is where doubt shows up.

PAYOFF + ASK (30-36 s)
Fix these first, then test. Want us to check your page? Comment AUDIT.</pre>
<table class="spec"><tr><th>Beat</th><th>On screen</th><th>Punch caption</th></tr>
<tr><td>Hook</td><td>Headline, gradient on &ldquo;3 things&rdquo;</td><td>Most stores skip <span style="color:#7EF0A5">number one</span></td></tr>
<tr><td>1</td><td>Mock card, ring on stars and price</td><td><span style="color:#7EF0A5">Reviews</span> and price, first screen</td></tr>
<tr><td>2</td><td>Ring on the button</td><td>One clear <span style="color:#7EF0A5">button</span></td></tr>
<tr><td>3</td><td>Ring on the line under the button</td><td><span style="color:#7EF0A5">Returns</span> and delivery by the button</td></tr>
<tr><td>CTA</td><td>Logo, &ldquo;Want us to check your page?&rdquo;, Comment AUDIT</td><td>none</td></tr></table>
<div class="card"><h3>Voice-over (what the voice engine reads)</h3><p>Write it so the voice says exactly what you mean: numbers as words (&ldquo;three&rdquo;, &ldquo;one&rdquo;), &ldquo;A B test&rdquo; instead of &ldquo;A/B&rdquo;, no symbols, short sentences, one idea per sentence. A full stop is a real pause. About 150 words per minute: this script is about 85 words, so about 34 seconds. Delivery: confident and warm, a little faster on the hook, slower on &ldquo;number one&rdquo; and on the final ask. File: <b>voiceover-learn-01.txt</b>.</p></div>'''))
# 9 storyboard
pages.append(pg(9,'07 · Example','Storyboard, 5 frames at 1080 x 1920',f'''
<div class="frames">'''+''.join(f'<div><img src="{K}learn-example/frame-0{i}.png"><div class="cap">{t}</div></div>' for i,t in [(1,'0 to 6 s'),(2,'6 to 14 s'),(3,'14 to 22 s'),(4,'22 to 30 s'),(5,'30 to 36 s')])+f'''</div>
<p>The mock product page is generic on purpose: blocks, stars, the words &ldquo;Price&rdquo; and &ldquo;Add to cart&rdquo;. It shows the idea without copying a real store or a real brand. When you have real proof (a screenshot of a page, an audit result with the owner&rsquo;s agreement), put it in the card instead, readable at phone size within one second.</p>
<div class="grid2"><div><h3>Instagram caption</h3><pre>Before you A/B test anything, check these 3 things:

1. Price and reviews on the first screen. Trust starts where the decision happens. Test showing the star rating and review count next to the price.
2. One clear button. Two competing buttons make people hesitate. Test keeping a single main action.
3. Returns and delivery next to the button. Doubt shows up at the last click. Test one line under the button.

Comment AUDIT for a free audit of your product page.

#shopify #ecommerce</pre></div>
<div><h3>TikTok caption</h3><pre>Which of these 3 does your product page skip? Free audit of your product page, link in bio.

#shopify #ecommerce</pre></div></div>'''))
# 10 rules
pages.append(pg(10,'08 · Content rules','Rules for every Solen short',f'''
<table class="spec"><tr><td>1</td><td>No em dash and no en dash anywhere: captions, on-screen text, hashtags.</td></tr>
<tr><td>2</td><td>English only.</td></tr>
<tr><td>3</td><td>No emoji in captions or on screen.</td></tr>
<tr><td>4</td><td>No invented numbers: no revenue claims, no &ldquo;+X% conversion&rdquo;, no fake reviews. Present fixes as things to test.</td></tr>
<tr><td>5</td><td>Hashtags: exactly <b>#shopify #ecommerce</b>.</td></tr>
<tr><td>6</td><td>CTA, Instagram: &ldquo;Comment AUDIT for a free audit of your product page.&rdquo; TikTok: &ldquo;Free audit of your product page. Link in bio.&rdquo;</td></tr>
<tr><td>7</td><td>Real logos of other brands only from the approved logo folder. Mock UI stays generic.</td></tr>
<tr><td>8</td><td>Nothing is scheduled without an explicit go.</td></tr></table>
<div class="card"><h3>Before you ship</h3><ul class="check"><li>Logo is from the kit, correct color for the background</li><li>One idea per frame, centered, readable at phone size in one second</li><li>One light green word per caption, no more</li><li>No text in the platform UI zones</li><li>Captions match the script word for word</li><li>CTA keyword reserved and unique</li></ul></div>'''))
html=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Solen visual kit</title><style>{css}{EX}</style></head><body>{"".join(pages)}</body></html>'
open('kit.html','w').write(html)
