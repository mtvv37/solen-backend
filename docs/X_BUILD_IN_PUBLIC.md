# Solen : 90 posts X en 30 jours (3 par jour, prêts à copier-coller)

> Version 0.2, 29/09/2026. Posts en anglais, tous ≤ 280 caractères, sans champ à compléter.
> Base : [`SOLEN_CONTEXT.md`](SOLEN_CONTEXT.md), [`GTM_STRATEGY.md`](GTM_STRATEGY.md), `docs/Solen_Market_GTM.pptx`.

## Mode d'emploi

- **Horaires suggérés** : A à 9h, B à 13h, C à 18h (heure de Paris). Le soir touche aussi la côte Est des États-Unis.
- **En plus des posts** : 10 à 15 réponses utiles par jour sous des comptes e-commerce, Shopify et CRO. Sur un petit compte, c'est ce qui apporte le plus de visibilité.
- **Bio X** : `Building Solen: turning Shopify visitor behavior into tested improvements. Ex-strategy/data. Looking for a technical cofounder.`
- **Visuels** : tous faisables en 5 minutes maximum. « Texte seul » = aucun visuel. « Wireframe » = un téléphone dessiné dans Excalidraw ou Figma, avec 1 à 2 flèches (aucune marque réelle).

### Ce que ces posts ne font jamais

- Aucun post ne cite une marque réelle ni des données de marchand.
- Aucun post n'annonce de résultat. Les frictions sont des hypothèses, avec le test qui permettrait de trancher.
- Aucun post n'invente de chiffre d'interviews ou de clients. Les seuls chiffres sont sourcés (Store Leads, 2026) ou présentés comme des suppositions.
- Si ta situation change (premier client, cofondateur trouvé), supprime ou adapte les posts qui disent « 0 customers » ou « looking for a cofounder ».

### Ce qu'on mesure

Pas les abonnés : demandes d'audit, messages privés qualifiés, interviews obtenues, contacts cofondateur. Si après 6 semaines X n'apporte rien de tout ça, passe X à 2 ou 3 posts par semaine et reporte l'effort sur LinkedIn.

### Les 5 thèmes

🔍 Friction à tester (27 posts) · 🛠 Journal de construction · 🎙 Interviews et méthode · 💬 Opinion · 📣 Appel (audits, pilotes, cofondateur)

---

## Semaine 1

### Jour 1

**A** 🛠
```
I'm building Solen in public.

The bet: Shopify stores have plenty of visitor data but no time to turn it into tested changes.

Status: working prototype, 0 customers, 15 merchant interviews to run.

I'll share what I test, learn and get wrong.
```
Visuel : capture de la heatmap du prototype, légende « prototype, not a product ».

**B** 💬
```
Rule I'm setting for Solen from day one:

Observation ≠ hypothesis ≠ result.

AI can suggest what to test. Only a controlled test says what worked.

AI proposes. Reality decides.
```
Visuel : carte texte avec « AI proposes. Reality decides. » sur fond sombre.

**C** 🎙
```
If you run a Shopify store: what was the last change you made to your product page, and how did you know if it worked?

Genuinely curious. Replies are my research this month.
```
Visuel : texte seul.

### Jour 2

**A** 🔍
```
Shopify friction worth testing #1:

On mobile, the add-to-cart button often sits below one or two screens of images.

Hypothesis: some visitors leave before reaching it.
Test: a higher or sticky CTA vs control.
Metric: mobile add-to-cart rate.
```
Visuel : wireframe d'un téléphone, flèche vers un bouton placé très bas.

**B** 🛠
```
What Solen's prototype does today:
– collects clicks and scroll depth
– draws heatmaps per device
– asks an LLM to read recent events and flag possible frictions

What it doesn't do: test anything. Yet.
```
Visuel : capture de la heatmap avec les calques clics et scroll.

**C** 📣
```
Free offer this week: send me your Shopify store link and I'll reply with 3 mobile frictions I'd test, with the reasoning.

No pitch. I'm learning how merchants decide what to change.
```
Visuel : texte seul.

### Jour 3

**A** 🛠
```
Sizing Solen's market, part 1:

2.87M live Shopify stores (Store Leads, July 2026). ~42% in North America.

That's the only number I'm confident in. Next: the two I'm guessing.
```
Visuel : slide 6 du deck (boutiques par région), exportée en image.

**B** 🛠
```
Sizing, part 2. The two numbers I'm guessing:

1. Share of Shopify stores with 10k+ visitors/month (I use 5–15%)
2. What they spend yearly on CRO, analytics and testing tools ($600–3,000)

If you have real data on either, I want it.
```
Visuel : slide 7 du deck (hypothèses), exportée en image.

**C** 🛠
```
Sizing, part 3. Result: a TAM between $86M and $1.29B, ~$430M in the middle.

A 15x range. That's what honest sizing looks like before you've talked to customers.
```
Visuel : slide 8 du deck (TAM / SAM / SOM).

### Jour 4

**A** 🔍
```
Shopify friction worth testing #2:

Shipping cost only revealed at checkout.

Hypothesis: the surprise causes drop-off between cart and payment.
Test: show the cost or free-shipping threshold on the product page.
Metric: cart-to-checkout rate.
```
Visuel : wireframe page produit → checkout, avec « $?? » entouré au checkout.

**B** 💬
```
Most small e-commerce teams don't lack data.

They lack the hours between "this looks off in GA4" and "we shipped a change and measured it".

That gap is what I'm researching.
```
Visuel : texte seul.

**C** 🎙
```
How I'm running merchant interviews:

I don't pitch. I ask one question: "Walk me through the last time you tried to improve conversion, step by step."

What people did beats what they say they'd do.
```
Visuel : carte texte avec la question entre guillemets.

### Jour 5

**A** 💬
```
Why I'm not building a dashboard:

Shopify stores already have GA4, Shopify Analytics, often a heatmap tool. Another screen of charts doesn't change what gets shipped.

The output I care about: a short list of changes worth testing.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #3:

Size or color picked from a dropdown that hides the options.

Hypothesis: shoppers hesitate or pick the wrong variant.
Test: visible swatches or buttons.
Metric: add-to-cart rate, size-related returns if tracked.
```
Visuel : wireframe avant / après (menu déroulant vs boutons).

**C** 📣
```
Looking for a technical cofounder.

Built: event tracking, per-device heatmaps, LLM friction analysis (Node, Supabase, Claude API).
Not built: multi-store, consent, experiments.

I bring strategy, CRO, data and go-to-market. DMs open.
```
Visuel : schéma d'architecture en 4 boîtes (script → API → base → analyse), Excalidraw.

### Jour 6

**A** 🎙
```
Interview question I rely on:

"Which tool did you stop paying for recently, and why?"

What people quit tells you more than what they say they want.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #4:

Reviews only at the bottom of the page.

Hypothesis: shoppers looking for reassurance don't reach them in time.
Test: star rating + review count next to the price.
Metric: add-to-cart rate.
```
Visuel : wireframe avec étoiles déplacées près du prix (flèche).

**C** 🛠
```
Honest status, week 1:
– prototype: runs
– customers: 0
– revenue: 0
– cofounder: not yet

Posting this because building in public only works if the zeros are public too.
```
Visuel : texte seul.

### Jour 7

**A** 💬
```
Most "AI CRO" pitches skip a step.

"Mobile users scroll less" is an observation.
"Move the CTA up" is a hypothesis.
"+X% conversion" needs a controlled test.

AI can shorten the path to a good hypothesis. Not the test.
```
Visuel : schéma en 4 cases : Observation → Hypothesis → Test → Result.

**B** 🛠
```
What I'm deliberately not doing yet:
– paid ads
– an app store listing
– automation that edits live stores

First: prove the problem hurts enough that someone pays to fix it.
```
Visuel : texte seul.

**C** 🎙
```
Question for Shopify founders:

When did you last run an A/B test, and what stopped you from running more?

No wrong answers. Not running any is useful data too.
```
Visuel : texte seul.

---

## Semaine 2

### Jour 8

**A** 🔍
```
Shopify friction worth testing #5:

Return policy buried in the footer.

Hypothesis: first-time buyers hesitate without it.
Test: one line near the buy button stating the actual policy.
Metric: conversion of new visitors.
```
Visuel : wireframe avec une ligne « Free returns · 30 days » sous le bouton.

**B** 🛠
```
Solen v0 architecture, no magic:

tracking script → Express API on Vercel → Supabase events table → heatmap + LLM analysis endpoints

Simple on purpose. The hard part isn't the stack, it's knowing what to recommend.
```
Visuel : le schéma d'architecture du jour 5.

**C** 🎙
```
Autonomy ladder I'm testing with merchants:
1. Flag problems
2. Draft changes, you approve
3. Run controlled tests
4. Deploy under strict rules

Where would you stop? Reply with a number.
```
Visuel : escalier à 4 marches numérotées (Excalidraw).

### Jour 9

**A** 🛠
```
Something I'm unsure about: the traffic threshold.

I use 10k visitors/month as a working filter for interviews. It's not a statistical rule.

Below what traffic does behavior analysis stop being useful? Open question.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #6:

Heavy product images that load slowly on mobile data.

Hypothesis: some visitors bounce before the page is usable.
Test: compressed images, lazy-load below the fold.
Metric: mobile bounce rate on product pages, load time.
```
Visuel : capture d'un test PageSpeed Insights sur une page de démo (pas une marque réelle).

**C** 💬
```
Things that should always stay human, in my view:
– prices
– promotions
– checkout
– legal copy
– core branding

Software can suggest. A person decides.
```
Visuel : texte seul.

### Jour 10

**A** 💬
```
I studied how Tally reportedly grew to millions in ARR, bootstrapped. Core loop: a "Made with Tally" badge every respondent sees.

That loop doesn't transfer to Solen. Optimization is invisible to shoppers. No badge possible.
```
Visuel : slide 16 du deck (transposition des leviers Tally).

**B** 💬
```
So what replaces a viral badge for an invisible product?

My bet: public audits. Each one shows the thinking, starts a conversation, and sometimes becomes an interview.

We'll see if the bet holds.
```
Visuel : texte seul.

**C** 🔍
```
Shopify friction worth testing #7:

A free-shipping threshold nobody sees until the cart.

Hypothesis: showing progress ("$12 away from free shipping") nudges order size.
Test: progress bar in the cart drawer vs none.
Metric: average order value.
```
Visuel : wireframe d'un tiroir panier avec barre de progression.

### Jour 11

**A** 🛠
```
Why Europe first for Solen, not the US:

The US has ~38% of live Shopify stores. But I'm a solo founder, French-speaking, zero budget.

Where I learn fastest beats where the market is biggest. For now.
```
Visuel : slide 13 du deck (priorisation des régions).

**B** 🔍
```
Shopify friction worth testing #8:

Size guide opens a new page or a PDF.

Hypothesis: shoppers leave the flow and don't come back.
Test: inline size guide in a drawer.
Metric: add-to-cart rate on apparel product pages.
```
Visuel : wireframe avant / après (lien externe vs tiroir).

**C** 📣
```
Pilot offer I'm testing:
4 weeks, weekly report of the frictions I'd prioritize, heatmaps per device, a weekly call.

In exchange: install a script, 30 min/week, honest feedback.

Free for the first 3 stores. No promised uplift.
```
Visuel : texte seul.

### Jour 12

**A** 🛠
```
Everything Solen recommends gets reviewed by me before a merchant sees it.

Not scalable. Intentional.

Every correction I make is a line in the spec of what the product needs to learn.
```
Visuel : texte seul.

**B** 💬
```
Uncomfortable truth: many small stores don't have enough traffic to A/B test every idea.

That's not a reason to stop testing. It's a reason to test fewer, bigger changes, with one primary metric.
```
Visuel : texte seul.

**C** 🔍
```
Shopify friction worth testing #9:

Email pop-up firing in the first seconds on mobile.

Hypothesis: it interrupts visitors before they see the product.
Test: trigger it on scroll depth or exit intent instead.
Metric: bounce rate, signups, conversion.
```
Visuel : wireframe téléphone entièrement couvert par un pop-up.

### Jour 13

**A** 🎙
```
What I ask instead of "would you pay for this?":
– What do you spend on tools today?
– On agencies or freelancers?
– How many hours a week go into this?

Current cost is a better signal than hypothetical willingness.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #10:

No delivery estimate on the product page.

Hypothesis: shoppers buying for a date (gifts, events) hesitate.
Test: "Order today, arrives by Friday" near the CTA.
Metric: conversion, especially before holidays.
```
Visuel : wireframe avec la ligne de date de livraison sous le bouton.

**C** 💬
```
Warning for anyone testing in November:

Conversion jumps around Black Friday for reasons that have nothing to do with your changes.

Don't read a before/after comparison from this period as a test result.
```
Visuel : texte seul.

### Jour 14

**A** 🛠
```
How I describe Solen in one line right now:

It helps Shopify stores decide what to test first, and why.

Smaller claim than "AI optimization". Easier to prove or disprove.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #11:

Site search returning nothing for common typos or synonyms.

Hypothesis: searchers are high-intent, and a zero-result page loses them.
Test: synonyms + suggested products on empty results.
Metric: search exit rate.
```
Visuel : wireframe « 0 results » vs « Did you mean… ».

**C** 🎙
```
Shopify founders: what's the one metric you check every morning?

Asking because I'm deciding what Solen's weekly report should lead with.
```
Visuel : texte seul.

---

## Semaine 3

### Jour 15

**A** 🛠
```
What the prototype gets wrong today, openly:
– it can't separate data from multiple stores
– it reads only the last 500 events
– it can't tell correlation from cause

Fixing the first is required before any pilot.
```
Visuel : capture de la réponse brute de l'analyse du prototype.

**B** 🔍
```
Shopify friction worth testing #12:

Cart drawer with the checkout button below the upsells.

Hypothesis: shoppers ready to pay have to scroll to find it.
Test: checkout button pinned in view.
Metric: cart-to-checkout rate.
```
Visuel : wireframe d'un tiroir panier avec le bouton hors écran.

**C** 📣
```
Still looking for a technical cofounder.

The interesting technical problems: event pipelines, per-store learning, LLM reasoning over behavior data, and experiment design with guardrails.

If that's your kind of problem, DM me.
```
Visuel : texte seul.

### Jour 16

**A** 💬
```
My market sizing has one solid number and two guesses. I published it anyway.

A wrong number in public gets corrected faster than a right-looking one in a private deck.
```
Visuel : slide 7 du deck (hypothèses marquées « à vérifier »).

**B** 🔍
```
Shopify friction worth testing #13:

Product description as one long block of text.

Hypothesis: shoppers scan and miss key info (materials, fit, care).
Test: 3–5 scannable bullets above the long copy.
Metric: add-to-cart rate.
```
Visuel : wireframe bloc de texte vs 4 puces.

**C** 📣
```
Interview ask: I'm talking to Shopify founders and e-commerce leads for 20 minutes.

No pitch. I want to understand how you decide what to change on your store.

Reply or DM if you're open to it.
```
Visuel : texte seul.

### Jour 17

**A** 💬
```
Some bet on rebuilding e-commerce from scratch around AI.

I'm betting on the opposite: most merchants won't migrate. They want their current store to get better.

Both bets can be right for different merchants. Mine is still unproven.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #14:

Out-of-stock variants shown as selectable, then failing at add-to-cart.

Hypothesis: frustration and exits.
Test: grey out unavailable variants + "notify me".
Metric: product page exits, back-in-stock signups.
```
Visuel : wireframe de variantes dont une grisée.

**C** 💬
```
Guardrails any automated optimization should have:
– a control group
– one primary metric + secondary checks
– a stop rule
– instant rollback
– human sign-off for sensitive changes

Without these, "autopilot" is just risk.
```
Visuel : liste en carte texte, une icône par ligne.

### Jour 18

**A** 🛠
```
Why the first pilots will be done by hand:

I'd rather learn what merchants actually use in a report than build the wrong automation fast.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #15:

Homepage hero with a brand slogan but no clear path to products.

Hypothesis: new visitors don't know where to click.
Test: one clear CTA to the best-selling collection.
Metric: clicks from homepage to collections or products.
```
Visuel : wireframe de page d'accueil avec et sans bouton.

**C** 🎙
```
Question for CRO people:

What's the most overrated "best practice" you've seen fail in a real test?

Collecting these. Good reminder that patterns are hypotheses.
```
Visuel : texte seul.

### Jour 19

**A** 🛠
```
Pricing hypothesis I'll test with pilots: ~€190/month.

Not based on data yet. Based on: cheaper than an agency, more than a free heatmap tool.

Pilots will tell me if it's too high, too low, or the wrong model.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #16:

Payment options (PayPal, Apple Pay, Klarna) only visible at checkout.

Hypothesis: shoppers unsure their method is accepted hesitate earlier.
Test: payment icons near the price or CTA.
Metric: add-to-cart, checkout starts.
```
Visuel : wireframe avec une ligne d'icônes de paiement sous le bouton.

**C** 💬
```
What building in public means for me:
– publish the zeros
– publish the guesses as guesses
– publish what the prototype gets wrong

What I won't publish: any merchant data without explicit consent.
```
Visuel : texte seul.

### Jour 20

**A** 🔍
```
Shopify friction worth testing #17:

Product images that can't be zoomed on mobile, or give no sense of scale.

Hypothesis: shoppers can't judge size or texture.
Test: pinch-zoom + one photo with the product in hand.
Metric: add-to-cart rate.
```
Visuel : wireframe de galerie avec une photo « en main ».

**B** 💬
```
Heatmaps show where people click. They don't show why.

That "why" is a hypothesis. It only becomes knowledge when you test it.
```
Visuel : capture de la heatmap du prototype.

**C** 📣
```
Open offer, still running: send me your Shopify store link, get 3 mobile frictions I'd test, with the reasoning.

I only publish an audit with your explicit OK.
```
Visuel : texte seul.

### Jour 21

**A** 🛠
```
Three weeks of posting about a product with 0 paying customers.

What I track: audit requests, interviews booked, pilot conversations, cofounder DMs.

Not followers. Followers don't tell me if the problem is real.
```
Visuel : capture du tableau de suivi (colonnes vides ou remplies, selon l'état réel).

**B** 🔍
```
Shopify friction worth testing #18:

Mobile menu with 15+ top-level items.

Hypothesis: choice overload, visitors fall back to scrolling or leave.
Test: 5–7 top categories + prominent search.
Metric: menu clicks to collections, exits.
```
Visuel : wireframe de menu long vs menu court.

**C** 🎙
```
Interview question I find most revealing:

"What did you try that you abandoned?"

Abandoned tools, spreadsheets, agencies. That's where the real pain and the budget history live.
```
Visuel : texte seul.

---

## Semaine 4

### Jour 22

**A** 🛠
```
The learning-loop idea behind Solen, stated as a hypothesis:

context → behavior → friction → hypothesis → change → result

If each result is stored that way, later recommendations might improve. Might. Unproven.
```
Visuel : boucle en 6 étapes (Excalidraw).

**B** 🔍
```
Shopify friction worth testing #19:

Cookie banner covering half the mobile screen, CTA included.

Hypothesis: visitors bounce before seeing the product.
Test: a compact banner that still meets consent rules.
Metric: bounce rate, consent rate.
```
Visuel : wireframe téléphone à moitié couvert par la bannière.

**C** 🛠
```
Solo founder math: every hour on code is an hour not talking to merchants.

My rule for this phase: max half a day per week on product. The rest is interviews, audits and pilots.
```
Visuel : texte seul.

### Jour 23

**A** 💬
```
"Best practices" are other people's hypotheses that worked in their context.

A sticky CTA that helped one store can hurt another. That's why I write "I'd test", never "you should".
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #20:

Cross-sell carousel placed above the add-to-cart button.

Hypothesis: it distracts from the main decision.
Test: move it below the CTA or into the cart.
Metric: add-to-cart rate, average order value.
```
Visuel : wireframe avant / après (carrousel au-dessus vs en dessous du bouton).

**C** 🎙
```
If you work at a Shopify agency or do CRO freelance:

Would a tool that drafts friction analyses help your capacity, or threaten your billable hours?

Honest answers wanted. This decides a whole channel for me.
```
Visuel : texte seul.

### Jour 24

**A** 🛠
```
What a Solen pilot report looks like (structure only):

For each friction:
observation → hypothesis → change to test → metric to watch

There's no "expected uplift" field. On purpose.
```
Visuel : modèle de rapport vide (tableau à 4 colonnes).

**B** 🔍
```
Shopify friction worth testing #21:

No product video where motion matters (fit, texture, how it works).

Hypothesis: photos alone leave doubts.
Test: a short 10–15s video in the gallery.
Metric: add-to-cart rate, via a randomized test.
```
Visuel : wireframe de galerie avec une vignette vidéo.

**C** 💬
```
Consent isn't a later problem for Solen.

The tracking script has to respect consent before the first pilot, not after.

Europe-first makes that non-negotiable. I think that's a good thing.
```
Visuel : texte seul.

### Jour 25

**A** 💬
```
A claim you'll often hear: "Visitors who watch the video convert 2x more."

Maybe the video helps. Or motivated buyers are the ones who watch videos.

Only showing it to a random half separates the two.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #22:

The same pre-purchase questions answered only by email or chat.

Hypothesis: shoppers leave instead of asking.
Test: 4–5 FAQ items on the product page (shipping, returns, sizing, care).
Metric: conversion, tickets per order.
```
Visuel : wireframe avec un accordéon FAQ sous le bouton.

**C** 📣
```
Cofounder search, honest version:

What exists: a prototype, a market sizing, a 90-day validation plan, CRO expertise.
What doesn't: customers, revenue, funding.

Looking for someone who likes that stage. DMs open.
```
Visuel : texte seul.

### Jour 26

**A** 🛠
```
The question I use to pick Solen's first customers:

Who feels this problem most strongly, most often, at the highest cost, and already has budget or clear intent to change?

Not "who likes the idea".
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #23:

Reviews without photos, for products where appearance matters.

Hypothesis: customer photos answer "what does it really look like?"
Test: surface photo reviews first.
Metric: add-to-cart rate.
```
Visuel : wireframe d'avis avec et sans photo.

**C** 🎙
```
What would make you trust a recommendation from software about your store?

For me: show the observed data, label the guess as a guess, say how to test it.

What would it be for you?
```
Visuel : texte seul.

### Jour 27

**A** 🛠
```
Kill criteria I set before starting, so I can't move the goalposts:
– no concrete pain stories in interviews → change segment
– pilots act on no recommendation → rethink the product
– zero paying pilots after 90 days → back to research
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #24:

Mobile collection page with filters hidden behind an unlabeled icon.

Hypothesis: visitors don't find them and scroll endlessly.
Test: a visible "Filter & sort" button.
Metric: filter usage, clicks to product pages.
```
Visuel : wireframe icône seule vs bouton libellé.

**C** 📣
```
Pilot spots open for Shopify stores with 20k+ visitors/month.

4 weeks, weekly friction report, heatmaps per device, a weekly call. Free. No promised uplift.

DM me.
```
Visuel : modèle de rapport vide du jour 24.

### Jour 28

**A** 💬
```
"We know what to fix, we just never get to it" is a different problem from "we don't know what to fix".

Solen v1 only helps with the second. If most merchants have the first, I need to know soon.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #25:

Forced account creation before checkout.

Hypothesis: first-time buyers abandon at the signup wall.
Test: guest checkout, account offer after purchase.
Metric: checkout completion rate.
```
Visuel : wireframe d'un écran « Create account to continue ».

**C** 🛠
```
Reminder to myself at the end of month one:

The goal isn't an audience. It's 3 pilots, honest interview notes, and one clear decision about what to build next.
```
Visuel : texte seul.

### Jour 29

**A** 🛠
```
What I'd build first if pilots confirm the problem:
1. multi-store data separation
2. consent-aware tracking
3. a weekly report generated, then reviewed by me

Not: autopilot, dashboards, an app store listing.
```
Visuel : texte seul.

**B** 🔍
```
Shopify friction worth testing #26:

No visible contact details or company info on a newer brand's store.

Hypothesis: first-time visitors wonder if it's legit.
Test: contact, address and returns info in footer and product page.
Metric: new-visitor conversion.
```
Visuel : wireframe de pied de page vide vs complet.

**C** 💬
```
Every store has more ideas to test than capacity to test them.

The real skill isn't generating ideas. It's ranking them by impact, confidence and effort.

That ranking is what I want Solen to get good at.
```
Visuel : grille à 3 colonnes (Impact, Confidence, Effort), Excalidraw.

### Jour 30

**A** 💬
```
30 days of posting about Solen. What stays the same:

Observation ≠ hypothesis ≠ result.
No promised uplifts.
Zeros published alongside the wins.

AI proposes. Reality decides.
```
Visuel : la carte texte du jour 1.

**B** 🔍
```
Shopify friction worth testing #27:

A prominent discount-code field at checkout.

Hypothesis: shoppers without a code leave to search for one.
Test: collapse it behind a small "Have a code?" link.
Metric: checkout completion rate.
```
Visuel : wireframe avant / après du champ code promo.

**C** 📣
```
If you've read along this month: thank you.

The most useful thing you can do for Solen hasn't changed: 20 minutes telling me how you decide what to change on your store.

DMs open.
```
Visuel : texte seul.
