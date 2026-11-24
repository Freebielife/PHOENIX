# Phoenix Observatory

## О проекте / токене

AI-powered ecosystem of services for earning, work, games, and entertainment.

Самоописание из метаданных токена; заявления проекта не проверены независимо.

Источники (проверены 2026-11-24):

- <https://tonapi.io/v2/jettons/EQABtSLSzrAOISWPfIjBl2VmeStkM1eHaPrUxRTj8mY-9h43>

Generated from https://github.com/Freebielife/TON-Observatory-Template.

Run python3 -m scripts.refresh_observatory; python3 build.py; python3 verify.py.
Publish index.html in TON Sites only after independent on-chain verification.
Live snapshot sections retain their last successful data; missing sections remain explicitly unavailable.
Only native TON swap pairs supported. Locks, staking and custom project NFT badges are configured through project.json and verified against TonAPI.
Configure your GitHub workflow scheduler before launch.

Foundation version: 1.3.0. Holders show 10, expandable to top 20.
`project.json` is the per-project specification. Contract/pool/precision changes require regenerating from the factory; do not reuse another token's snapshot.
Run `python3 build.py` for an atomic bundle and `build/report.json` size report.
No external fonts, scripts or images are needed to render the saved page. Fresh data checks and manual wallet lookups require network access.
Cloudflare dispatch registration and GitHub repository access remain separate deployment steps. No credentials go into HTML.

## Phoenix configuration

Logo and section flag: user-supplied Phoenix image. Hero: orange/red.
DEXes: STON.fi and DeDust, verified direct PHXPW/TON swaps.
Common OG, +888, four-digit TON DNS and burn badges plus VNUK, Joystick,
Phoenix, ARNI, NAPIWAS and 🥚 NFT. DEV, Author NFT and JVault excluded.

GitHub Actions fallback schedule: every 30 minutes at :17/:47 UTC, subject to
GitHub scheduling delays. The shared Cloudflare runner has not been modified.
TON Storage publication is a separate step and is not claimed by this repository.
