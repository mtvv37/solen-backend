"""Posts « Worth stealing » écrits à partir des captures de Thomas (format long, X Premium).

Une capture = un post. Ordre = ordre de publication à 13h, à partir du 24 novembre.
`shot` = nom du fichier de la capture, publié à côté de la page (les captures restent hors du repo).
Règles : anglais, pas de tiret long ni d'emoji, on ne décrit que ce qui est visible, aucun résultat de marque inventé.
"""

WS = [
 dict(brand="Gymshark", shot="9.webp", text="""Worth stealing #1: Gymshark's discount badge.

One small label above the product name: "-30% | €12 saved".

Why it works:
· It sits above the title, so the deal is read before the product.
· It states the same discount twice: as a percentage and in euros.
· The old price (€40) is right next to the new one (€28). No math needed.
· "Boxy Fit" under the title sets the fit before you reach the size grid.

The smart part: on a €40 item, "30%" sounds bigger than "€12". That's the rule of 100: under 100, a percentage feels larger; above 100, the amount in money does. Gymshark leads with the bigger-sounding number.

What I'd test next:
Flip the order on items above €100: "€45 saved | -30%".
Or simpler: on high-ticket items, show only the amount saved.

Hypothesis: the same discount sells better when framed in its bigger-sounding unit. Metric: add-to-cart rate on discounted items, split by price band.

Follow for more breakdowns like this."""),

 dict(brand="Gymshark", shot="10.png", text="""Worth stealing #2: Gymshark's cart drawer.

Open the cart and the first thing you read is how far you are from free shipping: "€31 to go", with a bar from €0 to €59.

Why it works:
· The goal comes before the items, so it frames everything below.
· Each line repeats colour, size and fit ("Black Wash, M, Boxy Fit"). No doubt about what you picked.
· Savings are shown per item, in euros, even in the cart.
· "Your items aren't reserved" adds urgency that happens to be true.

The smart part: the bar turns shipping from a cost into a goal you're already halfway to.

What I'd test next:
The suggestions under it. The 6-pack of socks at €19.60 doesn't close a €31 gap, and with the next pair at €11.20 you'd still be €0.20 short. I'd suggest products priced just above the gap.
Or simpler: label one product "Unlocks free shipping".

Hypothesis: shoppers add more when one tap clearly gets them over the line. Metric: share of carts reaching the threshold, average order value.

Follow for more breakdowns like this."""),

 dict(brand="Represent", shot="16.png", text="""Worth stealing #3: Represent's two lines under the buttons.

On the French store: "Express France Shipping" with a flag, then "EU Import Duties Included".

Why it works:
· A UK brand selling into the EU after Brexit. The fear isn't the price, it's a customs bill at the door. They answer it before you ask.
· The delivery promise names your country, not "worldwide shipping".
· Klarna is shown as 3 payments of €18.66, under €20 each.
· "Style With" shows four pieces with their crossed-out prices: the outfit, already on sale.

The smart part: they localised the risks, the things that make cross-border shoppers hesitate.

What I'd test next:
Localise the words too. The page says "RRP" and "30% OFF, SAUVEGARDER €24". In French, "sauvegarder" means saving a file. "Économisez 24 €" and "Prix conseillé" would read like a local store.
Or simpler: fix the one discount line.

Hypothesis: copy that reads native builds the same trust as "duties included". Metric: French conversion rate, before and after.

Follow for more breakdowns like this."""),

 dict(brand="Based", shot="30.png", text="""Worth stealing #4: Based's Black Friday button.

The main button doesn't say "Add to cart". It says "Buy one get one €21.95", in gold.

Why it works:
· The offer lives in the button, the one place everybody looks before deciding.
· The price is the same as a single, so "get one free" needs no math.
· The banner under it repeats it: "Buy one, get one is live."
· A 60-day satisfaction guarantee closes the page.

The smart part: they didn't add a promo block next to the product. They changed the action itself.

What I'd test next:
Two details for European shoppers. The price is in euros, but the free shipping thresholds are in dollars ($50+, $100+). One currency everywhere.
And "2.5 g" next to €21.95 can look tiny. "Lasts about X weeks" would answer it, if they know the number.

Hypothesis: on small formats, "how long does it last?" matters more than the weight. Metric: conversion on EU traffic, reviews mentioning "small".

Follow for more breakdowns like this."""),

 dict(brand="Fincut", shot="14.png", text="""Worth stealing #5: Fincut's pack selector.

Three options, and the single t-shirt is the only one with a cost attached: "+ shipping €7.90".

Why it works:
· Shipping shows up at the moment of choice, on the option they'd rather you skip. It's the cost of not taking the pack, not a surprise at checkout.
· The free t-shirt gets its own row, with its own colour and size. You've already picked it, so it already feels yours.
· "Best seller" on the middle pack, "best offer, ending soon" on the biggest: two different reasons to move up.
· One short line kills size doubt: "Take your usual size."

The smart part: 1 shirt is €35.90 delivered. 4 shirts are €84 with free shipping. The single option mostly exists to make the pack look obvious.

What I'd test next:
Show the price per t-shirt on each option: €21 each for 3+1, under €20 each for 5+2.
Or simpler: put "€21 per t-shirt" inside the add-to-cart button.

Hypothesis: when the pack math is instant, more shoppers pick the biggest pack. Metric: share of 5-packs, units per order.

Follow for more breakdowns like this."""),

 dict(brand='DJI', shot='33.png', text="""Worth stealing #0: DJI's Black Friday, without a discount.

A €1,599 drone bundle during Black Friday, and the price doesn't move. Instead (translated): a free DJI Pro backpack, tagged "Gift", and "5 times more DJI credit on your purchase".

Why it works:
· No price cut means no new reference price. €1,599 stays credible after November 30.
· Credit can only be spent at DJI. The deal brings you back for batteries, filters, the next drone.
· The gift is an object you can picture, first in the box, before the specs.
· 30-day returns and the official warranty sit right under it: the risk side of a big purchase.

The smart part: on high-ticket products, discounts hurt the brand and its resellers. Value added instead of value removed protects both.

What I'd test next:
Put the credit in euros. If the base is the 1% shown above, 5 times more is about €80 on this bundle. "5x" sounds clever, "€80 back" is money you can already spend in your head. Above 100, the amount beats the ratio (the rule of 100 from #1).
Or simpler: "€80 in DJI credit" right next to the price.

Hypothesis: a concrete euro amount pulls harder than a multiplier on a percentage nobody remembers. Metric: conversion during the promotion, share of credit redeemed within 90 days.

Follow for more breakdowns like this."""),

 dict(brand="HOLY", shot="15.png", text="""Worth stealing #6: HOLY's price per portion.

A €99.99 bundle, and the line right under it: "150 portions. Only €0.80 per portion."

Why it works:
· It turns a three-digit price into a daily one. Same money, smaller unit.
· "Total value €119.97" sits above, so €99.99 already reads as a saving.
· The button is in the first person: "I add to cart". The shopper says it, not the brand.
· "Mix & match: save up to 20%" keeps the door open for people who don't want every flavour.

The smart part: €0.80 is a number shoppers can compare to what they already buy. That comparison happens in their head, for free.

What I'd test next:
Make the comparison explicit, only if it holds for their buyers: "€0.80 a portion, less than a can of energy drink".
Or simpler: next to "Ships in 6 to 10 days", show the actual delivery date.

Hypothesis: a concrete comparison anchors lower than a bare unit price. Metric: bundle conversion rate, bundle share of orders.

Follow for more breakdowns like this."""),

 dict(brand="Alphalete", shot="19.webp", text="""Worth stealing #7: Alphalete's fit suggestion.

"Ilon is 6'1"/185cm, wearing a size L with a 43"/109cm chest."

Why it works:
· Height tells you little about a sweater. Chest size is what decides it. They give both.
· Imperial and metric in the same line, so nobody converts in their head.
· "Oversized" is a badge at the top and the first line of the fit note. Said twice, so nobody sizes down by mistake.
· The "Final sale" badge is as visible as "-70%". No surprise after delivery.

The smart part: final sale means no returns. The fit info gets more precise exactly where the safety net disappears.

What I'd test next:
Add the garment's own measurements next to the model's: chest width and length of the L.
Or simpler: one line on what to do between two sizes, if they have a clear rule.

Hypothesis: on non-returnable items, precise fit data lowers hesitation more than a bigger discount. Metric: conversion on final sale items, sizing questions to support.

Follow for more breakdowns like this."""),

 dict(brand="Arntreal", shot="13.webp", text="""Worth stealing #8: Arntreal's three lines of copy.

Right under the product name (translated from French):
"A basic bag is bad quality.
A luxury bag is €3,000, and you pay for the logo.
This one has everything of luxury, at €149.90."

Why it works:
· It sets two bad options, then places the product between them. The compromise effect, done in copy instead of a pricing table.
· €3,000 anchors the price before €149.90 shows up.
· It talks like a friend ("tu"), not like a catalogue.
· Below, three chips answer "when would I use it?": luxury look, every day, cabin size.

The smart part: the shopper isn't asked "is €149.90 a lot?" but "do I want to overpay for a logo?". Different question, easier answer.

What I'd test next:
Make the chips do something: "Cabin size" shows the bag in an overhead bin, with its dimensions.
Or simpler: put the dimensions inside the "Cabin size" chip.

Hypothesis: concrete proof behind each use case removes the last doubt. Metric: add-to-cart rate after a chip tap.

Follow for more breakdowns like this."""),

 dict(brand="Gymshark", shot="11.png", text="""Worth stealing #9: Gymshark's "224 XP".

Under the add-to-cart button: "Buying this product earns you 224 XP".

Why it works:
· XP, not "points". It's the language of games, and of people who track their reps.
· It's specific to this product, not a generic "join our rewards".
· The same box answers the last two questions: free shipping from €59, express available.
· Paying in 4 is shown as 4 x €7.00. A smaller number than €28, same total.

The smart part: loyalty framed as progress, not as a discount. For a gym brand, levelling up is the identity.

What I'd test next:
Give the XP a meaning: "224 XP, one order away from your next level", or what it's worth on the next order. Points without an exchange rate are just a number.
Or simpler: show the XP total this cart would get you to.

Hypothesis: a reward you can picture pulls harder than an abstract one. Metric: account sign-ups from product pages, repeat purchase rate.

Follow for more breakdowns like this."""),

 dict(brand="Boku", shot="12.webp", text="""Worth stealing #10: Boku's compatibility button.

A bidet you fit on your own toilet comes with one big unspoken question. Boku puts it on a button (translated): "Is this bidet compatible with your toilet?"

Why it works:
· It names the objection in the shopper's words, before they leave to google it.
· "10-minute install, no works, no electricity" handles the next fear, with a video link.
· The first add-on is a 3-way tap "for rigid water inlets": the fix for the most likely blocker, sold right there.
· The benefits are blunt about what the product does. In an awkward category, plain words remove embarrassment.

The smart part: that add-on isn't an upsell. It's an installation fix, placed next to the question it answers.

What I'd test next:
Turn the button into a 3-question check (toilet shape, seat type, water inlet) that ends on "Compatible" and adds the right part automatically.
Or simpler: carry the result into the cart, so nobody wonders again at checkout.

Hypothesis: shoppers who get a clear yes buy more and return less. Metric: conversion after the check, returns marked "incompatible".

Follow for more breakdowns like this."""),

 dict(brand="AYBL", shot="18.png", text="""Worth stealing #11: AYBL's add-to-cart button.

Until you pick a size, the button doesn't say "Add to cart". It says "Select your size".

Why it works:
· The button tells you the next step instead of throwing an error after you tap.
· The model's height and size are written on the first photo: 1.67m, wearing XS. The fit answer is where your eyes already are.
· "Fits true to size" closes the key features box.
· The newsletter isn't a pop-up. It's a small side tab: "Never miss a drop". Easy to ignore, easy to find later.

The smart part: they prevent the mistake instead of correcting it. No red error text, no shake, just the right instruction in the right place.

What I'd test next:
Once a size is picked, echo it in the button: "Add XS to cart".
Or simpler: show the model's size on every photo, not only the first one.

Hypothesis: confirming the choice in the button cuts wrong-size orders. Metric: size exchanges and returns.

Follow for more breakdowns like this."""),

 dict(brand="Oner Active", shot="17.webp", text="""Worth stealing #12: Oner Active's colour names.

The selected colour isn't "Brown". It's "70% Cocoa".

Why it works:
· You know the exact shade before you zoom: dark chocolate, not beige, not black.
· It sticks. "The 70% Cocoa jacket" is easier to talk about than "the brown one".
· Points are shown as 6,660 for a €66.60 jacket. Big numbers feel generous.
· "In stock" in green sits next to the price, so availability is settled before the button.

The smart part: a colour name does the job of a photo and of a brand voice at once. Research backs it: unusual colour names tend to raise preference (Miller and Kahn, 2005).

What I'd test next:
Show every swatch's name on hover or tap, not only the selected one, so shoppers browse names, not dots.
Or simpler: keep the colour name in the cart line and the order confirmation.

Hypothesis: named colours get explored more, and more of them get bought. Metric: swatch taps per session, colour mix of orders.

Follow for more breakdowns like this."""),

 dict(brand="Broken Planet", shot="22.png", text="""Worth stealing #13: Broken Planet's two models.

"Dawn is 6'2, wearing size XL. Supriya is 5'3, wearing size M." Same sweatpants, two very different bodies.

Why it works:
· One model gives you one data point. Two give you a range you can place yourself in.
· It says unisex without a label.
· "540 GSM organic cotton" comes first. For heavyweight streetwear buyers, fabric weight is the quality proof.
· Sold-out sizes stay visible, crossed out. You see what exists and what's gone.

The smart part: they don't ask you to trust a size chart. They let you compare yourself to two real people.

What I'd test next:
Make the crossed-out sizes tappable: "XS is gone. Get notified when it's back."
Or simpler: tag each lifestyle photo with who's wearing what size.

Hypothesis: sold-out sizes are demand signals they currently throw away. Metric: back-in-stock sign-ups, sales from restock emails.

Follow for more breakdowns like this."""),

 dict(brand="Alphalete", shot="20.png", text="""Worth stealing #14: Alphalete's size guide.

Most size charts give you numbers. This one first teaches you how to get yours.

Why it works:
· Body landmarks instead of jargon: "about 1 inch below the armpit", "in line with your belly button".
· A physical cue for the waist: "bend to the side to find the natural crease". You can do it alone, in your room.
· An IN / CM switch, so nobody converts in their head.
· Ranges, not single numbers: chest 39 to 42 for an M. Real bodies sit between sizes.

The smart part: a size chart is only as good as the measurement people bring to it. They fixed the input, not just the table.

What I'd test next:
A "no tape measure?" option: lay a sweater you own flat, measure armpit to armpit, match it to the garment.
And one small fix: the product page sells XXL and XXXL, the guide says 2XL and 3XL. Same labels on both.

Hypothesis: easier measuring means more people use the guide, and fewer order two sizes. Metric: guide opens followed by add to cart, size exchanges.

Follow for more breakdowns like this."""),

 dict(brand="Kosbiotic", shot="23.webp", text="""Worth stealing #15: Kosbiotic's subscription option.

The subscription is selected by default. What makes that acceptable is the three lines inside it (translated).

Why it works:
· "Save 10% · No commitment" sits right under the price.
· "Cancel in 1 click" answers the fear behind every subscription: will I get stuck?
· "Automatic delivery every 28 days" matches the length of a cure. The next box lands when the last one runs out.
· The button repeats the unit: "€66.11 / month". No doubt that it's recurring.

The smart part: the default does the selling, the reassurance does the trust. A pre-selected subscription without those lines would feel like a trap. And every 28 days means 13 deliveries a year, not 12: the cure length and the revenue line up.

What I'd test next:
Prove the 1-click cancel: a link that shows the account screen where you do it.
Or simpler: add "Skip or pause anytime", for people afraid of a pile of boxes.

Hypothesis: visible proof of an easy exit raises subscription take-up more than a bigger discount. Metric: subscription share of orders, cancellations in month 1.

Follow for more breakdowns like this."""),

 dict(brand="Alo", shot="24.webp", text="""Worth stealing #16: Alo's annotated product photo.

The second photo has labels pointing at the garment: "Soft Performance Fabric", "Fitted Sleeves", "Relaxed Fit".

Why it works:
· Each feature is named where it is, on the body, not in an accordion below.
· Shoppers look at photos before they read. The copy goes where the attention already is.
· "Fit: true to size, relaxed cut" repeats the fit right above the size guide.
· The member price ("€47 for members only, sign up") turns the discount into an account.

The smart part: it's the spatial contiguity principle from learning research. People understand faster when the words sit next to what they describe.

What I'd test next:
Make the labels tappable: "Soft Performance Fabric" opens a close-up of the fabric.
Or simpler: add a fourth label for the question their 1,943 reviews raise most.

Hypothesis: annotated photos answer questions earlier, so fewer shoppers scroll down hunting for details. Metric: add-to-cart rate, accordion opens per session.

Follow for more breakdowns like this."""),

 dict(brand="Horace", shot="25.png", text="""Worth stealing #17: Horace's two questions.

The product description is two questions in bold (translated): "What does it do?" and "How do I use it?"

Why it works:
· For a first-time buyer, "how do I use it?" is a real question. The answer is plain: morning and/or evening, lather on a wet face and neck.
· They're the questions you'd ask a friend at the counter, not marketing headings.
· "Fragrance: none" gets its own line. For many buyers, that's the deal-breaker.
· The price is in the button: "Add to cart, €13". No scrolling back up.

The smart part: they sell the routine, not just the product. Knowing how to use it removes the fear of buying something that will sit in the cabinet.

What I'd test next:
A third question: "What goes with it?", showing the next step of the routine and how close it gets you to free delivery at €40.
Or simpler: a 10-second video of the "how to use" part.

Hypothesis: shoppers who see a full routine buy more than one product. Metric: items per order, routine bundle take-up.

Follow for more breakdowns like this."""),

 dict(brand="Le Slip Français", shot="26.png", text="""Worth stealing #18: Le Slip Français's discount ladder.

Three small chips under the price (translated): "-5% extra from 3", "-10% extra from 4", "-20% extra from 5".

Why it works:
· The reward for buying more is visible before you choose the quantity, not discovered at checkout.
· Three steps instead of one threshold. Each step is a small yes.
· "Extra" means it stacks on a price already reduced (€99 instead of €125).
· Green dots on every size: stock is answered without a click.

The smart part: the ladder turns "how many?" into "which step do I stop at?". Shoppers anchor on the next step, not on 1.

What I'd test next:
Carry the ladder into the cart: "Add 1 more item to unlock -10%."
Or simpler: highlight the step the current cart has reached.

Hypothesis: shoppers climb a ladder they can see from the cart, not only from the product page. Metric: items per order, share of orders at 3, 4 and 5 items.

Follow for more breakdowns like this."""),

 dict(brand="Le Slip Français", shot="27.png", text="""Worth stealing #19: Le Slip Français's "Frequently bought together".

Under a 5-pack at €99, the suggestions aren't socks or belts. They're bigger packs: 7 boxers at €160, 10 at €185.

Why it works:
· It's upsizing dressed as cross-selling. The next step up is already in view.
· The 7-pack photo is a gift: red background, a gold bag that says "a little gift, a pretty package".
· The designs have festive names (garland, ski run). In December, the product names do the seasonal marketing.
· Crossed-out prices on both keep the deal frame going.

The smart part: the 10-pack is €18.50 a boxer, cheaper than the 5-pack (€19.80). The 7-pack is €22.86, more per boxer. It sells the wrapping, not the unit price.

What I'd test next:
Show the price per boxer only where it helps: "€18.50 each" on the 10-pack.
And sell the gift pack on the moment instead: "Gift-wrapped, delivered before Christmas", if they can promise it.

Hypothesis: unit prices push bulk buyers, gift framing pushes gift buyers. Mixing both in one carousel blurs each. Metric: take-up of each suggestion, average order value.

Follow for more breakdowns like this."""),

 dict(brand="Polène", shot="28.webp", text="""Worth stealing #20: Polène's split screen.

Left half: the bag worn, in a wide landscape. Right half: the same bag alone on white, name, price, one button.

Why it works:
· Emotion and facts sit side by side. You don't scroll from one to the other.
· The left side is read first. Desire before details.
· The packshot has a lot of white space around it. At €380, room signals value.
· "3D view" lets you turn the bag yourself, instead of a row of six angles.

The smart part: the page is half magazine, half shop window. It never makes you choose between wanting it and checking it.

What I'd test next:
The question a compact bag always gets: what fits inside? A photo of it open with a phone, cards and keys.
Or simpler: one line under the price saying what fits, if it does.

Hypothesis: for small bags, "will my things fit?" is the last doubt before buying. Metric: add-to-cart rate, returns for "too small".

Follow for more breakdowns like this."""),

 dict(brand="Typology", shot="29.png", text="""Worth stealing #21: Typology's lab codes.

The serum is called "A63". Above the name, a reference like a lab sample: "LAB1035-30ML-SG". The description is set in a typewriter font.

Why it works:
· The name is the active and its concentration ("PDRN-EGF Complex 3%"), not a mood word like "Glow".
· Precise numbers read as honest (translated): "150,000 vegan micro-spicules per gram", "95% ingredients of natural origin".
· A 15 ml option next to the 30 ml lowers the cost of trying a new product.
· "Is this product compatible with your skin type?" opens a diagnostic, right under the button.

The smart part: the page looks like a lab sheet because the promise is science. The design itself is the proof of seriousness.

What I'd test next:
Name the 15 ml for what it is, "Trial size", and show its price on the toggle.
Or simpler: show the price difference before the click, not after.

Hypothesis: on a new product, an explicit trial size converts first-time buyers who would skip the 30 ml. Metric: first-order conversion, repurchase from 15 ml to 30 ml.

Follow for more breakdowns like this."""),

 dict(brand="Stüssy", shot="32.png", text="""Worth stealing #22: Stüssy's product page, for what it leaves out.

A €70 glass ashtray. No reviews, no "only 3 left", no countdown, no upsell carousel.

Why it works:
· The product details are open by default, as a plain list: shape, notches, etched logo, material.
· Every dimension in inches and centimetres. For an object, size is the first unknown.
· The holiday shipping guide sits at the top, with a "Hide" link. Useful, and easy to dismiss.
· The page looks like the brand: a list, a photo, one black button.

The smart part: for a cult brand, persuasion tricks would cheapen the product. The restraint is the signal.

What I'd test next:
Scale. On a white background, 20cm reads as nothing. One photo of the ashtray next to a hand or a lighter.
Or simpler: a side view showing the 2.5cm height.

Hypothesis: shoppers who can picture the real size hesitate less on a €70 object. Metric: add-to-cart rate, returns for "smaller than expected".

Follow for more breakdowns like this."""),

 dict(brand="Based", shot="31.png", text="""Worth stealing #23: Based's packaging notice.

On the product page, two tubes side by side: "New Packaging, Same Texture Powder." Then: "You may receive either our previous or new packaging. The product inside is the same."

Why it works:
· During a rebrand, the risk isn't the design. It's a customer opening a box that doesn't match the photo and thinking it's fake.
· They show both versions, so whatever arrives was expected.
· It answers a support ticket before it's written.
· It turns a logistics problem into a small piece of brand news.

The smart part: satisfaction is the gap between what people expect and what they get. They moved the expectation instead of hoping the old stock runs out first.

What I'd test next:
Put the same image in the shipping confirmation email. The doubt happens at the unboxing, not on the product page.
Or simpler: one line on the packing slip.

Hypothesis: fewer "is this the right product?" tickets and returns during the transition. Metric: support tickets about packaging, returns tagged "wrong item".

Follow for more breakdowns like this."""),
 dict(brand='Apple', shot='34.png', text="""Worth stealing #0: Apple's step-by-step configurator.

Each step opens with one short sentence in two colours (translated): "Model." in black, "Choose the size." in grey. Then two big cards: 13-inch and 15-inch.

Why it works:
· One decision per step. The black word names the step, the grey words tell you what to do.
· Dots on the side show how many steps are left. No surprise at the end.
· Each card gives the total and the monthly price: from €1,399, or €41.80 a month over 36 months.
· Size comes first: the one question every buyer can answer without reading specs.

The smart part: in totals, the 15-inch costs €300 more. In monthly terms, it's €8.96 more. Same gap, and one of them sounds like a coffee a week.

What I'd test next:
Show each upgrade as a difference from the current choice: "+€8.96 a month" on the 15-inch card once the 13-inch is selected.
Or simpler: one line under each size saying who it's for.

Hypothesis: upgrades framed as small monthly differences get picked more than upgrades framed as totals. Metric: share of 15-inch, average configured price.

Follow for more breakdowns like this."""),

 dict(brand='Decathlon', shot='35.png', text="""Worth stealing #0: Decathlon's price block.

A €459.99 outdoor table tennis table. Under the price (translated): "€85 off" in red, then "Promotion from 03/11/2026 to 26/01/2027".

Why it works:
· The saving is in euros, not in percent. On a €545 product, €85 sounds bigger than 16%. The rule of 100, applied right.
· The promotion has real dates. Urgency without a fake countdown, and credible because it's specific.
· The description sells the use: friends and family, outdoors, big wheels to move it, storage for the paddles.
· 4.7 stars from 103 reviews sit right under the name.

The smart part: a dated promotion is the honest version of a timer. You know exactly how long you have, so you believe the discount.

What I'd test next:
Two small conflicts. The top badge says "Free delivery", the price block says "Delivery fees may be added". One message, at the top, with its condition if there is one.
And "Size: no size" can go. A line that says nothing still costs attention.

Hypothesis: removing the shipping contradiction lowers hesitation right before the button. Metric: add-to-cart rate, drop-off at the shipping step.

Follow for more breakdowns like this."""),

 dict(brand='Garmin', shot='36.png', text="""Worth stealing #0: Garmin's version selector.

On the fēnix E page, the other versions aren't hidden in another menu. They're buttons under the case size: fēnix 8 AMOLED, fēnix 8 Solar, fēnix 8 Pro AMOLED, fēnix 8 Pro MicroLED.

Why it works:
· The whole range is one tap away, on one page. No back button, no new tab to compare.
· You land on the entry model, so the first price you see is the lowest. Everything above is a choice, not a default.
· Case size is a row of buttons in mm, with an info icon for anyone who doesn't know their wrist.
· The discount is in euros (€150 off), and Klarna splits the price into 3 payments of €149.99, just under €150.

The smart part: the product range becomes a single page with an upgrade ladder. Comparing never means leaving.

What I'd test next:
Tell people why to climb. "Solar", "AMOLED", "MicroLED" are specs, not reasons. Under each version: the price difference and one benefit in plain words ("charges in the sun").
Or simpler: an info icon on each version, like the one on case size.

Hypothesis: shoppers upgrade when they understand what the difference buys them. Metric: share of orders above the entry version, version button taps.

Follow for more breakdowns like this."""),

 dict(brand='Charles Tyrwhitt', shot='37.png', text="""Worth stealing #0: Charles Tyrwhitt's shirt builder.

A €29.95 shirt (was €84.95), and the red banner under the price says (translated): "Save €55 today, no promo code needed."

Why it works:
· "No promo code needed" stops the detour to Google in search of a code, the leak from friction #27, closed in five words.
· The fit is chosen with drawings of the shirt, not with words like "slim" that mean something different to everyone.
· Collar sizes in cm are grouped under S, M, L, XL. Experts read the centimetres, everyone else reads the letter.
· "Your selections" recaps the choices so far, each with a tick.

The smart part: two sizing languages on one screen, so neither the made-to-measure buyer nor the casual one feels lost.

What I'd test next:
The "Most popular" label sits on Slim, which is crossed out, unavailable. The badge points shoppers to something they can't buy. When an option sells out, move the label, or swap it for "Notify me".
Or simpler: grey the label out with the option.

Hypothesis: a popularity badge on an unavailable option creates frustration instead of reassurance. Metric: exits at the fit step, notify-me sign-ups.

Follow for more breakdowns like this."""),
 dict(brand='Arntreal', shot='39.png', text="""Worth stealing #0: Arntreal's Black Friday draw.

On the product page (translated): "Black Friday draw. Each order = 1 entry to win a luxury watch." Three prizes: a Rolex Oyster Perpetual, an Omega Speedmaster, a Cartier Santos. Then "See the rules".

Why it works:
· The prize fits the promise. The page sells "everything of a luxury bag, except the price". The draw offers the real luxury logo, without paying for it.
· A discount costs margin on every order. Three watches are a fixed cost: the more orders, the cheaper each entry gets.
· The price doesn't move, so €149.90 stays the reference after Black Friday.
· The rule fits in five words, and the rules link sits right under it.

The smart part: the purchase is reasonable, the reward is a dream. You buy a €149.90 bag and get a ticket for the watch you'd never buy yourself.

What I'd test next:
"Each order" rewards splitting a basket: two orders of one bag earn two entries, one order of two bags earns one. Fincut runs the same kind of draw but ties tickets to the pack: its 3+1 pack earns 3 tickets. I'd test 1 entry per bag.
Or simpler: a bonus entry for orders of 2 bags or more.

Hypothesis: entries tied to items push basket size instead of order count. Metric: items per order during the draw, repeat orders from the same customer within the week.

Follow for more breakdowns like this."""),

 dict(brand='Arntreal', shot='41.png', text="""Worth stealing #0: Arntreal's empty slot.

The Black Friday offer (translated): "1 bought = 1 free. 2 bags, the 2nd one free, colour of your choice." Next to the bag you picked sits a dashed, greyed-out bag with a "+": "Choose your free bag".

Why it works:
· The empty slot is a task half done. You picked one bag, the page shows the second place waiting. That's the endowed progress effect: people push harder toward a goal they feel they've already started (Nunes and Drèze, 2006).
· Based put its buy-one-get-one in the button (#3). Arntreal draws it: the free bag is a picture, not a line of text.
· The offer is pre-selected and framed; the single bag above it, at the same €149.90, reads like the worse deal.
· "Colour of your choice" makes the free bag a decision, not a leftover.

The smart part: you don't read about a gift, you look at a gap in your order.

What I'd test next:
The crossed-out price. It shows €149.90 struck through next to €149.90: no visible saving. It should read €299.80 struck through, or "2 bags for €149.90, €74.95 each".
Or simpler: once the free bag's colour is picked, show "€149.90 saved" in green.

Hypothesis: a visible saving turns "nice offer" into "I lose €149.90 if I skip it". Metric: share of orders taking the 2-bag offer, add-to-cart rate.

Follow for more breakdowns like this."""),

 dict(brand='Boku', shot='38.webp', text="""Worth stealing #0: Boku's three percentages.

A product image, not a review block (translated): "Tested under dermatological control". Then: 95% of users find it improves hygiene, 97% of women users find it improves hygiene during periods, 98% find it pleasant to use. The bottle rests on an open hand.

Why it works:
· Each number answers a different doubt: does it work, does it work for me, is it unpleasant to use.
· The middle figure names a use most brands in this category stay vague about. The women it concerns see themselves in it at once.
· The claims are worded as perception ("find that"), which is what a user survey can honestly measure.
· The hand gives the scale: you see it's portable before reading a word.

The smart part: in an awkward category, the numbers ask the question so the shopper doesn't have to.

What I'd test next:
Make the numbers checkable. Without a base, 95% could mean 19 people out of 20. "95% of [n] users, after [x] weeks", with their real figures, turns a claim into a result.
Or simpler: one line of small print under the title with the study size and length.

Hypothesis: a stated sample size makes the same percentages more believable. Metric: add-to-cart rate after viewing this image, review taps after viewing it.

Follow for more breakdowns like this."""),

 dict(brand='Based', shot='42.png', text="""Worth stealing #0: Based's ingredient tiles.

A product image: "The Key Ingredients. Endless Benefits." Four tiles, each with an ingredient name, a strip of the raw powder's texture, and one line on what it does for your hair.

Why it works:
· You see the ingredients, not just their names. Silica, arrowroot, rice powder and mica each get a texture you can almost touch.
· Every chemical name is translated into a result: volume, less oil, softness, a matte finish.
· Four ingredients, four jobs. Nothing is listed without a reason to be there.
· The footer packs three trust cues: science-backed, naturally derived, formulated and filled in the USA.

The smart part: this image answers the question a €21.95 product weighing 2.5 g raises: what exactly am I paying for? Four named actives make a small format feel dense instead of tiny.

What I'd test next:
Start from the problem instead of the ingredient: "Flat hair? Silica silylate. Oily roots by noon? Arrowroot." Shoppers know their problem, not the ingredient.
And for EU shoppers, "filled in the USA" raises a delivery question: say where it ships from and how long it takes.

Hypothesis: problem-first tiles help shoppers recognise themselves, and buy. Metric: add-to-cart rate after viewing this image, gallery swipes.

Follow for more breakdowns like this."""),

 dict(brand='Arntreal', shot='40.png', text="""Worth stealing #0: Arntreal's proof before the promise.

Above the product name, before anything else: five stars, "Over 100,000 bags sold" with a French flag, and five small customer photos (translated).

Why it works:
· Most pages go product, promise, then reviews at the bottom. Arntreal flips it: proof, promise, product.
· The bold claim that follows ("Everything of a luxury bag. Except the price.") lands on a crowd that already bought.
· Faces turn 100,000 into people. A number is abstract; five faces are someone like you.
· The flag answers "who's behind this?" with one small icon.

The smart part: the first thing your eye hits is "other people did this". The pitch comes second, already backed.

What I'd test next:
The stars have no rating and no count. "Over 100,000 bags sold" is a sales figure, not a review figure, so five stars with nothing next to them can read as decoration. I'd show the real average and the number of reviews, and make the stars jump to them.
Or simpler: make the five faces tappable, each opening that customer's photo review.

Hypothesis: proof you can check beats proof you have to trust. Metric: taps on the rating, conversion of visitors who open reviews.

Follow for more breakdowns like this."""),
 dict(brand='Based', shot='new:based-cart', text="""Worth stealing #0: Based's cart, built like a game.

Open the cart during the buy-one-get-one: "Your haul. 1 pick, 0 free." A big gold "€255.76 left", "€277 max per order", a progress bar, and next to your item, a dashed slot marked "FREE".

Why it works:
· The words come from unboxing videos: "haul", "picks". The cart talks like the people who buy.
· "BOGO savings €0.00" in gold. A zero you're invited to fix.
· The dashed free slot is the same endowed-progress trick as Arntreal's empty bag (#4): one pick in, one place waiting.
· The cap does more than stop resellers. Purchase limits signal value: in a classic study, "limit 12 per person" signs raised the quantity people bought (Wansink, Kent and Hoch, 1998).

The smart part: Based put the offer in the button (#3), then turned the cart into a scoreboard.

What I'd test next:
The biggest number in the cart is "€255.76 left", a budget nobody planned. The bar measures the distance to the cap, not to the next reward. I'd make the next step the headline: "Pick 1 more, it's free", and keep the cap in small print.
Or simpler: swap "BOGO savings €0.00" for "Add 1 pick, save €21.95".

Hypothesis: shoppers respond to the next step, not to the remaining budget. Metric: share of carts with 2 picks or more, items per order.

Follow for more breakdowns like this."""),

 dict(brand='HOLY', shot='new:holy-cart', text="""Worth stealing #0: HOLY's cart, one cent short.

The cart has a reward bar with steps from €49 to €200. Under it (translated): "You'll now receive Cap + Shaker. Only €0.01 left for the blue Thermo Shaker."

Why it works:
· Unlocked gifts sit in the cart as real lines: "Free!", the crossed-out value, "Gift unlocked" in green. You can see what you'd lose by removing items.
· The next gift waits right below: "Free from €100.00", with a padlock.
· The bundle costs €99.99. One cent from the next reward is the strongest possible pull: people speed up as a goal gets closer (Kivetz, Urminsky and Zheng, 2006).
· Shipping shows "Free", so the bar is only about gifts.

The smart part: a charm price (€99.99) sitting one cent under a round threshold (€100). Planned or not, the hero product lands right before the next reward.

What I'd test next:
Two things. "Total savings -€33.97" only counts the two gifts. With the bundle discount (€119.97 down to €99.99), the real figure is €53.95. They undersell their own deal by €19.98.
And the one cent can read as a trick. I'd test rounding in the shopper's favour: unlock the shaker at €99.99 and say "We rounded up for you".

Hypothesis: a generous gesture at €0.01 earns more goodwill than the extra item earns money. Metric: conversion and average order value, both versions.

Follow for more breakdowns like this."""),

 dict(brand='Fincut', shot='new:fincut-cart', text="""Worth stealing #0: Fincut's tickets in the cart.

Fincut runs a Black Friday draw for 3 cars (translated): "Each item bought = 1 ticket." In the cart, the tickets aren't a banner. They're a line item: "Ticket, Grand Jeu. Free. x3".

Why it works:
· The entries sit in the cart like things you own. Remove a t-shirt, lose a ticket. People value what they already hold more than what they could get (the endowment effect, Kahneman, Knetsch and Thaler, 1990).
· The free shirt of the 3+1 pack earns no ticket: 4 shirts, 3 tickets. The rule holds, "each item bought".
· The shipping bar is already full: "Congratulations, you get free delivery".
· The first add-on suggested is a €9 gift box, the one that matches the season a month before Christmas.
· The button carries the price and the old one, and the last line repeats "You save €28 on this cart".

The smart part: the draw lives where the decision happens. Nobody has to remember a homepage banner.

What I'd test next:
The code. A black banner says "Code BLACK20: -20% on your cart, enter it in 'Promo code'". That field is collapsed at the bottom, and the €84 total doesn't include it yet. Why make shoppers type a code the cart already knows? I'd apply it automatically. And say whether it stacks with the pack, already at -25%.
Or simpler: a one-tap "Apply" on the banner.

Hypothesis: every code shoppers must type is a chance to leave and look for a better one. Metric: share of orders using BLACK20, checkout completion.

Follow for more breakdowns like this."""),

 dict(brand='Cabaia', shot='new:cabaia-product', text="""Worth stealing #0: Cabaia's sizes in litres.

A backpack page (translated): "Size: Medium, 18L. Large, 23L", with a "Compare sizes" link right above the two buttons.

Why it works:
· Litres are the right unit for a bag. "Medium" means nothing until you know what fits.
· Every colour swatch is a photo of the bag with its matching pouch, not a flat dot. You see the whole product in each colourway.
· The price lives in the button: "Add, €53.40".
· Under €100, the badge leads with the percentage (-40%) rather than the euros: the rule of 100 from #1, applied right.

The smart part: size, capacity and a comparison link on one line. "Will it be big enough?" is answered before it's asked.

What I'd test next:
Turn litres into objects. Most people can't picture 18 litres. "18L: a 14-inch laptop, a jumper and a water bottle. 23L: add a pair of trainers", if that's what actually fits.
Or simpler: show the "Compare sizes" answer inline, under the two buttons, instead of behind a link.

Hypothesis: shoppers who can picture the capacity pick the right size first time. Metric: add-to-cart rate, exchanges between Medium and Large.

Follow for more breakdowns like this."""),

 dict(brand='Cabaia', shot='new:cabaia-cart', text="""Worth stealing #0: Cabaia's cart, ready for December.

One backpack in the cart, and the last three questions answered before checkout (translated).

Why it works:
· When will it arrive? "In stock. Delivered Thursday 26 Nov", with the shopper's postcode and a link to compare delivery options. A date, not "3 to 5 business days".
· Is it a gift? A checkbox on the line itself: "Gift wrap (€2.80)". The fix for friction #41, gift options hidden until checkout.
· What goes with it? The suggestions include "Side pocket Pau, €7", and the backpack is called "Pau" too. Products named after cities make the match obvious without a "goes with" label.
· Free delivery is confirmed right above a checkout button that repeats the price.

The smart part: in December, the delivery date is the decision. Putting it in the cart, with your own postcode, removes the last "will it arrive in time?".

What I'd test next:
Make the gift option complete: once "Gift wrap" is ticked, offer a gift message and a receipt without prices.
Or simpler: a cutoff next to the date, "Order before 2pm for Thursday", if that's their real cutoff.

Hypothesis: a complete gift option turns more December carts into orders. Metric: gift wrap take-up, December conversion rate.

Follow for more breakdowns like this."""),
]

# Ordre de publication à 13h (24 novembre + rang - 1). Les offres Black Friday tombent pendant la semaine du Black Friday.
ORDER = ['9.webp', '39.png', '30.png', '41.png', 'new:based-cart', '33.png', 'new:holy-cart', 'new:fincut-cart',
         '16.png', '19.webp', '15.png', '12.webp', '10.png', '14.png', '18.png', '13.webp', '17.webp', 'new:cabaia-product',
         '38.webp', '22.png', '11.png', '20.png', '23.webp', 'new:cabaia-cart', '24.webp', '25.png', '27.png', '42.png',
         '28.webp', '29.png', '32.png', '37.png', '26.png', '40.png', '34.png', '35.png', '36.png', '31.png']
assert sorted(ORDER) == sorted(p['shot'] for p in WS) and len(set(ORDER)) == len(ORDER)
WS = sorted(WS, key=lambda p: ORDER.index(p['shot']))

import re as _re
for _i, _p in enumerate(WS, 1):
    _p['text'] = _re.sub(r'^Worth stealing #\d+:', f'Worth stealing #{_i}:', _p['text'])

if __name__ == '__main__':
    import re
    for i, p in enumerate(WS, 1):
        t = p['text']
        assert t.startswith(f'Worth stealing #{i}: '), (i, t[:30])
        assert '–' not in t and '—' not in t, i
        assert not re.search('[\U0001F000-\U0001FFFF☀-➿]', t), i
        assert t.endswith('Follow for more breakdowns like this.'), i
    print(len(WS), 'posts ;', 'longueurs :', [len(p['text']) for p in WS])
