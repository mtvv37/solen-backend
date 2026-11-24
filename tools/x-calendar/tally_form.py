"""Le formulaire Tally de Solen, page par page, prêt à recopier.

Structure inspirée du modèle Tally « B2B SaaS Research Report » (intro en 3 étapes, sections par profil,
une section sur l'avenir, une fin facultative avec email), réécrite pour Solen.
Règles : questions sur ce que les gens ont fait, pas sur ce qu'ils feraient ; aucune question
« combien paieriez-vous » (on demande ce qu'ils dépensent déjà) ; pas d'emoji ; options en tiret simple.
"""

PAGES = [
 dict(title="Page 1 · Intro", logic="« Oui, je parle français » → page FR. « No, continue in English » → page 2. Le schéma : un bloc image de Tally (taper /image).",
      images=["img/form-compare.png"], text="""Help me uncover how Shopify stores decide what to change in 2026

I'm gathering answers from people who run, grow or build for Shopify stores, to see how changes really get decided: what gets tested, what gets guessed, and what quietly gets dropped.

It takes about 4 minutes, in 3 simple steps:
1. Share how you decide what to change today, on your store or your clients'
2. Tell me what gets in the way
3. Say how far you'd let AI go, and what it would take to trust it

Your answers will shape a short report on how Shopify stores improve conversion. Leave your email at the end and you'll get it in January. Nothing to buy, no sales follow-up.

Thanks for taking the time.

Why I'm asking
I'm Thomas, and I'm building Solen, an AI tool for Shopify stores. Most stores already have the data: Shopify Analytics, GA4, heatmaps. What's missing is the step between "this looks off" and "we changed it, and it worked". Solen tries to do that step for you.

How it works today
- you add a small script to your store
- it records how visitors click and scroll, page by page, on mobile and desktop
- it spots where they drop off or get stuck
- it proposes a fix, with how sure it is. The less data it has, the lower that number goes, on purpose.
- you can ask it questions in plain English, like "why are mobile visitors leaving my product page?"

Where it's going
You set a confidence threshold. Above it, Solen applies the fix itself, tests it on part of your traffic, measures it, and rolls it back if it hurts. Below it, it asks you first. Prices, promos and checkout always wait for you. Every result is kept, so later suggestions can learn from earlier ones. Finer segments come next too: new visitors, people coming from Instagram, and so on.

What it isn't: another dashboard. The goal is one clear next step, not more charts.

[Image: with-vs-without-solen.png]

Before I build more, I need to know how stores really work today. That's what this form is for.

Would you rather do a 20-minute call in French? (one choice, required)
- Oui, je parle français
- No, continue in English"""),

 dict(title="Page FR · Appel", logic="Fin du formulaire après cette page.", text="""Top, on s'appelle

Réserve 20 minutes ici : [lien Cal.com]
Pas de pitch. Je veux comprendre comment tu décides quoi changer sur ta boutique.

Prénom (court)
Lien de ta boutique (court)
Email, pour t'envoyer le rapport en janvier (email)"""),

 dict(title="Page 2 · You and your store", logic="« Shopify app developer » → page 3B. Tout le reste → page 3A.", text="""You and your store

1. What's your role? (one choice, required)
- Founder or owner
- E-commerce or growth manager
- Agency or freelancer
- Shopify app developer
- Other

2. Roughly how many visitors a month? Your store, or your typical client's. (one choice)
- Under 5k
- 5k to 10k
- 10k to 50k
- 50k to 200k
- 200k+
- Not sure

3. Store URL (optional, never shared)"""),

 dict(title="Page 3A · How you improve your store today", logic="« I tried and stopped » → affiche la question 6b. Si la 7 contient « None », masque la 8. La 8 : bloc « Linear scale » de Tally, 1 à 5, libellés Not at all / Extremely well, l'exemple en description. Fin de page → page 4.", text="""How you improve your store today

4. Tell me about the last change you made to improve conversion. What did you notice, what did you change, and did it work? (long answer, required)

5. How do you usually decide what to change? (several)
- Analytics (Shopify, GA4)
- Heatmaps or session recordings
- Reviews, support tickets, customer feedback
- What other stores do
- An agency or freelancer
- A/B test results
- Gut feeling

6. Do you run A/B tests? (one choice)
- Regularly
- I tried and stopped
- Never

6b. What made you stop? (short answer)

7. Which of these do you use? (several)
- Shopify Analytics
- Google Analytics
- Heatmaps (Hotjar, Clarity...)
- An A/B testing app (Shoplift, Intelligems, VWO...)
- An agency or freelancer
- None

8. How well do these tools help you decide what to change on your store? (linear scale 1 to 5: 1 = Not at all, 5 = Extremely well)
Example: "My heatmap showed most mobile visitors never reached Add to cart, so I moved it up" (extremely well) vs. "I open Google Analytics once a month and don't really act on it" (not at all).

9. Hours a month spent on this (one choice)
- 0
- Under 2
- 2 to 5
- 5 to 10
- 10+

10. Monthly spend on it, tools and people, € or $ (one choice)
- 0
- Under 50
- 50 to 200
- 200 to 1,000
- 1,000+
- Rather not say

11. What's hardest right now? (one choice)
- Knowing what to change
- Finding the time or people to do it
- Knowing if a change worked
- Not enough traffic to test
- Nothing, conversion isn't a priority"""),

 dict(title="Page 3B · The app you're building", logic="Seulement pour « Shopify app developer ». Fin de page → page 4.", text="""The app you're building

4. What does your app do, in one line? (short answer)

5. Active installs (one choice)
- Under 100
- 100 to 1,000
- 1,000 to 10,000
- 10,000+

6. Do merchants ask you for analytics or recommendations inside your app? (one choice)
- Often
- Sometimes
- Never

7. When they do, what do they ask for? (several)
- Reports and dashboards
- Benchmarks against similar stores
- What to do next
- Alerts when something drops
- A/B testing
- Other

8. Does your app show merchants what to change, or only what happened? (one choice)
- Only what happened
- Some recommendations
- Mostly recommendations"""),

 dict(title="Page 4 · Where AI fits", logic="Tout le monde passe par cette page.", text="""Where AI fits, or doesn't

12. If software spotted a problem on a store, how far would you let it go? (one choice)
- Just flag it
- Draft the fix, I approve it
- Test it on part of the traffic
- Ship winning changes on its own, within rules I set

13. What would make you trust an AI recommendation about a store? (several)
- Seeing the data behind it
- A confidence level
- Testing it before it goes live
- Results from similar stores
- A one-click undo
- Nothing would

14. Have you used AI (ChatGPT, Shopify Sidekick...) to decide what to change on a store? (one choice)
- Yes, regularly
- I tried it
- Never"""),

 dict(title="Page 5 · Get the report (optional)", logic="Dernière page de questions, tout est facultatif.", text="""Get the report

Optional. Leave your email and you'll get the full report in January.

15. Email (optional)

16. If your store could fix one thing on its own every week, what would it be? (long answer, optional)

17. You can email me 2 or 3 follow-up questions (checkbox, optional)"""),

 dict(title="Page de fin · Merci", logic="Page « Thank you » de Tally.", text="""Thanks, that really helps.

The report lands in January. If you'd rather talk, 20 minutes here: [lien Cal.com]"""),
]

if __name__ == '__main__':
    import re
    for p in PAGES:
        assert '·' not in p['text'] and '–' not in p['text'] and '—' not in p['text'], p['title']
        assert not re.search('[\U0001F000-\U0001FFFF☀-➿]', p['text']), p['title']
    qs = [l for p in PAGES for l in p['text'].split('\n') if re.match(r'^\d+b?\. ', l)]
    print(len(PAGES), 'pages ;', len(qs), 'questions numérotées')
    print('intro :', len(PAGES[0]['text']), 'caractères')
