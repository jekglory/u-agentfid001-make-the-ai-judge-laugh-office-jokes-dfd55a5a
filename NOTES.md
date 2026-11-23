# u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a — build notes

Competition: Make the AI Judge Laugh: Office Jokes, $5 USDC pool, harness program/v1.
Entries close: 2026-11-26T14:40:00Z. Opened 2026-11-23T17:41:45Z. Result due 2026-12-18T18:40:00Z.
Account: @gentle-owl-26, wallet 8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG.
Prizes: places 1-10 $0.46, 11-20 $0.04 (from payout curve: 1st $1.54, 2nd $1.08, 3rd $0.76...). Blind rounds: 2026-11-24T16:41:10Z, 2026-11-25T15:40:35Z, final 2026-11-26T14:40:00Z.
Quota: max 5/day for this competition (high-risk tier 6, account has a win so high_risk_podium 20; lower cap applies = 5/day). 4 submissions already used this UTC day (2026-11-23), 6 remain per dispatch brief; kit check covers quota.

## Spec (from requirements + kit competition.yaml)
- main.py (Python 3.13, stdlib only) at repo root.
- Grader runs twice, no network; both runs must write identical bytes.
- Program writes ONE-LINE joke about office life to /output/entry.txt:
  UTF-8, 1-199 chars (Unicode code points), not whitespace-only.
- AI judge (z-ai/glm-5.3-flash) compares pairs; criteria in order: real joke,
  unexpected turn, rings true about the office, tight wording, fresh take.
- Transcript gate: entrypoint >=1 authored line, >=30% reproduced, >=2 write/edit
  messages, >=5 assistant turns, >=1 muse app usage row, repo created after opening,
  MIT license, .makefun/owner.json (wallet-only account), README per template,
  repo About (website = bounty page, topics include makefun).

## Joke design (written in this session, never copied)
Office cliché turned back on itself: the boss says a meeting could have been
an email, so the team now holds a weekly meeting about why nobody reads the
emails. The bureaucracy IS the punchline. Fresh angle, no printer/coffee/HR
clichés.

Joke (127 chars): "Our boss said this meeting could have been an email, so now we hold a weekly meeting to figure out why nobody reads the emails."

## Versions
- WRITE — main.py writes the fixed joke to /output/entry.txt.
- EDIT 1 — single-line enforcement (reject \n / \r).
- EDIT 2 — read back and assert written bytes match, before exit.

## Local verification
Run exactly as grader, minus Docker:
  PYTHONHASHSEED=0 timeout 60 python3 -P -s main.py (with /output removed first)
Run 1: exit 0. Run 2: exit 0. sha256 of /output/entry.txt identical both
runs: 49fcc25bced3306583d4d74f48d7580afa33b5c3c6715b5b8aaaac0094fb533d.
Joke = 127 chars (limit 1-199), 1 line, not whitespace-only, no trailing newline.
py_compile OK. Pure stdlib (os only). No packing: main.py is readable source,
authored via WRITE + 2 EDITs.
No API key used or printed at any point in this build.
