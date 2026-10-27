# Solen benchmark crawler

Collects FEATURES (not text, not images) of public product pages, to answer one question: what do real stores put on a product page? Runs every night on GitHub Actions, so it does not need your computer.

- `crawl.py`: reads `seeds.txt`, samples 5 product pages per domain from its sitemap, stores features.
- `aggregate.py`: turns them into store-level statistics (`stats.json`, `stats.md`).
- `test_local.py`: offline test against a fake store. Run: `python3 tools/benchmark/test_local.py`.
- `.github/workflows/benchmark.yml`: the nightly job. Data goes to the branch `benchmark-data`.

## Rules the crawler follows

Clear User-Agent with a contact address, `robots.txt` read first and obeyed (including Crawl-delay), 1 request per domain every 1.5 s at least, a 401/403/429 marks the domain "blocked" and leaves it alone. Nothing is worked around.

## Set up

1. Merge this code into the default branch (scheduled workflows only run from there).
2. In the ntfy app, subscribe to the topic written in `.github/workflows/benchmark.yml` (`solen-jhh607v7l91uh7rti9gz`). No secret to configure. The repository is public, so this topic name is public too: it only carries crawl summaries.
3. Actions tab, "benchmark-crawl", Run workflow, to start the first run by hand.

## Rule for anything you publish

Quote only numbers from `stats.json`. "We analysed N product pages" must use the real N from the file.
