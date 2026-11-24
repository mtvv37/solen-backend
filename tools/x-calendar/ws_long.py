"""Format long de la série Worth stealing : 900 caractères maximum (au-delà de 280, X Premium), puces en tiret simple."""

TEMPLATE = """Worth stealing #1: [Brand]'s [feature].

Really like how [Brand] handles [feature] on mobile.

Why it works:
- [what the shopper sees]
- [the question it answers before they ask]
- [the friction it removes]
- [how it backs up the offer or the brand]

The smart part: [one insight, in one or two sentences].

What I'd test next:
[one idea, framed as a test]
Or simpler: [a smaller version of the same idea].

Hypothesis: [who it helps and why]. Metric: [what to watch].

Follow for more."""

EXAMPLE = """Worth stealing #1: [Brand]'s size picker.

Really like how [Brand] handles sizing on mobile.

Why it works:
- Every size is visible at once. No dropdown to open.
- Sold-out sizes stay on screen, greyed out, so you know they exist.
- A short fit note sits right under the sizes: "Runs small, size up if you're between two."
- Add to cart stays inactive until a size is picked, so nobody adds the wrong one by accident.

The smart part: it answers "which size do I take?" at the exact moment the shopper decides, without sending them to a size chart.

What I'd test next:
A "Between two sizes?" link that opens the fit guide in a drawer, right where you are.
Or simpler: show the model's height and the size they wear next to the sizes.

Hypothesis: fewer shoppers leave the page to check sizing. Metric: mobile add-to-cart rate, and size-related returns.

Follow for more."""

if __name__ == '__main__':
    for name, t in (('TEMPLATE', TEMPLATE), ('EXAMPLE', EXAMPLE)):
        assert '–' not in t and '—' not in t, name
        print(name, len(t), 'caractères ; les 2 premières lignes :', repr(t.split('\n\n')[0]))
