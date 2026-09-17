# VERZO Sales Agent

Scaffold for a Claude Code-driven outbound sales agent for VERZO Studio.
This is a V1 skeleton: prompts + CRM schema + operating rules. It is not
wired to live MCP servers yet — that's the next step, done outside this repo
(MCP server config is per-machine/per-Claude-Code-project, not code to check
in here).

## Structure

```
verzo-sales-agent/
├── CLAUDE.md          # persistent instructions for the agent (read this first)
├── data/
│   └── icp.md         # ideal customer profile / qualification criteria
├── prompts/
│   ├── sourcing.md         # step 1: find candidate companies
│   ├── qualification.md    # step 2-6: research, score, decide who to contact
│   ├── personalization.md  # step 7-9: draft outreach for leads scoring > 75
│   └── followup.md         # daily follow-up + reply handling
├── leads/              # local exports/snapshots of CRM data (gitignored-ish; keep small)
└── outputs/            # generated audits, drafts, reports
```

## Required MCP servers (set up in your Claude Code config, not in this repo)

1. **Web search** — for sourcing companies, verifying facts, finding triggers.
2. **Browser** — for opening and analyzing prospect websites.
3. **CRM** — Airtable or Supabase, with the `leads` table below.
4. **Gmail** — read (check replies) + draft. Sending requires human approval
   for every message; do not grant an always-send scope.

## CRM schema — `leads` table

| field              | type                                              |
|--------------------|----------------------------------------------------|
| id                 | auto                                                |
| company            | text                                                |
| website            | url                                                 |
| industry           | text                                                |
| employees          | number                                              |
| country            | text                                                |
| decision_maker     | text                                                |
| role               | text                                                |
| linkedin           | url                                                 |
| email              | text                                                |
| website_score      | number (0-100)                                      |
| business_trigger   | text                                                |
| opportunity        | text                                                |
| total_score        | number (0-100)                                      |
| status             | enum: NEW, QUALIFIED, CONTACTED, REPLIED, INTERESTED, CALL, PROPOSAL, WON, LOST |
| last_contact       | date                                                |
| next_followup      | date                                                |
| followup_count     | number                                              |
| email_draft        | long text                                           |
| linkedin_draft     | long text                                           |
| created_at         | date (auto)                                         |

## Operating rules (also in CLAUDE.md)

- Never invent names, emails, company facts, or business events — publicly
  verifiable info only.
- Only leads scoring > 75 get personalized outreach.
- Claude can draft; Claude never sends without explicit human approval.
- Max ~5 minutes of research per cold lead. No prototypes for cold leads
  unless explicitly requested.

## Suggested first run

Test with ~20 target companies end-to-end (sourcing → qualification →
personalization → CRM) before scaling volume. Validate that the qualification
scores and drafts are good enough with minimal manual correction, then
increase volume and only then consider adding the "Website Auditor"
(automated audit page generation) described in the original plan.
