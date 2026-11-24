# Formulaire Tally de Solen

> Généré depuis `tools/x-calendar/tally_form.py`. Une section = une page Tally. Structure inspirée du modèle Tally « B2B SaaS Research Report », réécrite pour Solen.
> Pas de question « combien paieriez-vous » : on demande ce que les gens dépensent déjà.
> Schéma de l'intro : `design/social/form/with-vs-without-solen.png` (bloc image de Tally). L'intro sépare ce que Solen fait aujourd'hui de ce qui vient ensuite.

## Page 1 · Intro

**Logique :** « Oui, je parle français » → page FR. « No, continue in English » → page 2. Le schéma : un bloc image de Tally (taper /image).

```
Help me uncover how Shopify stores decide what to change in 2026

I'm gathering answers from people who run, grow or build for Shopify stores, to see how changes really get decided: what gets tested, what gets guessed, and what quietly gets dropped.

It takes about 4 minutes, in 3 simple steps:
1. Share how you decide what to change today, on your store or your clients'
2. Tell me what gets in the way
3. Say how far you'd let AI go, and what it would take to trust it

After that, an optional part goes deeper, about 4 more minutes. It's the part that helps me most.

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
- No, continue in English
```

## Page FR · Appel

**Logique :** Fin du formulaire après cette page.

```
Top, on s'appelle

Réserve 20 minutes ici : [lien Cal.com]
Pas de pitch. Je veux comprendre comment tu décides quoi changer sur ta boutique.

Prénom (court)
Lien de ta boutique (court)
Email, pour t'envoyer le rapport en janvier (email)
```

## Page 2 · You and your store

**Logique :** « Shopify app developer » → page 3B. Tout le reste → page 3A.

```
You and your store

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

3. What do you sell? Your store, or most of your clients'. (one choice)
- Fashion and apparel
- Beauty and skincare
- Food, drinks and supplements
- Sports and fitness
- Home and living
- Electronics and gadgets
- Other

4. Store URL (optional, never shared)
```

## Page 3A · How you improve your store today

**Logique :** « I tried and stopped » → affiche la 7b. Si la 8 contient « None », masque la 9. La 9 : bloc « Linear scale » de Tally, 1 à 5, libellés Not at all / Extremely well, l'exemple en description. Fin de page → page 4.

```
How you improve your store today

5. Tell me about the last change you made to improve conversion. What did you notice, what did you change, and did it work? (long answer, required)

6. How do you usually decide what to change? (several)
- Analytics (Shopify, GA4)
- Heatmaps or session recordings
- Reviews, support tickets, customer feedback
- What other stores do
- An agency or freelancer
- A/B test results
- Gut feeling

7. Do you run A/B tests? (one choice)
- Regularly
- I tried and stopped
- Never

7b. What made you stop? (short answer)

8. Which of these do you use? (several)
- Shopify Analytics
- Google Analytics
- Heatmaps (Hotjar, Clarity...)
- An A/B testing app (Shoplift, Intelligems, VWO...)
- An agency or freelancer
- None

9. How well do these tools help you decide what to change on your store? (linear scale 1 to 5: 1 = Not at all, 5 = Extremely well)
Example: "My heatmap showed most mobile visitors never reached Add to cart, so I moved it up" (extremely well) vs. "I open Google Analytics once a month and don't really act on it" (not at all).

10. Hours a month spent on this (one choice)
- 0
- Under 2
- 2 to 5
- 5 to 10
- 10+

11. Monthly spend on it, tools and people, € or $ (one choice)
- 0
- Under 50
- 50 to 200
- 200 to 1,000
- 1,000+
- Rather not say

12. What's hardest right now? (one choice)
- Knowing what to change
- Finding the time or people to do it
- Knowing if a change worked
- Not enough traffic to test
- Nothing, conversion isn't a priority
```

## Page 3B · The app you're building

**Logique :** Seulement pour « Shopify app developer ». Fin de page → page 4.

```
The app you're building

5. What does your app do, in one line? (short answer)

6. Active installs (one choice)
- Under 100
- 100 to 1,000
- 1,000 to 10,000
- 10,000+

7. Do merchants ask you for analytics or recommendations inside your app? (one choice)
- Often
- Sometimes
- Never

8. When they do, what do they ask for? (several)
- Reports and dashboards
- Benchmarks against similar stores
- What to do next
- Alerts when something drops
- A/B testing
- Other

9. Does your app show merchants what to change, or only what happened? (one choice)
- Only what happened
- Some recommendations
- Mostly recommendations
```

## Page 4 · Where AI fits

**Logique :** Tout le monde passe par cette page. La 15b s'affiche si la 15 = « Yes, regularly » ou « I tried it ». La 17 : « Yes, go deeper » → page 5A, ou 5B si la 1 = « Shopify app developer ». « No, take me to the end » → page 6.

```
Where AI fits, or doesn't

13. If software spotted a problem on a store, how far would you let it go? (one choice)
- Just flag it
- Draft the fix, I approve it
- Test it on part of the traffic
- Ship winning changes on its own, within rules I set

14. What would make you trust an AI recommendation about a store? (several)
- Seeing the data behind it
- A confidence level
- Testing it before it goes live
- Results from similar stores
- A one-click undo
- Nothing would

15. Have you used AI (ChatGPT, Shopify Sidekick...) to decide what to change on a store? (one choice)
- Yes, regularly
- I tried it
- Never

15b. What did you ask it, and did you act on the answer? (short answer)

16. Which of these would you never let software change on its own, even if it tested it first? (several)
- Prices
- Discounts and promos
- Checkout
- Product titles and descriptions
- Product photos
- Page layout and section order
- Shipping and returns info
- Brand look (logo, colours, fonts)
- None, as long as it's tested and I can undo it

17. Got 4 more minutes? The next part goes deeper, and it's the part that helps me most. (one choice, required)
- Yes, go deeper
- No, take me to the end
```

## Page 5A · Go deeper: your store (optional)

**Logique :** Seulement si « Yes, go deeper » et rôle ≠ « Shopify app developer ». Tout est facultatif. La 28b s'affiche si la 28 commence par « Yes ». Fin de page → page 6.

```
Go deeper: your store

Thanks for staying. Everything here is optional, skip anything you'd rather not answer.

18. How often do you change something on the store to improve conversion? (one choice)
- Every week
- Every month
- A few times a year
- Almost never

19. Do you know your store's conversion rate, roughly? (one choice)
- Under 1%
- 1 to 2%
- 2 to 3%
- Over 3%
- I don't track it

20. Roughly what share of your visitors are on mobile? (one choice)
- Under 50%
- 50 to 70%
- 70 to 85%
- Over 85%
- Not sure

21. Where does most of your traffic come from? (one choice)
- Paid social (Meta, TikTok...)
- Google Ads
- Google search, unpaid
- Social media, unpaid
- Email and SMS
- Influencers or affiliates
- Not sure

22. Who makes the call on changes to the store? (one choice)
- Me, alone
- Me, with a small team
- A growth or marketing team
- Our agency
- Depends on the change

23. Do you look at results separately for mobile and desktop, or for new and returning visitors? (one choice)
- Yes, always
- Sometimes
- No, one number for everything

24. Where do you keep track of what you changed and how it went? (one choice)
- Nowhere, honestly
- In my head
- A doc or spreadsheet
- A project tool (Notion, Trello...)
- Our A/B testing app
- Our agency keeps it

25. Has a change ever hurt your sales without you noticing right away? What happened, and how did you find out? (long answer)

26. Which apps or services do you pay for today to sell more? Reviews, upsells, bundles, quizzes, testing, an agency... (short answer)

27. In the last 12 months, did you stop paying for an analytics, testing or conversion tool? Which one, and why? (short answer)

28. Have you ever paid for a conversion audit or a CRO agency? (one choice)
- Yes, and it was worth it
- Yes, and it wasn't
- No

28b. What made it worth it, or not? (short answer)

29. If you could ask your store's data one question and get a straight answer, what would you ask? (long answer)
```

## Page 5B · Go deeper: your app (optional)

**Logique :** Seulement si « Yes, go deeper » et rôle = « Shopify app developer ». Tout est facultatif. Fin de page → page 6.

```
Go deeper: your app

Thanks for staying. Everything here is optional, skip anything you'd rather not answer.

18. What category is your app in? (one choice)
- Conversion and upsells
- Reviews and social proof
- Analytics and reporting
- Marketing, email and SMS
- Store design and page builders
- Operations and shipping
- Other

19. How do you charge? (one choice)
- Free
- Freemium
- Paid plans only
- Usage-based
- A mix

20. How do merchants find out whether your app actually helped them? (several)
- A report inside the app
- They check Shopify Analytics themselves
- We send them results
- They don't really know

21. What's the most common reason merchants uninstall your app? (short answer)

22. Have you tried adding recommendations to your app, the "do this next" kind? What happened? (long answer)
```

## Page 6 · Get the report (optional)

**Logique :** Dernière page de questions, tout est facultatif.

```
Get the report

Optional. Leave your email and you'll get the full report in January.

30. Email (optional)

31. If your store could fix one thing on its own every week, what would it be? (long answer, optional)

32. You can email me 2 or 3 follow-up questions (checkbox, optional)
```

## Page de fin · Merci

**Logique :** Page « Thank you » de Tally.

```
Thanks, that really helps.

The report lands in January. If you'd rather talk, 20 minutes here: [lien Cal.com]
```
