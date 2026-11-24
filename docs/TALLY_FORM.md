# Formulaire Tally de Solen

> Généré depuis `tools/x-calendar/tally_form.py`. Une section = une page Tally. Structure inspirée du modèle Tally « B2B SaaS Research Report », réécrite pour Solen.
> Pas de question « combien paieriez-vous » : on demande ce que les gens dépensent déjà.

## Page 1 · Intro

**Logique :** « Oui, je parle français » → page FR. « No, continue in English » → page 2.

```
Help me build Solen

I'm Thomas, building Solen. Before I build more, I want to understand how Shopify stores actually decide what to change.

4 minutes, 3 short parts:
1. You and your store
2. How you improve it today
3. Where AI fits, or doesn't

No pitch, nothing to buy. Leave your email at the end and you'll get the full report in January.

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

3. Store URL (optional, never shared)
```

## Page 3A · How you improve your store today

**Logique :** « I tried and stopped » → affiche la question 6b. Fin de page → page 4.

```
How you improve your store today

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

8. Hours a month spent on this (one choice)
- 0
- Under 2
- 2 to 5
- 5 to 10
- 10+

9. Monthly spend on it, tools and people, € or $ (one choice)
- 0
- Under 50
- 50 to 200
- 200 to 1,000
- 1,000+
- Rather not say

10. What's hardest right now? (one choice)
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
- Mostly recommendations
```

## Page 4 · Where AI fits

**Logique :** Tout le monde passe par cette page.

```
Where AI fits, or doesn't

11. If software spotted a problem on a store, how far would you let it go? (one choice)
- Just flag it
- Draft the fix, I approve it
- Test it on part of the traffic
- Ship winning changes on its own, within rules I set

12. What would make you trust an AI recommendation about a store? (several)
- Seeing the data behind it
- A confidence level
- Testing it before it goes live
- Results from similar stores
- A one-click undo
- Nothing would

13. Have you used AI (ChatGPT, Shopify Sidekick...) to decide what to change on a store? (one choice)
- Yes, regularly
- I tried it
- Never
```

## Page 5 · Get the report (optional)

**Logique :** Dernière page de questions, tout est facultatif.

```
Get the report

Optional. Leave your email and you'll get the full report in January.

14. Email (optional)

15. If your store could fix one thing on its own every week, what would it be? (long answer, optional)

16. You can email me 2 or 3 follow-up questions (checkbox, optional)
```

## Page de fin · Merci

**Logique :** Page « Thank you » de Tally.

```
Thanks, that really helps.

The report lands in January. If you'd rather talk, 20 minutes here: [lien Cal.com]
```
