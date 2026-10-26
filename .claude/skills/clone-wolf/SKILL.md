---
name: clone-wolf
description: "Turn ONE topic into ONE vertical short (1080x1920): AI avatar of you (HeyGen) + HyperFrames motion graphics + real proof, with punch captions and a music bed. Use when the user says /clone-wolf or 'make a short from this topic'."
argument-hint: 'clone-wolf <topic or hook>'
allowed-tools: Bash, Read, Write, Edit, Agent
user-invocable: true
---

# Clone Wolf: one topic → one short

Everything lives in `~/shortform-pipeline/` (code in `engine/`). Load keys first:
`set -a && source ~/.claude/.env && set +a`. One folder per short: `out/<slug>/`.

**The job of every short:** a real payoff, fast loops, one loop left open, then one ask.
**Taste:** simple, bold, big, clean. One idea per frame, centered. Premium comes from light, depth and motion, never clutter.

**Where facts live (never copy them here):** script rules `engine/SCRIPTING.md` · beat format, layouts, captions, music `engine/EDL.md` · what to show `engine/GRAPHICS.md` · motion components `engine/mg/README.md` · avatar looks `engine/avatar.json` · layout numbers `engine/style.json` · themes `engine/themes/`.

## 1. Hook
Start from a proven hook (a hook that already got views in your niche). Keep its wording and structure, swap only the slots (tool, topic, number). It must read clearly to a cold viewer. Numbers only with a source.

## 2. Script (lock it before the avatar)
Follow `engine/SCRIPTING.md`. Read it aloud as a cold viewer; cut any unclear line. Write money as words ("five dollars"): HeyGen reads "$5" digit by digit. Save `out/<slug>/script_<slug>.json`. Goal: one HeyGen render per short, so lock the words first.

## 3. Avatar
`python3 engine/avatar.py --script out/<slug>/script_<slug>.json --out out/<slug>/avatar_<slug>.mp4`
Default look comes from `engine/avatar.json`. Re-render only when the spoken words change.

## 4. Plan + EDL
1. Dissect the script into `out/<slug>/plan_<slug>.json`: what is on screen for each line (see `engine/GRAPHICS.md`).
2. Write `out/<slug>/edl_<slug>.json` from the plan (format: `engine/EDL.md`).
Taste: animate the verb; show anything named on screen; every screenshot must be readable at phone size in 1 second; something new by ~2s; no graphic label that repeats the caption; real logos only from `engine/brand/logos/`.

## 5. Build + QA
```bash
python3 engine/build_short.py --edl out/<slug>/edl_<slug>.json --out out/<slug>/passN_<slug>.mp4
python3 engine/qa.py out/<slug>/passN_<slug>.mp4 --build out/<slug>/build_<slug>.json
```
Ship only with zero FAIL and zero WARN. Then review every cut at 2x crop. Fix, re-render, repeat. Use `--incremental` for quick previews only; the final pass is a full render.

## 6. Music
`python3 engine/music_mix.py` with a bed from `music/library/approved/` (see `music/README.md`). Final: `out/<slug>/short_<slug>_music.mp4`.

## 7. Captions + cover
Write one caption per platform to `out/<slug>/captions_<slug>.json`. Max 5 hashtags. Cover: the intro title screen (`titleframe_<slug>.jpg`) or `engine/cover.py`.

## 8. Schedule + comment-to-DM (Blotato)
Needs `BLOTATO_API_KEY` in `~/.claude/.env` and your account ids pasted into `schedule.py` and `engine/dm_automation.py` (run `blotato_list_accounts` to get them).
Nothing posts without the user's explicit go.
1. Pick a unique CTA keyword: `python3 engine/keywords.py reserve <WORD> --slug <slug> --lane top` (checks the registry + live Blotato automations).
2. Dry run first: `python3 schedule.py --slug <slug> --dry-run --platforms ig,fb,tt,yt,x --date YYYY-MM-DD --hour 9`. Show the plan, then run it for real.
3. DM: `python3 engine/dm_automation.py create ...` builds the Blotato comment-to-DM for the post. Details in the file header.
4. Public "sent! check your DMs" replies under keyword comments: `engine/comment_replies.py` (run every 5 min; `engine/COMMENTS.md`, `engine/run_comment_replies.sh`).
Optional: set `KEYWORD_GUARD=1` so `avatar.py` refuses to render until the keyword is reserved.

## Reference
- Engine: HyperFrames (HTML + GSAP → MP4). Gotchas: `engine/mg/README.md`. Verify with the real renderer, not a browser.
- Crop source frames from a gridded full-res frame sheet, never guess (`engine/EDL.md` → Crop cheat sheet).
