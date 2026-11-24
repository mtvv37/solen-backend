"""Posts « Worth stealing » écrits à partir des captures de Thomas (format long, X Premium).

Une capture = un post, dans l'ordre de publication à 13h, à partir du 24 novembre.
`shot` = nom du fichier de la capture, publié à côté de la page (les captures restent hors du repo) ;
`new:...` = capture reçue sans fichier : le texte est prêt, Thomas a l'image.
Règles : anglais, 900 caractères maximum, puces en tiret simple « - », ton humain, pas de tiret long ni d'emoji,
on ne décrit que ce qui est visible, aucun résultat de marque inventé. Finit par « Follow for more. »
"""

WS = [
 dict(brand="Gymshark", shot="9.webp", text="""Worth stealing #1: Gymshark's discount badge.

Tiny label above the product name: "-30% | €12 saved".

What I like:
- you read the deal before the product
- same discount, said twice: percent and euros
- old price (€40) right next to the new one (€28), zero math

And the order isn't random. On a €40 item, 30% sounds bigger than €12. That's the rule of 100: under 100, lead with the percent. Over 100, lead with the money.

What I'd test: flip it on anything over €100. "€45 saved | -30%" instead of "-30% | €45 saved".

I'd watch add-to-cart on discounted items, split by price band.

Follow for more."""),

 dict(brand="Arntreal", shot="39.png", text="""Worth stealing #2: Arntreal's Black Friday draw.

On the product page: every order = 1 entry to win a Rolex, an Omega Speedmaster or a Cartier Santos. Rules linked right under it.

Why I think it's clever:
- the brand sells "everything of a luxury bag, except the price". The prize is the actual luxury logo. Same story.
- a discount eats margin on every order. Three watches are a fixed cost, cheaper per order the more you sell.
- the €149.90 price doesn't move, so it's still believable in January

What I'd test: "each order" rewards splitting your basket. Two orders of one bag = 2 entries, one order of two bags = 1. Fincut runs a similar draw but gives a ticket per item bought. I'd try 1 entry per bag.

I'd watch items per order during the draw.

Follow for more."""),

 dict(brand="Based", shot="30.png", text="""Worth stealing #3: Based's Black Friday button.

The main button doesn't say "Add to cart". It says "Buy one get one €21.95", in gold.

- the offer lives where everyone looks right before deciding
- same price as one, so "get one free" needs no math
- the banner underneath repeats it, and a 60-day guarantee closes the page

They didn't add a promo block next to the product. They changed the action itself.

What I'd test, for European shoppers:
- prices are in euros but the free shipping thresholds are in dollars ($50+, $100+). One currency please.
- "2.5 g" next to €21.95 looks tiny. "Lasts about X weeks" would answer that, if they know the number.

I'd watch conversion on EU traffic and reviews that mention "small".

Follow for more."""),

 dict(brand="Arntreal", shot="41.png", text="""Worth stealing #4: Arntreal's empty slot.

Black Friday offer: buy 1 bag, get the 2nd free, any colour. Next to the bag you picked there's a greyed-out bag with a "+" on it. "Choose your free bag."

Based put its BOGO in the button (#3). Arntreal draws it.

That empty slot is a task half done. You've picked one, a space is waiting. People push harder toward a goal they feel they've already started (Nunes and Drèze called it the endowed progress effect).

One thing bugs me: the offer shows €149.90 crossed out next to €149.90. No visible saving at all.

What I'd test: €299.80 crossed out, or "2 bags for €149.90, €74.95 each". And once the free colour is picked, "€149.90 saved" in green.

I'd watch how many orders take the 2-bag offer.

Follow for more."""),

 dict(brand="Based", shot="new:based-cart", text="""Worth stealing #5: Based's cart.

During the BOGO the cart turns into a game. "Your haul. 1 pick, 0 free." A progress bar, a dashed slot marked FREE next to your item, and "BOGO savings €0.00" in gold. A zero you kind of want to fix.

"Haul" and "picks" is unboxing-video talk. The cart speaks like the people buying.

There's also a cap, "€277 max per order". A limit makes a deal feel precious.

But the biggest number in the cart is "€255.76 left". A budget nobody planned. The bar measures the distance to the cap, not to the next reward.

What I'd test: make the next step the headline. "Pick 1 more, it's free." Cap in small print.

I'd watch the share of carts with 2+ picks.

Follow for more."""),

 dict(brand="DJI", shot="33.png", text="""Worth stealing #6: DJI's Black Friday, without a discount.

A €1,599 drone bundle and the price doesn't move. Instead: a free DJI Pro backpack tagged "Gift", and 5x more DJI credit on your purchase.

Why it's smart:
- no price cut = no new reference price. €1,599 stays believable after November.
- credit only works at DJI, so it brings you back for batteries, filters, the next drone
- the gift is something you can picture, listed before the specs

What I'd test: put the credit in euros. If the base is the 1% shown above, 5x is about €80 on this bundle. "5x" sounds clever. "€80 back" is money you're already spending in your head. Over 100, the money beats the ratio (rule of 100, see #1).

I'd watch conversion during the promo and how much credit gets used within 90 days.

Follow for more."""),

 dict(brand="HOLY", shot="new:holy-cart", text="""Worth stealing #7: HOLY's cart, one cent short.

Reward bar from €49 to €200. Under it: "You'll now get the Cap + Shaker. Only €0.01 left for the blue Thermo Shaker."

The bundle costs €99.99. The next gift unlocks at €100.

What they nail:
- unlocked gifts sit in the cart as real lines, "Free!", crossed-out value, "Gift unlocked" in green
- the next one is right below, with a padlock
- shipping's already free, so the bar is only about gifts

One cent away is about the strongest pull you can create. People speed up when a goal gets close.

Two things I'd change:
- "Total savings -€33.97" only counts the gifts. Add the bundle discount and it's €53.95. They undersell their own deal.
- 1 cent can feel like a trick. I'd test unlocking the shaker at €99.99 with "we rounded up for you".

Follow for more."""),

 dict(brand="Fincut", shot="new:fincut-cart", text="""Worth stealing #8: Fincut's tickets in the cart.

Black Friday draw for 3 cars, 1 ticket per item bought. In the cart, the tickets show up as a line item: "Ticket, Grand Jeu. Free. x3."

Remove a t-shirt, lose a ticket. People hate giving up stuff they already "have".

Also:
- the free shirt in the 3+1 pack earns no ticket. 4 shirts, 3 tickets. The rule holds.
- the free shipping bar is already full
- first add-on is a €9 gift box. Very on season.

What bugs me: a banner says "Code BLACK20: -20%, enter it in Promo code". That field is collapsed at the bottom and the €84 total doesn't include it. Why make me type a code the cart already knows?

What I'd test: apply it automatically, or a one-tap "Apply" on the banner. And say if it stacks with the pack (already -25%).

Follow for more."""),

 dict(brand="Represent", shot="16.png", text="""Worth stealing #9: Represent's two lines under the buttons.

French store, UK brand. Under the buttons: "Express France Shipping" with a flag, and "EU Import Duties Included".

After Brexit the fear isn't the price, it's a customs bill at the door. They kill it before you even ask.

- delivery names your country, not "worldwide shipping"
- Klarna shown as 3 x €18.66, each under €20
- "Style With" shows 4 pieces, all with crossed-out prices

They localised the risks. Now localise the words. The page says "RRP" and "30% OFF - SAUVEGARDER €24". In French, "sauvegarder" means saving a file. "Économisez 24 €" and "Prix conseillé" would read like a local store.

What I'd test: fix that one discount line and compare French conversion before and after.

Follow for more."""),

 dict(brand="Alphalete", shot="19.webp", text="""Worth stealing #10: Alphalete's fit suggestion.

"Ilon is 6'1"/185cm, wearing a size L with a 43"/109cm chest."

Height alone tells you almost nothing about a sweater. Chest size does. They give both, in inches and cm, so nobody converts in their head.

- "Oversized" is a badge at the top and the first line of the fit note. Said twice, so nobody sizes down by mistake.
- "Final sale" is as visible as the -70%. No surprise after delivery.

Final sale means no returns. And that's exactly where the fit info gets more precise. Love that.

What I'd test: the garment's own measurements next to the model's, chest width and length of the L. Or one line on what to do between two sizes.

I'd watch conversion on final sale items and sizing questions to support.

Follow for more."""),

 dict(brand="HOLY", shot="15.png", text="""Worth stealing #11: HOLY's price per portion.

€99.99 bundle. Right under it: "150 portions. Only €0.80 per portion."

Same money, smaller unit. A three-digit price becomes a daily one.

- "Total value €119.97" sits above, so €99.99 already reads like a saving
- the button is first person: "I add to cart". The shopper says it, not the brand.
- "Mix & match, save up to 20%" for people who don't want every flavour

€0.80 is a number you instantly compare to what you already buy. That comparison happens in your head, for free.

What I'd test: make it explicit, if it's true for their buyers. "€0.80 a portion, less than a can of energy drink." And next to "Ships in 6 to 10 days", an actual date.

Follow for more."""),

 dict(brand="Boku", shot="12.webp", text="""Worth stealing #12: Boku's compatibility button.

A bidet you fit on your own toilet comes with one obvious question. Boku turns it into a button: "Is this bidet compatible with your toilet?"

- it names the doubt in the shopper's words, before they go google it
- "10-minute install, no works, no electricity", with a video link, handles the next fear
- the first add-on is a 3-way tap for rigid water inlets. The fix for the most likely blocker, sold right there.

That add-on feels less like an upsell and more like help.

What I'd test: turn the button into a 3-question check (toilet shape, seat, water inlet) that ends on "Compatible" and adds the right part. Or at least carry the answer into the cart.

I'd watch conversion after the check and returns marked "incompatible".

Follow for more."""),

 dict(brand="Gymshark", shot="10.png", text="""Worth stealing #13: Gymshark's cart drawer.

Open the cart and the first thing you see is how far you are from free shipping. "€31 to go", a bar from €0 to €59.

- the goal comes before the items, so it frames everything below
- each line repeats colour, size and fit ("Black Wash, M, Boxy Fit")
- savings per item, in euros, even here
- "Your items aren't reserved", urgency that happens to be true

The bar turns shipping from a cost into a goal you're already halfway to.

But look at the suggestions. The 6-pack of socks is €19.60, it doesn't close a €31 gap. Add the next pair at €11.20 and you're still €0.20 short.

What I'd test: suggest products priced just above the gap. Or label one "Unlocks free shipping".

Follow for more."""),

 dict(brand="Fincut", shot="14.png", text="""Worth stealing #14: Fincut's pack selector.

Three options. Only the single t-shirt shows a cost on top: "+ shipping €7.90".

So shipping shows up at the moment you choose, on the option they'd rather you skip. It's the price of not taking the pack.

- the free t-shirt in the 3+1 gets its own row, colour and size. You picked it, it already feels yours.
- "Best seller" on the middle pack, "best offer, ending soon" on the big one. Two different reasons to move up.
- "Take your usual size." One line, no size doubt.

1 shirt is €35.90 delivered. 4 shirts are €84, free shipping. The single option mostly exists to make the pack obvious.

What I'd test: price per t-shirt on each option. €21 each for 3+1, under €20 for 5+2. Or "€21 per t-shirt" in the button.

Follow for more."""),

 dict(brand="AYBL", shot="18.png", text="""Worth stealing #15: AYBL's add-to-cart button.

Until you pick a size, the button doesn't say "Add to cart". It says "Select your size".

No red error after you tap, no shake. Just the next step, where you're already looking.

- the model's height and size are written on the first photo: 1.67m, wearing XS
- "Fits true to size" closes the key features box
- the newsletter is a small side tab ("Never miss a drop"), not a pop-up. Easy to ignore, easy to find later.

They prevent the mistake instead of correcting it.

What I'd test: once a size is picked, echo it in the button. "Add XS to cart." Small, but it confirms the choice right before the tap.

I'd watch size exchanges and returns.

Follow for more."""),

 dict(brand="Arntreal", shot="13.webp", text="""Worth stealing #16: Arntreal's three lines of copy.

Right under the product name (translated):
"A basic bag is bad quality.
A luxury bag is €3,000, and you pay for the logo.
This one has everything of luxury, at €149.90."

Two bad options, then the product sits in the middle. The compromise effect, done in copy instead of a pricing table. And €3,000 anchors the price before €149.90 even shows up.

It talks like a friend ("tu"), not like a catalogue.

The real trick: you stop asking "is €149.90 a lot?" and start asking "do I want to overpay for a logo?". Much easier answer.

What I'd test: the 3 chips below (luxury look, every day, cabin size) don't do anything yet. Tap "Cabin size", see the bag in an overhead bin with its dimensions.

Follow for more."""),

 dict(brand="Oner Active", shot="17.webp", text="""Worth stealing #17: Oner Active's colour names.

The selected colour isn't "Brown". It's "70% Cocoa".

You know the shade before you zoom. Dark chocolate, not beige, not black. And it sticks: "the 70% Cocoa jacket" is way easier to talk about than "the brown one".

There's research on this too. Unusual colour names tend to make people like the product more (Miller and Kahn, 2005).

Other details:
- points shown as 6,660 for a €66.60 jacket. Big numbers feel generous.
- "In stock" in green, right next to the price

What I'd test: show every swatch's name on tap, not only the selected one. People would browse names, not dots. And keep the name in the cart and the confirmation email.

I'd watch swatch taps per session and the colour mix of orders.

Follow for more."""),

 dict(brand="Cabaia", shot="new:cabaia-product", text="""Worth stealing #18: Cabaia's sizes in litres.

Backpack page: "Medium, 18L. Large, 23L", with "Compare sizes" right above.

Litres are the right unit for a bag. "Medium" means nothing until you know what fits.

- every swatch is a photo of the bag with its matching pouch, not a flat dot
- the price is in the button: "Add, €53.40"
- under €100 they lead with the percentage (-40%). Rule of 100 from #1, done right.

What I'd test: turn litres into objects. Most people can't picture 18 litres. "18L: a 14-inch laptop, a jumper, a water bottle. 23L: add a pair of trainers." Only if that's what really fits, obviously.

Or simpler: show the "Compare sizes" answer under the two buttons instead of behind a link.

I'd watch exchanges between Medium and Large.

Follow for more."""),

 dict(brand="Boku", shot="38.webp", text="""Worth stealing #19: Boku's three percentages.

A product image, not a review block. "Tested under dermatological control", then:
- 95% of users find it improves hygiene
- 97% of women find it improves hygiene during periods
- 98% find it pleasant to use

Each number answers a different doubt. Does it work, does it work for me, is it weird to use.

The middle one names a use most brands in this category stay vague about. The women it's for see themselves in it right away.

And the bottle rests on an open hand. You see it's portable before reading a word.

What I'd test: make the numbers checkable. Without a base, 95% could be 19 people out of 20. "95% of [n] users after [x] weeks", with the real figures, turns a claim into a result.

Follow for more."""),

 dict(brand="Broken Planet", shot="22.png", text="""Worth stealing #20: Broken Planet's two models.

"Dawn is 6'2, wearing size XL. Supriya is 5'3, wearing size M."

Same sweatpants, two very different bodies. One model gives you one data point. Two give you a range you can place yourself in. It says unisex without a label.

- "540 GSM organic cotton" comes first. For heavyweight streetwear buyers, fabric weight is the quality proof.
- sold-out sizes stay visible, crossed out. You see what exists and what's gone.

What I'd test: make those crossed-out sizes tappable. "XS is gone. Get notified when it's back." Right now that demand just disappears.

I'd watch back-in-stock sign-ups and sales from restock emails.

Follow for more."""),

 dict(brand="Gymshark", shot="11.png", text="""Worth stealing #21: Gymshark's "224 XP".

Under the add-to-cart button: "Buying this product earns you 224 XP".

XP, not "points". That's gaming talk, and gym people track progress anyway. For a gym brand, levelling up is the whole identity.

- it's specific to this product, not a generic "join our rewards"
- the same box answers the last questions: free shipping from €59, express available
- pay in 4 shown as 4 x €7.00. Smaller number, same total.

Problem: 224 XP of what? Points without an exchange rate are just a number.

What I'd test: give it meaning. "224 XP, one order away from your next level", or what it's worth on the next order. Or show the total this cart gets you to.

I'd watch account sign-ups from product pages and repeat purchases.

Follow for more."""),

 dict(brand="Alphalete", shot="20.png", text="""Worth stealing #22: Alphalete's size guide.

Most size charts just give you numbers. This one first teaches you how to get yours.

- body landmarks, no jargon: "about 1 inch below the armpit", "in line with your belly button"
- a physical cue for the waist: bend to the side, find the crease. Doable alone in your room.
- an IN / CM switch
- ranges, not single numbers: chest 39 to 42 for an M. Real bodies sit between sizes.

A size chart is only as good as the measurement people bring to it. They fixed the input, not just the table.

What I'd test: a "no tape measure?" option. Lay a sweater you own flat, measure armpit to armpit, match it.

Small fix too: the product page sells XXL and XXXL, the guide says 2XL and 3XL. Same labels on both.

Follow for more."""),

 dict(brand="Kosbiotic", shot="23.webp", text="""Worth stealing #23: Kosbiotic's subscription.

The subscription is selected by default. What makes that OK is what's written inside it (translated):
- "Save 10%, no commitment"
- "Cancel in 1 click"
- "Automatic delivery every 28 days"

A pre-selected subscription without those lines would feel like a trap. With them, it just feels like the obvious choice.

28 days matches the length of a cure, so the next box lands when the last one runs out. Also, every 28 days = 13 deliveries a year, not 12. The cure and the revenue line up nicely.

What I'd test: prove the 1-click cancel, with a small link showing the screen where you do it. Or add "Skip or pause anytime" for people scared of a pile of boxes.

I'd watch subscription share and month-1 cancellations.

Follow for more."""),

 dict(brand="Cabaia", shot="new:cabaia-cart", text="""Worth stealing #24: Cabaia's cart, ready for December.

One backpack in the cart, and the last three questions answered before checkout.

When does it arrive? An actual delivery date, using your postcode, plus a link to compare options. Not "3 to 5 business days".

Is it a gift? A checkbox right on the line: "Gift wrap (€2.80)". That's the fix for friction #41.

What goes with it? A "Side pocket Pau, €7". The backpack is called Pau too. They name products after cities, so the match is obvious without a "goes with" label.

In December the delivery date basically is the decision. Having it in the cart removes the last "will it arrive in time?".

What I'd test: once gift wrap is ticked, offer a gift message and a receipt without prices.

Follow for more."""),

 dict(brand="Alo", shot="24.webp", text="""Worth stealing #25: Alo's annotated product photo.

Second photo, little labels pointing at the shirt: "Soft Performance Fabric", "Fitted Sleeves", "Relaxed Fit".

People look at photos before they read. So the copy goes where the attention already is, on the body, instead of in an accordion nobody opens. Learning research calls it spatial contiguity: words next to what they describe get understood faster.

- "Fit: true to size, relaxed cut" right above the size guide
- a member price, €47 instead of €68 if you sign up. The discount becomes an account.

What I'd test: make the labels tappable. "Soft Performance Fabric" opens a close-up of the fabric. Or add a 4th label for whatever their 1,943 reviews ask about most.

I'd watch add-to-cart rate and accordion opens.

Follow for more."""),

 dict(brand="Horace", shot="25.png", text="""Worth stealing #26: Horace's two questions.

The description is just two questions in bold (translated): "What does it do?" and "How do I use it?"

For a first-time buyer, "how do I use it?" is a real question. Answer: morning and/or evening, lather on a wet face and neck. Done.

- they're the questions you'd ask a friend at the counter, not marketing headings
- "Fragrance: none" gets its own line. For a lot of guys that's the deal-breaker.
- the price is in the button: "Add to cart, €13"

They sell the routine, not just the bottle. Knowing how to use it kills the fear of buying something that ends up stuck in the cabinet.

What I'd test: a third question, "What goes with it?", showing the next step of the routine and how close you are to free delivery at €40.

Follow for more."""),

 dict(brand="Le Slip Français", shot="27.png", text="""Worth stealing #27: Le Slip Français's "Frequently bought together".

Under a 5-pack at €99, the suggestions aren't socks or belts. They're bigger packs: 7 boxers for €160, 10 for €185.

Upsizing dressed up as cross-selling.

- the 7-pack photo is a gift: red background, gold bag saying "a little gift, a pretty package"
- the designs have festive names (garland, ski run). In December the product names do the seasonal marketing.

Now the math. The 10-pack is €18.50 a boxer, cheaper than the 5-pack (€19.80). The 7-pack is €22.86 a boxer, more expensive. It sells the wrapping, not the unit price.

What I'd test: show the price per boxer only where it helps, "€18.50 each" on the 10-pack. And sell the gift pack on the moment: "gift-wrapped, delivered before Christmas", if they can promise it.

Follow for more."""),

 dict(brand="Based", shot="42.png", text="""Worth stealing #28: Based's ingredient tiles.

A product image: "The Key Ingredients. Endless Benefits." Four tiles, each with an ingredient, a strip of the actual powder's texture, and one line on what it does.

- you see silica, arrowroot, rice powder and mica. You don't just read their names.
- every chemical name becomes a result: volume, less oil, softness, matte finish
- 4 ingredients, 4 jobs. Nothing's there without a reason.

This image quietly answers the question a €21.95 product weighing 2.5 g raises: what am I paying for? Four named actives make a small format feel dense instead of tiny.

What I'd test: start from the problem, not the ingredient. "Flat hair? Silica silylate. Oily roots by noon? Arrowroot." People know their problem, not the chemistry.

Follow for more."""),

 dict(brand="Polène", shot="28.webp", text="""Worth stealing #29: Polène's split screen.

Left half: the bag worn, in a huge landscape. Right half: the same bag alone on white, name, price, one button.

Emotion and facts side by side. You never scroll from one to the other. And you read the left side first, so it's desire before details.

- tons of white space around the packshot. At €380, room signals value.
- "3D view" lets you turn the bag yourself instead of scrolling six angles

Half magazine, half shop window. It never makes you choose between wanting it and checking it.

What I'd test: the question every compact bag gets. What fits inside? One photo of it open with a phone, cards and keys. Or one line under the price.

I'd watch add-to-cart rate and returns for "too small".

Follow for more."""),

 dict(brand="Typology", shot="29.png", text="""Worth stealing #30: Typology's lab codes.

The serum is called "A63". Above the name there's a reference like a lab sample, "LAB1035-30ML-SG". The description is in a typewriter font.

- the name is the active and its concentration ("PDRN-EGF Complex 3%"), not a mood word like "Glow"
- precise numbers read as honest: "150,000 vegan micro-spicules per gram", "95% natural origin"
- a 15 ml option next to the 30 ml, a cheaper way to try something new
- "Is this compatible with your skin type?" right under the button

The page looks like a lab sheet because the promise is science. The design is the proof.

What I'd test: call the 15 ml what it is, "Trial size", and show its price on the toggle before the click.

I'd watch first-order conversion and repurchases from 15 to 30 ml.

Follow for more."""),

 dict(brand="Stüssy", shot="32.png", text="""Worth stealing #31: Stüssy's product page, for what it leaves out.

A €70 glass ashtray. No reviews, no "only 3 left", no countdown, no upsell carousel.

- product details open by default, as a plain list
- every dimension in inches and cm. For an object, size is the first unknown.
- a holiday shipping guide at the top, with a "Hide" link
- a list, a photo, one black button. The page looks like the brand.

For a cult brand, persuasion tricks would cheapen the product. The restraint is the signal.

What I'd test: scale. On a white background, 20cm reads as nothing. One photo next to a hand or a lighter. Or a side view showing the 2.5cm height.

I'd watch returns for "smaller than expected".

Follow for more."""),

 dict(brand="Charles Tyrwhitt", shot="37.png", text="""Worth stealing #32: Charles Tyrwhitt's shirt builder.

€29.95 shirt (was €84.95), and a red banner: "Save €55 today, no promo code needed."

"No promo code needed" stops the trip to Google looking for one. The leak from friction #27, closed in five words.

- the fit is picked from drawings of the shirt, not words like "slim" that mean something different to everyone
- collar sizes in cm, grouped under S, M, L, XL. Experts read the cm, everyone else reads the letter.
- "Your selections" recaps each choice with a tick

One thing's off: the "Most popular" badge sits on Slim, which is crossed out. Unavailable. The badge sends people to something they can't buy.

What I'd test: when an option sells out, move the badge, or swap it for "Notify me".

Follow for more."""),

 dict(brand="Le Slip Français", shot="26.png", text="""Worth stealing #33: Le Slip Français's discount ladder.

Three small chips under the price: "-5% extra from 3", "-10% extra from 4", "-20% extra from 5".

- you see the reward for buying more before choosing the quantity, not at checkout
- three steps instead of one threshold. Each one is a small yes.
- "extra" means it stacks on a price that's already reduced (€99 instead of €125)
- green dots on every size, so stock is answered without a click

The ladder turns "how many?" into "which step do I stop at?". People anchor on the next step, not on 1.

What I'd test: carry it into the cart. "Add 1 more item to unlock -10%." Or highlight the step the cart has reached.

I'd watch items per order and how many orders land on 3, 4 and 5.

Follow for more."""),

 dict(brand="Arntreal", shot="40.png", text="""Worth stealing #34: Arntreal's proof before the promise.

Above the product name, before anything else: five stars, "Over 100,000 bags sold" with a French flag, and five tiny customer photos.

Most pages go product, promise, then reviews way down. Arntreal flips it. Proof, promise, product.

- the bold claim that follows ("Everything of a luxury bag. Except the price.") lands on a crowd that already bought
- faces turn 100,000 into people. A number is abstract, five faces are someone like you.

But the stars have no rating and no count. "100,000 bags sold" is a sales number, not a review number, so five stars alone can look like decoration.

What I'd test: show the real average and the number of reviews, and make the stars jump to them. Or make each face tappable, opening that person's photo review.

Follow for more."""),

 dict(brand="Apple", shot="34.png", text="""Worth stealing #35: Apple's step-by-step configurator.

Each step opens with one short sentence in two colours (translated): "Model." in black, "Choose the size." in grey. Then two big cards, 13-inch and 15-inch.

- one decision per step. Black names the step, grey tells you what to do.
- dots on the side show how many steps are left
- size first, the one question anyone can answer without reading specs
- every card shows the total and the monthly price

Now look at the gap. In totals, the 15-inch is €300 more. Monthly, it's €8.96 more. Same difference, and one of them sounds like a coffee a week.

What I'd test: once the 13-inch is selected, show the upgrade as a difference, "+€8.96 a month", on the 15-inch card.

I'd watch the share of 15-inch and the average configured price.

Follow for more."""),

 dict(brand="Decathlon", shot="35.png", text="""Worth stealing #36: Decathlon's price block.

€459.99 outdoor table tennis table. Under the price: "€85 off" in red, then "Promotion from 03/11/2026 to 26/01/2027".

- the saving is in euros, not percent. On a €545 product, €85 sounds bigger than 16%. Rule of 100, done right.
- the promo has real dates. Urgency without a fake countdown, and you believe it because it's specific.
- the description sells the use: friends, family, outdoors, big wheels, room for the paddles

A dated promo is the honest version of a timer.

Two small conflicts though. The top badge says "Free delivery", the price block says "Delivery fees may be added". Pick one, at the top, with its condition. And "Size: no size" can go. A line that says nothing still costs attention.

Follow for more."""),

 dict(brand="Garmin", shot="36.png", text="""Worth stealing #37: Garmin's version selector.

On the fēnix E page, the other versions are buttons right under the case size: fēnix 8 AMOLED, Solar, Pro AMOLED, Pro MicroLED.

- the whole range is one tap away, on one page. No back button, no new tab to compare.
- case size is a row of buttons in mm, with an info icon if you don't know your wrist
- €150 off shown in euros, and Klarna splits it into 3 x €149.99, just under €150

Comparing never means leaving the page.

But "Solar", "AMOLED", "MicroLED" are specs, not reasons. Nobody upgrades for a word they don't understand.

What I'd test: under each version, the price difference and one benefit in plain words ("charges in the sun"). Or an info icon on each version, like the one on case size.

I'd watch the share of orders above this version.

Follow for more."""),

 dict(brand="Based", shot="31.png", text="""Worth stealing #38: Based's packaging notice.

On the product page, two tubes side by side: "New Packaging, Same Texture Powder." Then: "You may receive either our previous or new packaging. The product inside is the same."

During a rebrand, the risk isn't the design. It's someone opening a box that doesn't match the photo and thinking it's fake.

- they show both versions, so whatever arrives was expected
- it answers a support ticket before anyone writes it
- a logistics problem becomes a little piece of brand news

Satisfaction is basically the gap between what you expected and what you got. They moved the expectation instead of hoping the old stock runs out first.

What I'd test: put the same image in the shipping confirmation email. The doubt happens at unboxing, not on the product page.

Follow for more."""),
]

MAX_CHARS = 900

if __name__ == '__main__':
    import re
    for i, p in enumerate(WS, 1):
        t = p['text']
        assert t.startswith(f'Worth stealing #{i}: '), (i, t[:30])
        assert len(t) <= MAX_CHARS, (i, p['brand'], len(t))
        assert '·' not in t and '–' not in t and '—' not in t, i
        assert not re.search('[\U0001F000-\U0001FFFF☀-➿]', t), i
        assert t.endswith('Follow for more.'), i
    print(len(WS), 'posts ; max', max(len(p['text']) for p in WS), '; longueurs :', [len(p['text']) for p in WS])
