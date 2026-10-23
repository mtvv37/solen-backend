import os
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, 'base.css')).read()
IMG = 'file:///home/user/solen-backend/design/guide-cutscene/img/'
SERIES = 'How to make &ldquo;You met me at...&rdquo; style videos'

EXTRA = """
.cover .hero{height:140mm}
.vol{font-family:'JetBrains Mono',monospace;font-size:10pt;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.series{font-size:13pt;font-weight:600;color:#C9CEDD}
.cover h1{font-size:44pt}
.map{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:3mm}
.map div{background:var(--card);border:1px solid var(--line);border-radius:3mm;padding:4mm}
.map div.on{border-color:var(--accent);background:#141B30}
.map b{display:block;font-size:11pt;margin:1mm 0}
.map span{font-size:9pt;color:var(--muted);line-height:1.4;display:block}
.map i{font-style:normal;font-family:'JetBrains Mono',monospace;font-size:8pt;color:var(--accent)}
.set{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:2mm}
.set div{background:#0E1220;border:1px solid #26304D;border-radius:2.5mm;padding:2.5mm 3mm}
.set small{display:block;font-family:'JetBrains Mono',monospace;font-size:7.5pt;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
.set strong{font-size:11pt}
.bad{color:#FF8A8A}.good{color:#8CF0B0}
"""

def page(n, kicker, title, body, vol):
    return f"""<section class="page"><div class="kicker">{kicker}</div><h2>{title}</h2>{body}
<div class="run">Vol. {vol} · You met me at...</div><div class="num">{n:02d}</div></section>"""

def cover(vol, title, sub, img, tags):
    t = ''.join(f'<span class="tag">{x}</span>' for x in tags)
    return f"""<section class="page cover"><div class="hero"><img src="{IMG}{img}"></div>
<div class="body"><div class="series">{SERIES}</div><div class="vol">Volume {vol} of 3</div><h1>{title}</h1>
<p class="sub">{sub}</p><div class="meta">{t}</div></div><div class="run">Vol. {vol} · You met me at...</div></section>"""

def seriesmap(on):
    items = [('Vol. 1', 'Character creation', 'Persona, look, PS2 style, sets, voice.'),
             ('Vol. 2', 'Video generation', 'Script, timing, Wan 3.0 settings, prompts.'),
             ('Vol. 3', 'Editing', 'Music, lip sync, captions, end card, export.')]
    return '<div class="map">' + ''.join(
        f'<div class="{"on" if i == on else ""}"><i>{a}</i><b>{b}</b><span>{c}</span></div>'
        for i, (a, b, c) in enumerate(items)) + '</div>'

PIPE = """<table>
<tr><th>Step</th><th>Where</th><th>What you get</th></tr>
<tr><td>1. Voice</td><td>Sume · Audio · Text to speech</td><td>The voice track of your script</td></tr>
<tr><td>2. Visual assets</td><td>Sume · Image</td><td>Your character in PS2 CGI style, 3 to 4 sets, style references</td></tr>
<tr><td>3. Video</td><td>Sume · Video · Wan 3.0</td><td>A 20 s clip, 4:3, 480p, with background music</td></tr>
<tr><td>4. Music</td><td>CapCut</td><td>The background sound extracted from the clip</td></tr>
<tr><td>5. Lip sync</td><td>Sume · Lipsync · Sync Lipsync 3</td><td>The clip, his mouth synced to your voice</td></tr>
<tr><td>6. Edit</td><td>CapCut</td><td>Final video with your sound and captions</td></tr>
</table>"""

def doc(vol, pages):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Vol {vol}</title>
<link rel="stylesheet" href="fonts-embed.css"><style>{CSS}{EXTRA}</style></head><body>{''.join(pages)}</body></html>"""

# ---------------------------------------------------------------- VOL 1
v1 = [cover(1, 'Character creation',
            'Build an original character in the style of a 2005 PS2 cutscene, the room he lives in, and the voice he speaks with. Everything the video model needs before you press Generate.',
            'hf-12.5.jpg', ['Persona', '3 identifiers', 'PS2 look', 'Character sheet', 'Sets', 'Style references', 'Voice'])]

v1.append(page(2, 'Start here', 'What this series teaches', f"""
<p>These videos all follow the same recipe: a CGI character from a 2005 era game cutscene looks into the camera and says out loud what your audience thinks in silence, then ends on a line people repeat. The series breaks the recipe into three volumes.</p>
{seriesmap(0)}
<h3 style="margin-top:2mm">The full workflow at a glance</h3>
{PIPE}
<div class="card"><h3>What you need</h3><ul>
<li>A <b>Sume</b> account (sume.com): voice, images, video and lip sync in one place.</li>
<li><b>CapCut</b> for the edit.</li>
<li>A script of about 60 words. Volume 2 gives you the structure.</li></ul></div>
""", 1))

v1.append(page(3, 'Step 1 · Persona', 'Decide who he talks to before what he looks like', f"""
<p>The character is a mirror. He talks like your audience, knows their habits and teases them a little. Fill this card before you generate a single image: every visual choice comes from it.</p>
<div class="card"><h3>Persona card</h3><table>
<tr><td>Audience</td><td>Who the video is for, in their own words. <span class="muted">Example: people who run a Shopify store.</span></td></tr>
<tr><td>Attitude</td><td>One word. <span class="muted">Example: knowing, a little smug, friendly.</span></td></tr>
<tr><td>Where he lives</td><td>A place your audience recognizes as theirs. <span class="muted">Example: a gamer bedroom full of shipping boxes.</span></td></tr>
<tr><td>His signature line</td><td>The line he ends on. <span class="muted">Example: "You met me at a very optimized time in my life."</span></td></tr>
<tr><td>What he never does</td><td>Sell features, shout, use jargon.</td></tr>
</table></div>
<div class="grid2">
<div class="card"><h3 class="good">Good persona</h3><p>Specific audience, one place, one attitude. People think "that is me" in the first 3 seconds.</p></div>
<div class="card"><h3 class="bad">Weak persona</h3><p>"Entrepreneurs" in "an office". Too wide: nobody feels seen, so nobody stops scrolling.</p></div>
</div>
""", 1))

v1.append(page(4, 'Step 2 · Look', 'The rule of 3 identifiers', f"""
<p>Video models drift: hair changes color, logos vanish, outfits change between shots. The fix is to give your character exactly <b>three identifiers</b> and repeat them, word for word, in every prompt you write.</p>
<div class="set">
<div><small>Identifier 1 · head</small><strong>Hair</strong><p>A color, a cut and one odd detail. <span class="muted">Jet black hair, long curtain bangs, one grey streak over the right eye.</span></p></div>
<div><small>Identifier 2 · body</small><strong>Top</strong><p>One strong color and your small logo. <span class="muted">Dark fir green t-shirt, small white logo on the chest.</span></p></div>
<div><small>Identifier 3 · detail</small><strong>Accessory</strong><p>Something that catches light. <span class="muted">Silver wallet chain, bracelets.</span></p></div>
</div>
<div class="grid2">
<div><img src="{IMG}hf-12.5.jpg"><div class="cap">Logo on the chest: the brand is in every close up</div></div>
<div><img src="{IMG}raw-4.5.jpg"><div class="cap">The streak over one eye makes him readable at a glance</div></div>
</div>
<div class="note"><p><b>Tip:</b> colored light changes hair color on screen. Add this sentence to your video prompts: "The blue tint on his hair is only the light from the screens."</p></div>
""", 1))

v1.append(page(5, 'Step 3 · Style', 'Words that make it look like a PS2 cutscene', f"""
<p>Models default to modern, photoreal rendering. To get the 2005 look you have to name the defects of that era, one by one.</p>
<table>
<tr><th>Ask for</th><th>Effect on screen</th></tr>
<tr><td>Pre-rendered CGI cutscene from a 2005 PlayStation 2 game</td><td>Sets the era and the type of image</td></tr>
<tr><td>Low polygon models, visible angular edges</td><td>Faceted jaw, shoulders and fingers</td></tr>
<tr><td>Simple low resolution textures</td><td>Flat clothes and walls, no fine detail</td></tr>
<tr><td>Smooth waxy plastic skin, no pores</td><td>The doll-like skin of the period</td></tr>
<tr><td>Hair made of a few thick glossy chunks</td><td>Stops realistic strand-by-strand hair</td></tr>
<tr><td>Soft flat lighting, washed out colors, mild blur</td><td>The faded look of old cutscenes</td></tr>
<tr><td>Not photorealistic, not a modern game</td><td>A guard rail against drift</td></tr>
</table>
<div class="grid2">
<div><img src="{IMG}raw-10.5.jpg"><div class="cap">Close to the target: soft light, chunky hair</div></div>
<div><img src="{IMG}raw-13.0.jpg"><div class="cap">Too modern: add more of the words above</div></div>
</div>
""", 1))

v1.append(page(6, 'Step 4 · Character sheet', 'Generate the character image', f"""
<p>In Sume, open <b>Image</b>. You need one clean reference image of the character: full body, face visible, neutral pose, plain background. This image goes into every video generation.</p>
<pre>An original character, a man in his late 20s. <span class="v">[HAIR: color, cut, one odd detail]</span>. <span class="v">[TOP: one strong color, small logo on the chest]</span>. <span class="v">[ACCESSORY]</span>. Standing, facing the camera, arms relaxed, neutral expression, mouth closed, full body and face visible, plain dark background.
Pre-rendered CGI cutscene from a 2005 PlayStation 2 game: low polygon model with visible angular edges, simple low resolution textures, smooth waxy plastic skin with no pores, hair made of a few thick glossy chunks, soft flat lighting, slightly washed out colors. Not photorealistic. 4:3.</pre>
<h3>Then make two more angles</h3>
<pre>The same character, exactly the same: <span class="v">[3 IDENTIFIERS]</span>. <span class="v">[ANGLE: close up of the face, looking into the camera / three quarter view, waist up]</span>. Same rendering style. 4:3.</pre>
<div class="note"><p>Generate 4 options, keep the best, and save the exact text of your 3 identifiers in a note. You will paste it again and again.</p></div>
""", 1))

v1.append(page(7, 'Step 5 · Sets', 'Make 3 to 4 decor assets of one place', f"""
<p>The set tells the viewer who the video is for before he says a word. Make one location and shoot it from 3 or 4 angles. Put 3 objects in it that only your audience owns.</p>
<div class="grid3">
<div><img src="{IMG}raw-1.0.jpg"><div class="cap">Wide: the whole room</div></div>
<div><img src="{IMG}hf-15.5.jpg"><div class="cap">Desk: the monitor and its data</div></div>
<div><img src="{IMG}hf-0.5.jpg"><div class="cap">Corner: shelf, neon, boxes</div></div>
</div>
<pre>Empty <span class="v">[LOCATION]</span> at night, no people. <span class="v">[3 OBJECTS ONLY YOUR AUDIENCE OWNS]</span>. <span class="v">[ANGLE: wide shot of the room / close view of the desk and monitor / corner with the shelf and the neon sign]</span>. <span class="v">[LIGHT: cold blue screen light, green neon sign]</span>. Pre-rendered CGI cutscene from a 2005 PlayStation 2 game, low polygon, simple textures, soft flat lighting, washed out colors, mild blur. 4:3.</pre>
<div class="card"><h3>Example of the 3 objects</h3><p>For an ad aimed at Shopify sellers: a monitor showing a sales dashboard with a falling red chart, stacked cardboard shipping boxes, a neon sign shaped like a rising chart line.</p></div>
""", 1))

v1.append(page(8, 'Step 6 · References', 'Style references, used the right way', f"""
<p>Besides your character and your sets, you can give the video model a few images whose <b>look</b> you like: the light, the rendering, the framing of old cutscenes.</p>
<div class="grid2">
<div class="card"><h3 class="good">Use as references</h3><ul>
<li>Your character sheet and its extra angles.</li>
<li>Your 3 to 4 sets.</li>
<li>Images that show a lighting or a framing you like, with no recognizable person in them.</li></ul></div>
<div class="card"><h3 class="bad">Do not use</h3><ul>
<li>Frames of another creator's character. The model copies faces, outfits and logos it sees, and you end up with their character in your ad.</li>
<li>Real people's faces.</li>
<li>Other brands' logos.</li></ul></div>
</div>
<div class="note"><p><b>Legal, read this once.</b> A visual style is free to use. Characters, faces and voices belong to someone. An original character is also an asset you own: every new video gets cheaper because he already exists.</p></div>
<h3>How many?</h3>
<p>Character plus 3 to 4 sets worked best for us. If a generation fails, remove references first: start again with the character and 2 sets.</p>
""", 1))

v1.append(page(9, 'Step 7 · Voice', 'Give him a voice in Sume', f"""
<p>Open <b>Audio</b>, tab <b>Text to speech</b>. Make the voice first: every later step is timed on it.</p>
<img src="{IMG}ui-30.jpg"><div class="cap">Sume · Audio · Text to speech. A custom voice, model Sonic 3.6, style Natural.</div>
<div class="step"><div class="n">1</div><div><h3>Pick or create the voice</h3><p><b>Create voice</b> makes a custom voice from an audio sample. Use your own voice or a voice actor who agreed in writing. Never clone a voice from someone else's video: it is their identity. Library voices work too.</p></div></div>
<div class="step"><div class="n">2</div><div><h3>Paste the script exactly</h3><p>Model <b>Sonic 3.6</b>, style <b>Natural</b>. Write the URL as "yoursite dot com" so it is pronounced right. Punctuation drives the pauses: a period gives a real silence, which you will need to cut on.</p></div></div>
<div class="step"><div class="n">3</div><div><h3>Generate a batch, keep one</h3><p>Batch size 2 to 4, listen, download the best. Aim for 20 to 22 seconds.</p></div></div>
""", 1))

v1.append(page(10, 'Before Volume 2', 'Your asset folder and checklist', f"""
<div class="grid2">
<div class="card"><h3>Folder structure</h3><pre>character/
  sheet-front.png
  close-up.png
  identifiers.txt
sets/
  wide.png  desk.png
  monitor.png  corner.png
references/
voice/
  script.txt  voice.mp3</pre></div>
<div class="card"><h3>Checklist</h3><ul class="check">
<li>Persona card filled</li>
<li>3 identifiers written once, saved</li>
<li>Character sheet in PS2 style, 4:3</li>
<li>3 to 4 sets of one location</li>
<li>No other creator's character, no real face, no other brand's logo</li>
<li>Voice you have the right to use</li>
<li>Voice track of 20 to 22 s downloaded</li>
</ul></div>
</div>
{seriesmap(1)}
<div class="card" style="margin-top:auto"><h3>Next: Volume 2, Video generation</h3><p>Turn the script into a shot plan, set up Wan 3.0 (20 s, 4:3, 480p) and write the prompt that keeps your character the same from the first frame to the last.</p></div>
""", 1))

# ---------------------------------------------------------------- VOL 2
v2 = [cover(2, 'Video generation',
            'Write the script, plan the shots on the voice, set up Wan 3.0 in Sume and write prompts that keep your character consistent for 20 seconds.',
            'raw-7.0.jpg', ['Script', 'Timing', 'Wan 3.0', '20 s · 4:3 · 480p', 'Prompt', 'Troubleshooting'])]

v2.append(page(2, 'Start here', 'Where you are in the workflow', f"""
{seriesmap(1)}
<p>You need the assets from Volume 1: the character sheet, 3 to 4 sets, the voice track. This volume ends with one raw clip: 20 seconds, 4:3, 480p, your character in his room, with background music. The mouth is synced later, in Volume 3.</p>
{PIPE}
<div class="card"><h3>The idea that saves you money</h3><p>Do not ask the model to act, talk and lip sync your exact words in one pass. Ask it for a good-looking performance with music. The lip sync tool then puts your voice in his mouth. Each part is easier, and a failed step costs one step, not everything.</p></div>
""", 2))

v2.append(page(3, 'Step 1 · Script', 'The 5 beat script', f"""
<p>About 60 words for 20 seconds. Short sentences, because every cut happens in the silence between two sentences.</p>
<table>
<tr><th>Beat</th><th>Time</th><th>Job</th><th>Example</th></tr>
<tr><td>Hook</td><td>0-6 s</td><td>Name the audience, quote their question</td><td>Shopifiers will say: "Man, how do you know I do Shopify for a living?"</td></tr>
<tr><td>Wink</td><td>6-9 s</td><td>A beat of attitude</td><td>Haha, like I don't know, bro.</td></tr>
<tr><td>Mirror</td><td>9-17 s</td><td>Habits they recognize</td><td>You just spend all your time staring at your stats, changing your product page with absolutely no clue, and wondering: "Why is my conversion rate so low?"</td></tr>
<tr><td>Punchline</td><td>17-20 s</td><td>The line people repeat</td><td>You met me at a very optimized time in my life.</td></tr>
<tr><td>CTA</td><td>end card</td><td>What to do now</td><td>Get your free audit at yoursite dot com.</td></tr>
</table>
<pre>[AUDIENCE] will say: "Man, how do you know I [THEIR JOB]?"
Haha, like I don't know, bro.
You just [HABIT 1], [HABIT 2], and wondering: "[THEIR QUESTION]?"
You met me at a very [WORD FROM YOUR WORLD] time in my life.</pre>
<p class="muted">Write your own lines. Habits that are specific and a little embarrassing work better than features.</p>
""", 2))

v2.append(page(4, 'Step 2 · Timing', 'Plan the shots on the voice', f"""
<p>Play your voice track and note when each sentence starts and ends. The shot plan follows those times: one shot per sentence, changes only in the silences.</p>
<table>
<tr><th>Time</th><th>Line</th><th>Shot</th></tr>
<tr><td>0-5 s</td><td>Hook</td><td>At the desk, he turns his chair to the camera, puzzled, open palm. Push-in to close up.</td></tr>
<tr><td>5-9 s</td><td>Wink</td><td>Medium close up, small smirk, the monitor visible next to him.</td></tr>
<tr><td>9-12 s</td><td>Mirror</td><td>The falling chart on screen, he glances at it and back at the camera.</td></tr>
<tr><td>12-17 s</td><td>Mirror</td><td>Close up by the green neon, tired deadpan look.</td></tr>
<tr><td>17-20 s</td><td>Punchline</td><td>Close up in blue screen light, he points at the camera, half smile.</td></tr>
</table>
<div class="grid3">
<div><img src="{IMG}f-2.6.jpg"><div class="cap">Hook</div></div>
<div><img src="{IMG}f-4.6.jpg"><div class="cap">Mirror</div></div>
<div><img src="{IMG}f-15.4.jpg"><div class="cap">Punchline</div></div>
</div>
<div class="note"><p>Faces carry lip sync. Plan most shots as close ups or medium close ups, face to the camera. Keep shots of the screen or of his back short.</p></div>
""", 2))

v2.append(page(5, 'Step 3 · Settings', 'Set up Wan 3.0 in Sume', f"""
<p>Open <b>Video</b> and choose the model <b>Wan 3.0</b> (text, image and reference to video).</p>
<div class="set">
<div><small>Duration</small><strong>20 s</strong><p>Matches a 20 to 22 s voice track.</p></div>
<div><small>Aspect ratio</small><strong>4:3</strong><p>The old cutscene frame.</p></div>
<div><small>Resolution</small><strong>480p</strong><p>The era look, and the cheapest run.</p></div>
</div>
<table>
<tr><td>References</td><td>Character sheet and angles, 3 to 4 sets, a few style references. No video.</td></tr>
<tr><td>Start / end frame</td><td>Leave empty. Sume accepts either frames or references, not both.</td></tr>
<tr><td>Audio</td><td><b>On.</b> The model adds background music. You will extract it in CapCut (Volume 3) and the voice is replaced by yours with lip sync.</td></tr>
<tr><td>Price shown</td><td>$1.00 for 20 s at 480p when we made the example. Check the Generate button before each run.</td></tr>
</table>
<div class="note"><p><b>Limits we hit:</b> reference clips must add up to 15 s at most, and a reference video plus the duration cannot pass 30 s. You do not need a reference video at all, so leave it out.</p></div>
""", 2))

v2.append(page(6, 'Step 4 · Prompt anatomy', 'The 7 blocks of a good prompt', f"""
<p>Write the prompt in this order. Each block fixes one problem we met while making the example.</p>
<table>
<tr><th>Block</th><th>What it says</th><th>Problem it fixes</th></tr>
<tr><td>1. Continuity</td><td>One single continuous shot, no cuts</td><td>Hard cuts in the middle of a sentence</td></tr>
<tr><td>2. Framing</td><td>Close ups and medium close ups, face to camera, mouth visible</td><td>Lip sync that cannot find the mouth</td></tr>
<tr><td>3. Character</td><td>The 3 identifiers, word for word, "he is alone"</td><td>Hair, logo or outfit changing</td></tr>
<tr><td>4. Setting</td><td>The room of the set references, the light on him</td><td>Random locations</td></tr>
<tr><td>5. Style</td><td>The PS2 vocabulary from Volume 1</td><td>A modern, photoreal look</td></tr>
<tr><td>6. Timeline</td><td>What happens second by second</td><td>Static or aimless shots</td></tr>
<tr><td>7. Text</td><td>No subtitles, no text except the logo</td><td>Fake captions burned into the video</td></tr>
</table>
<div class="grid2">
<div><img src="{IMG}raw-4.5.jpg"><div class="cap">Close framing, mouth visible: easy to sync</div></div>
<div><img src="{IMG}raw-7.0.jpg"><div class="cap">From behind: keep it short, no sync possible</div></div>
</div>
""", 2))

v2.append(page(7, 'Step 5 · Prompt', 'The full prompt, ready to fill', f"""
<pre>One single continuous shot, no cuts at all. The camera moves smoothly from one position to the next, like a slow handheld camera following him in one take.
Framing for lip sync: only close ups and medium close ups. His face always faces the camera or a slight three quarter angle, fully visible, never hidden by his hands, hair or objects. His mouth is always clearly visible. No wide shots, no shots from behind.
The only character is the man from the character reference image, exactly the same during the whole video: <span class="v">[3 IDENTIFIERS, word for word]</span>. <span class="v">[If colored light: The blue tint on his hair is only the light from the screens.]</span> He is alone.
Setting: the <span class="v">[LOCATION]</span> shown in the set reference images: <span class="v">[3 OBJECTS]</span>. <span class="v">[LIGHT]</span> on him.
Rendering style: exactly like the set reference images, a pre-rendered CGI cutscene from a 2005 PlayStation 2 game. Low polygon models with visible angular edges, simple low resolution textures, smooth waxy plastic skin, hair in a few thick glossy chunks, soft flat lighting, washed out colors, 480p look. Not photorealistic, not a modern game.
He talks to the camera with natural hand gestures at chest height. Background music only.
0-5s: <span class="v">[HOOK SHOT]</span>, slow push-in to a close up.
5-9s: without cutting, <span class="v">[WINK SHOT]</span>.
9-12s: without cutting, <span class="v">[MIRROR SHOT 1]</span>.
12-17s: without cutting, <span class="v">[MIRROR SHOT 2]</span>.
17-20s: without cutting, he looks straight at the camera and points at it, confident half smile.
No subtitles, no text on screen except the logo on his top.</pre>
""", 2))

v2.append(page(8, 'Step 6 · Direction', 'Camera moves and gestures that work', f"""
<div class="grid2">
<div class="card"><h3>Camera</h3><ul>
<li><b>Slow push-in</b>: the default. Adds tension to any line.</li>
<li><b>Quick punch-in</b> on a key word ("bro", "optimized").</li>
<li><b>Small handheld movement</b>: never a frozen frame.</li>
<li><b>Glide to the side</b> to reveal the monitor without cutting.</li></ul></div>
<div class="card"><h3>Gestures</h3><ul>
<li>Open palm at chest height: the confused customer.</li>
<li>Glance at the screen, then back at the camera.</li>
<li>Tired deadpan stare: the mirror line.</li>
<li>Point at the camera: the punchline.</li></ul></div>
</div>
<div class="grid3">
<div><img src="{IMG}f-2.6.jpg"><div class="cap">Open palm</div></div>
<div><img src="{IMG}f-9.2.jpg"><div class="cap">Glance at the screen</div></div>
<div><img src="{IMG}raw-18.0.jpg"><div class="cap">Point and smile</div></div>
</div>
<div class="note"><p>Hands stay below the chin. A hand in front of the mouth breaks the lip sync for that whole moment.</p></div>
""", 2))

v2.append(page(9, 'Troubleshooting', 'Errors we hit and the fix', f"""
<table>
<tr><th>Problem</th><th>Fix</th></tr>
<tr><td>"input_video_duration + duration exceeds 30s limit"</td><td>Remove the reference video. You do not need one.</td></tr>
<tr><td>"Reference clips must add up to at most 15s"</td><td>Same: no video in the references.</td></tr>
<tr><td>"Use either a start / end frame or reference media, not both"</td><td>Remove the frames, keep the references.</td></tr>
<tr><td>Generation failed</td><td>Remove a video if any, then keep only the character and 2 sets.</td></tr>
<tr><td>Hard cuts between shots</td><td>Block 1 of the prompt: one continuous shot, "without cutting" on every line.</td></tr>
<tr><td>Too realistic, looks like a new game</td><td>More PS2 vocabulary, and sets generated in the same style.</td></tr>
<tr><td>Hair or logo changes</td><td>3 identifiers word for word, the light sentence for colored hair.</td></tr>
<tr><td>Another person appears</td><td>"He is alone" and no references showing other people.</td></tr>
</table>
<img src="{IMG}ui-29.jpg" style="max-height:72mm;object-fit:cover;object-position:top"><div class="cap">Sume refuses start / end frames and references together</div>
""", 2))

v2.append(page(10, 'Before Volume 3', 'Review the raw clip', f"""
<div class="grid2">
<div><img src="{IMG}raw-4.5.jpg"><div class="cap">Keep: face to camera, identifiers intact</div></div>
<div><img src="{IMG}raw-1.0.jpg"><div class="cap">Short only: wide shot, face too small to sync</div></div>
</div>
<div class="card"><h3>Keep the clip if</h3><ul class="check">
<li>He looks the same from start to end: hair, top, logo, accessory</li>
<li>His face is visible and large in most of the clip</li>
<li>No cut in the middle of a line of your voice track</li>
<li>No other person, no fake text on screen</li>
<li>The look is PS2 cutscene, not a modern game</li>
<li>The background music fits the mood</li>
</ul></div>
<div class="card"><h3>Cost of one try, at the prices shown when we made it</h3><p>Wan 3.0, 20 s, 480p: $1.00. If two of the checks above fail, regenerate rather than fixing it in the edit.</p></div>
{seriesmap(2)}
""", 2))

# ---------------------------------------------------------------- VOL 3
v3 = [cover(3, 'Editing',
            'Extract the music, sync his mouth to your voice, then cut, caption and export in CapCut. From the raw clip to a video you can post.',
            'f-15.4.jpg', ['CapCut', 'Music extraction', 'Sync Lipsync 3', 'Captions', 'End card', 'Export', 'Measure'])]

v3.append(page(2, 'Start here', 'From raw clip to posted video', f"""
{seriesmap(2)}
<p>You have the raw clip from Volume 2 (20 s, 4:3, 480p, with background music) and the voice track from Volume 1. Four moves turn them into the final video.</p>
<div class="flow">
<div><i>01</i><b>Extract</b><span>Pull the background music out of the clip in CapCut.</span></div>
<div><i>02</i><b>Lip sync</b><span>Sync his mouth to your voice in Sume.</span></div>
<div><i>03</i><b>Edit</b><span>Voice, music, captions and end card in CapCut.</span></div>
<div><i>04</i><b>Export</b><span>Vertical, loud enough, then measure.</span></div>
</div>
<img src="{IMG}f-6.6.jpg"><div class="cap">The finished video: synced voice, music underneath, captions</div>
""", 3))

v3.append(page(3, 'Step 1 · Music', 'Extract the background sound in CapCut', f"""
<p>The clip from Wan comes with music. Keep it: it was generated for this exact video and fits its rhythm.</p>
<div class="step"><div class="n">1</div><div><h3>Import the raw clip</h3><p>New project in CapCut, drop the raw clip on the timeline.</p></div></div>
<div class="step"><div class="n">2</div><div><h3>Extract the audio</h3><p>Use CapCut's extract audio option on the clip. You get the soundtrack as its own audio track.</p></div></div>
<div class="step"><div class="n">3</div><div><h3>Keep only the music</h3><p>If the model added voices or noises, use CapCut's vocal isolation or noise reduction to keep the background only. Menu names change between CapCut versions: look in the audio panel of the selected track.</p></div></div>
<div class="step"><div class="n">4</div><div><h3>Export the music</h3><p>Export it as an audio file, or keep the project open: you will put the lip synced video back on top.</p></div></div>
<div class="note"><p>Prefer a different sound? You can use any track you have the right to use, or a trending sound inside TikTok or Instagram when you post.</p></div>
""", 3))

v3.append(page(4, 'Step 2 · Lip sync', 'Put your voice in his mouth', f"""
<p>In Sume, open <b>Lipsync</b>, tab <b>Video to video</b>, model <b>Sync Lipsync 3</b> (re-syncs a clip's lips to new audio).</p>
<img src="{IMG}ui-32.jpg"><div class="cap">Sume · Lipsync · Video to video. Clip of 20 s, voice of 21 s, price shown $2.80.</div>
<div class="step"><div class="n">1</div><div><h3>Upload the raw clip and the voice track</h3><p>Lengths should be close. A voice longer than the clip gets cut at the end.</p></div></div>
<div class="step"><div class="n">2</div><div><h3>Generate and watch it on mute, then with sound</h3><p>On mute you see whether the mouth moves naturally. With sound you check each word lands. Wide shots and shots from behind will not sync: that is fine, the voice plays over them.</p></div></div>
""", 3))

v3.append(page(5, 'Step 3 · Timeline', 'Build the edit in CapCut', f"""
<p>Back in CapCut, set up three layers.</p>
<table>
<tr><th>Track</th><th>Content</th><th>Rule</th></tr>
<tr><td>Video</td><td>The lip synced clip</td><td>Its audio is your voice: keep it as the main sound</td></tr>
<tr><td>Music</td><td>The background you extracted, or your sound</td><td>Well under the voice: every word must be clear on a phone speaker</td></tr>
<tr><td>Text</td><td>Captions, then the end card</td><td>Added in steps 4 and 5</td></tr>
</table>
<div class="card"><h3>Cutting</h3><ul>
<li>Cut only in the silences between sentences.</li>
<li>Trim dead air at the start: the first word lands in the first second.</li>
<li>Keep the full punchline, then go straight to the end card.</li>
<li>Aim for 20 seconds in total, end card included.</li></ul></div>
<div class="grid2">
<div><img src="{IMG}f-0.4.jpg"><div class="cap">0 s: the first word is already there</div></div>
<div><img src="{IMG}f-15.4.jpg"><div class="cap">The punchline, then the end card</div></div>
</div>
""", 3))

v3.append(page(6, 'Step 4 · Captions', 'Subtitles people can read with no sound', f"""
<p>Many people watch muted. Captions carry the joke when the sound is off.</p>
<div class="grid2">
<div class="card"><h3>Style</h3><ul>
<li>CapCut auto captions in English.</li>
<li>2 to 5 words on screen at a time.</li>
<li>Big white text, black outline or shadow.</li>
<li>Lower third, centered, clear of the face.</li></ul></div>
<div class="card"><h3>Proofread every line</h3><ul>
<li>Auto captions invent words. Compare them with your script.</li>
<li>In English, no space before "?" or "!".</li>
<li>Keep quotation marks on the quoted question.</li>
<li>Your URL spelled the way people type it.</li></ul></div>
</div>
<div class="grid2">
<div><img src="{IMG}f-13.6.jpg"><div class="cap">To fix: "so low ?" should be "so low?"</div></div>
<div><img src="{IMG}f-4.6.jpg"><div class="cap">To fix: the script said "Haha, like I don't know, bro"</div></div>
</div>
""", 3))

v3.append(page(7, 'Step 5 · End card', 'Close on one clear action', f"""
<p>The last 3 to 4 seconds. The CTA line of your voice plays over it.</p>
<div class="grid2">
<div><img src="{IMG}f-18.5.jpg"><div class="cap">Logo, one benefit, the URL in a button</div></div>
<div class="card"><h3>Rules</h3><ul>
<li>Your logo and name.</li>
<li>One benefit in 4 words or less: "Get your free audit".</li>
<li>The URL, big, in a high contrast box.</li>
<li>The same aspect ratio as the rest of the video, or you get black bars.</li>
<li>Nothing else on screen.</li></ul></div>
</div>
<div class="card"><h3>Make it in 4:3 and in 9:16</h3><p>Design the card once in each ratio: 4:3 (768 x 576) to match the generated clip, 9:16 (1080 x 1920) for the vertical export. A simple dark background with your brand color is enough.</p></div>
""", 3))

v3.append(page(8, 'Step 6 · Export', 'Vertical, sharp enough, loud enough', f"""
<table>
<tr><th>Setting</th><th>Value</th><th>Why</th></tr>
<tr><td>Canvas</td><td>9:16, 1080 x 1920</td><td>TikTok, Reels and Shorts fill the screen with it</td></tr>
<tr><td>4:3 clip</td><td>Full width in the middle, blurred copy behind</td><td>No black bars, the image stays big</td></tr>
<tr><td>Captions</td><td>Inside the middle area</td><td>Clear of the app buttons at the bottom and the right</td></tr>
<tr><td>Loudness</td><td>About -14 LUFS</td><td>Our first export was near -30 LUFS, much quieter than the videos around it</td></tr>
<tr><td>Length</td><td>About 20 s</td><td>Short enough to watch twice</td></tr>
</table>
<div class="note"><p><b>Check on a phone before posting:</b> watch it once muted (captions alone must carry the joke) and once with sound on the speaker (every word clear above the music).</p></div>
<div class="card"><h3>Upscale?</h3><p>The clip is 480p on purpose: the soft look is part of the style. Export at 1080 x 1920 anyway so the captions and the end card stay sharp.</p></div>
""", 3))

v3.append(page(9, 'Step 7 · Measure', 'Know if it works before you make ten more', f"""
<p>Post, wait 48 hours, write down four numbers from the platform analytics. Compare them with your own average post.</p>
<table>
<tr><th>Metric</th><th>Question it answers</th></tr>
<tr><td>3 second hold rate</td><td>Does the first frame stop the scroll?</td></tr>
<tr><td>Completion rate</td><td>Does the script hold attention to the end card?</td></tr>
<tr><td>Profile visits</td><td>Did the character make people curious?</td></tr>
<tr><td>Clicks or keyword comments</td><td>Did anyone act on the CTA?</td></tr>
</table>
<div class="card"><h3>Change one thing per video</h3><p>Same character and room, new script: you learn which message works. Same script, new first shot: you learn what stops the scroll.</p></div>
<h3>Cost of one finished video, at the prices shown when we made it</h3>
<table>
<tr><td>Wan 3.0 · 20 s · 4:3 · 480p</td><td>$1.00</td></tr>
<tr><td>Sync Lipsync 3 · 20 s clip</td><td>$2.80</td></tr>
<tr><td>Voice and images</td><td>Check the Generate buttons in Sume</td></tr>
</table>
<p class="muted">Prices change. Retries add up: follow the checklists to need fewer of them.</p>
""", 3))

v3.append(page(10, 'Before you post', 'The final checklist', f"""
<div class="grid2">
<div class="card"><h3>Sound</h3><ul class="check">
<li>Background music extracted, or a sound you have the right to use</li>
<li>Voice clear above the music on a phone speaker</li>
<li>About -14 LUFS</li></ul></div>
<div class="card"><h3>Lip sync</h3><ul class="check">
<li>Mouth matches every word on face shots</li>
<li>No word cut at the end of the clip</li></ul></div>
<div class="card"><h3>Edit</h3><ul class="check">
<li>Cuts only in silences</li>
<li>First word in the first second</li>
<li>Every caption proofread against the script</li>
<li>End card 3 to 4 s, same ratio</li></ul></div>
<div class="card"><h3>Export and after</h3><ul class="check">
<li>9:16, 1080 x 1920</li>
<li>Watched muted and with sound on a phone</li>
<li>48 h later: hold, completion, profile visits, clicks</li>
<li>One change picked for the next video</li></ul></div>
</div>
<div class="card" style="margin-top:auto"><h3>The whole recipe in one breath</h3><p>Persona, 3 identifiers, PS2 vocabulary, sets, voice. Script on 5 beats, shots on the silences, Wan 3.0 at 20 s, 4:3, 480p. Extract the music, sync the mouth, cut, caption, end card, export vertical, measure, change one thing.</p></div>
""", 3))

names = {1: '01-character-creation', 2: '02-video-generation', 3: '03-editing'}
for vol, pages in ((1, v1), (2, v2), (3, v3)):
    open(os.path.join(HERE, f'vol{vol}.html'), 'w').write(doc(vol, pages))
print('ok', len(v1), len(v2), len(v3))
