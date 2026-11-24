# RRA Analysis Report — 2026-05-15

- **Data as-of:** 2026-05-15
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-05-15_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 26** | **IMPROVING: 8** | **WEAKENING: 10** | **LAGGING: 52**

> Weekly read: Commodity/energy leadership entrenched — 15 tickers perfect 12/12 (USO/XLE/XOP/FCG/COMT/DBC/WEAT) in a LAGGING-heavy tape (52); the arc's peak-extension week.
> The tell the quadrant counts hide: every consistent leader is already heading ↙ — position intact, direction deteriorating.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (8)**<br>• Energy/commodity: `CORN`↙<br>• Defensive/rate-sensitive: `TLT`↙ `XLU`↙<br>• Financials/REITs: `IYR`↙<br>• Growth/mega-cap tech: `ARKK`↗ `IWF`↗ `VOT`↗<br>• EM/Intl: `EWA`↙ | **LEADING (26)**<br>• Energy/commodity: `BCD`↙ `CANE`↘ `COMT`↙ `DBC`↙ `FCG`↙ `FTGC`↙ `IEO`↙ `SOYB`↙ `USO`↘ `VDE`↙ `WEAT`↙ `XLE`↙ `XOP`↙<br>• Metals/hard-asset: `SMOG`↙<br>• Financials/REITs: `SCHH`↙<br>• Growth/mega-cap tech: `CIBR`↗ `CLOU`↗ `QQQ`↗ `SMH`↗ `XLK`↗<br>• Clean energy: `ICLN`↙ `PBW`↗ `QCLN`↗<br>• EM/Intl: `EWY`↗<br>• Transports/infra/industrials: `GRID`↙ `IFRA`↙ |
| **< 100** | **LAGGING (52)**<br>• Energy/commodity: `NANR`↙ `UNG`↙<br>• Metals/hard-asset: `COPX`↙ `CPER`↙ `DBB`↙ `GDX`↙ `GLD`↙ `PALL`↙ `PLTM`↘ `SLV`↘ `XME`↙<br>• Healthcare: `IBB`↙ `IHI`↙ `VHT`↙ `XBI`↙ `XLV`↙ `XPH`↙<br>• Defensive/rate-sensitive: `HYG`↙ `ITB`↙ `JNK`↙ `SGOV`↙ `XLP`↙<br>• Value/dividend/consumer: `IWD`↙ `VBR`↙ `VOE`↙ `VTV`↙ `XLB`↙ `XLY`↙ `XRT`↙<br>• Financials/REITs: `IAI`↘ `IYF`↙ `KRE`↙ `XLF`↙<br>• Growth/mega-cap tech: `AWAY`↗ `DIA`↙ `HERO`↘ `XLC`↙ `XSW`↗<br>• EM/Intl: `EFA`↙ `EWC`↙ `EWJ`↙ `EWZ`↙ `FXI`↙ `INDA`↖ `VGK`↙ `VNM`↗ `VXUS`↙<br>• Transports/infra/industrials: `IYT`↙ `JETS`↙ `XAR`↘ `XLI`↙ `XTN`↙ | **WEAKENING (10)**<br>• Energy/commodity: `XES`↙<br>• Metals/hard-asset: `BATT`↙ `LIT`↙ `REMX`↙ `SLX`↙<br>• Growth/mega-cap tech: `IWM`↙ `VBK`↙<br>• Clean energy: `TAN`↙<br>• EM/Intl: `EEM`↙<br>• Other: `AMLP`↙ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XOP | LEADING | 115.67 | 115.41 | 10.4 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| FCG | LEADING | 112.52 | 109.94 | 9.7 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| IEO | LEADING | 113.46 | 112.64 | 9.2 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| VDE | LEADING | 108.26 | 101.98 | 8.9 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| XLE | LEADING | 107.43 | 100.91 | 8.8 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| USO | LEADING | 173.58 | 170.11 | 7.1 | DECELERATING | ↘ | TEMPORARY | 12 | 0 | 100.0 |
| COMT | LEADING | 123.29 | 120.55 | 5.0 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| FTGC | LEADING | 113.01 | 108.55 | 4.7 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| IFRA | LEADING | 101.86 | 100.86 | 4.4 | ACCELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| DBC | LEADING | 119.54 | 114.00 | 4.4 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |

> Read: 15 perfect leaders, all hard assets or income — the full energy/ag/commodity complex (USO/XLE/XOP/FCG/COMT/DBC/WEAT/FTGC) plus infrastructure (IFRA/GRID) and REITs (SCHH); zero growth or healthcare names. The anomaly in the Heading column: all 10 shown head ↙ — even entrenched leaders are rotating down-left. A fully mature commodity regime.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| EWA | IMPROVING | 98.78 | 103.36 | 7.0 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| ARKK | IMPROVING | 96.30 | 109.18 | 5.1 | ACCELERATING | ↗ | TEMPORARY | 0 | 8 | 0.0 |
| XLU | IMPROVING | 99.14 | 111.00 | 3.8 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| TLT | IMPROVING | 92.70 | 100.59 | 3.0 | ACCELERATING | ↙ | TEMPORARY | 6 | 0 | 50.0 |
| IYR | IMPROVING | 99.21 | 103.43 | 2.8 | DECELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| CORN | IMPROVING | 99.87 | 105.57 | 2.1 | ACCELERATING | ↙ | TEMPORARY | 9 | 1 | 75.0 |
| IWF | IMPROVING | 99.59 | 102.91 | 2.1 | ACCELERATING | ↗ | TEMPORARY | 0 | 10 | 0.0 |
| VOT | IMPROVING | 97.17 | 103.96 | 0.7 | ACCELERATING | ↗ | TEMPORARY | 0 | 0 | 0.0 |

> Read: Heading data cuts the 8-deep bench to three genuine improvers — ARKK +5.1, IWF +2.1, VOT +0.7, all ↗. The rest are breakdowns in disguise: EWA (-3.53 ratio), XLU, CORN and IYR are ↙-heading regime breaks out of LEADING, and TLT is fading ↙ too. No successor regime yet — speculative flickers only.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XES | WEAKENING | 120.31 | 99.54 | 8.0 | DECELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| SLX | WEAKENING | 103.90 | 87.14 | 4.4 | ACCELERATING | ↙ | TEMPORARY | 6 | 0 | 50.0 |
| REMX | WEAKENING | 107.76 | 87.24 | 4.2 | DECELERATING | ↙ | TEMPORARY | 9 | 0 | 75.0 |
| BATT | WEAKENING | 104.02 | 93.05 | 3.2 | DECELERATING | ↙ | TEMPORARY | 1 | 0 | 8.3 |
| AMLP | WEAKENING | 103.56 | 98.25 | 3.0 | DECELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| EEM | WEAKENING | 104.01 | 99.26 | 2.6 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| LIT | WEAKENING | 114.67 | 97.18 | 2.3 | ACCELERATING | ↙ | TEMPORARY | 0 | 0 | 0.0 |
| TAN | WEAKENING | 104.93 | 95.26 | 2.2 | ACCELERATING | ↙ | TEMPORARY | 5 | 0 | 41.7 |
| IWM | WEAKENING | 100.37 | 97.02 | 1.8 | DECELERATING | ↙ | TEMPORARY | 10 | 0 | 83.3 |
| VBK | WEAKENING | 100.64 | 98.13 | 0.4 | DECELERATING | ↙ | TEMPORARY | 10 | 0 | 83.3 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XOP | LEADING | 115.67 | 115.41 | 10.4 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| FCG | LEADING | 112.52 | 109.94 | 9.7 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| IEO | LEADING | 113.46 | 112.64 | 9.2 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| VDE | LEADING | 108.26 | 101.98 | 8.9 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| XLE | LEADING | 107.43 | 100.91 | 8.8 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| USO | LEADING | 173.58 | 170.11 | 7.1 | DECELERATING | ↘ | TEMPORARY | 12 | 0 | 100.0 |
| COMT | LEADING | 123.29 | 120.55 | 5.0 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| FTGC | LEADING | 113.01 | 108.55 | 4.7 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| DBC | LEADING | 119.54 | 114.00 | 4.4 | DECELERATING | ↙ | TEMPORARY | 12 | 0 | 100.0 |
| SMH | LEADING | 127.32 | 110.01 | 4.0 | DECELERATING | ↗ | TEMPORARY | 10 | 0 | 83.3 |

> Read: 10 weakening incl. the metals/EV-chain early casualties (BATT/LIT/REMX/SLX/XES) — and XES/AMLP/EEM are 10-11w leaders crossing LEADING->WEAKENING, regime aging inside the complex itself. Both tables are uniformly ↙ except SMH (↗): the top decelerators ARE the leaders (XOP 10.4D, FCG 9.7D, IEO 9.2D, VDE 8.9D) — the regime is topping from within.

## 5. Quadrant Crossings

21 crossings this week: **12 confirmed / 9 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 8x WEAKENING->LAGGING, 4x LEADING->IMPROVING, 3x IMPROVING->LEADING, 3x LEADING->WEAKENING, 1x IMPROVING->LAGGING, 1x LEADING->LAGGING, 1x WEAKENING->LEADING. 1 diagonal/discontinuous transition.

### Counter-clockwise — abrupt reversals

**LEADING->IMPROVING** — potential regime break / RS breakdown warning

- `EWA` CONFIRMED — ↙, Δratio -3.53, Δmom -6.03 (landed ratio 98.78, 1.22 past boundary); quadrant_persistence TEMPORARY
- `XLU` PROVISIONAL_CROSSING — ↙, Δratio -2.86, Δmom -2.54 (landed ratio 99.14, only 0.86 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `IYR` PROVISIONAL_CROSSING — ↙, Δratio -1.49, Δmom -2.35 (landed ratio 99.21, only 0.79 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `CORN` PROVISIONAL_CROSSING — ↙, Δratio -2.05, Δmom -0.38 (landed ratio 99.87, only 0.13 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**IMPROVING->LAGGING** — failed recovery / bearish continuation

- `SGOV` CONFIRMED — ↙, Δratio -1.15, Δmom -2.00 (landed mom 98.90, 1.10 past boundary); quadrant_persistence TEMPORARY

**WEAKENING->LEADING** — possible re-acceleration — verify follow-through

- `PBW` CONFIRMED — ↗, Δratio +3.64, Δmom +3.30 (landed mom 102.63, 2.63 past boundary); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**IMPROVING->LEADING** — possible rotation into leadership — confirm next week

- `CLOU` CONFIRMED — ↗, Δratio +5.94, Δmom +9.09 (landed ratio 101.65, 1.65 past boundary); quadrant_persistence TEMPORARY
- `CIBR` CONFIRMED — ↗, Δratio +6.47, Δmom +5.82 (landed ratio 101.64, 1.64 past boundary); quadrant_persistence TEMPORARY
- `CANE` PROVISIONAL_CROSSING — ↘, Δratio +2.33, Δmom -0.24 (landed ratio 100.54, only 0.54 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LEADING->WEAKENING** — potential distribution / early reversal — watch

- `AMLP` CONFIRMED — ↙, Δratio -0.12, Δmom -2.98 (landed mom 98.25, 1.75 past boundary); quadrant_persistence TEMPORARY
- `XES` PROVISIONAL_CROSSING — ↙, Δratio -5.64, Δmom -5.72 (landed mom 99.54, only 0.46 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `EEM` PROVISIONAL_CROSSING — ↙, Δratio -1.83, Δmom -1.91 (landed mom 99.26, only 0.74 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**WEAKENING->LAGGING** — potential bearish continuation — confirm persistence

- `XLB` CONFIRMED — ↙, Δratio -4.04, Δmom -6.10 (landed ratio 96.08, 3.92 past boundary); quadrant_persistence TEMPORARY
- `XTN` CONFIRMED — ↙, Δratio -4.75, Δmom -4.71 (landed ratio 97.39, 2.61 past boundary); quadrant_persistence TEMPORARY
- `IYT` CONFIRMED — ↙, Δratio -3.46, Δmom -2.88 (landed ratio 96.89, 3.11 past boundary); quadrant_persistence TEMPORARY
- `VXUS` CONFIRMED — ↙, Δratio -1.94, Δmom -2.80 (landed ratio 98.56, 1.44 past boundary); quadrant_persistence TEMPORARY
- `XBI` CONFIRMED — ↙, Δratio -2.22, Δmom -1.40 (landed ratio 98.40, 1.60 past boundary); quadrant_persistence TEMPORARY
- `NANR` PROVISIONAL_CROSSING — ↙, Δratio -3.37, Δmom -7.67 (landed ratio 99.81, only 0.19 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `EWC` PROVISIONAL_CROSSING — ↙, Δratio -1.42, Δmom -2.07 (landed ratio 99.11, only 0.89 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `IWD` PROVISIONAL_CROSSING — ↙, Δratio -1.37, Δmom -2.07 (landed ratio 99.26, only 0.74 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

### Diagonal — discontinuous

**LEADING->LAGGING** — discontinuous regime change — investigate

- `EWZ` CONFIRMED — ↙, Δratio -8.82, Δmom -11.13 (landed ratio 97.16, mom 89.10, 2.84/10.90 past boundary); quadrant_persistence TEMPORARY

> Read: the tape turned one-directional — 14 of 21 crossings run clockwise (normal rotation) but the content is bearish: an 8-name WEAKENING->LAGGING breakdown wave (XLB/XTN/IYT/VXUS/XBI confirmed; NANR/EWC/IWD provisional — NANR only 0.19 past the line) plus AMLP/XES/EEM aging out of LEADING. The counter-clockwise side carries the real regime breaks: EWA's LEADING->IMPROVING is CONFIRMED 1.22 past the boundary while XLU/IYR/CORN are PROVISIONAL whipsaw-watch names (CORN just 0.13 past — could flip back). The genuine bullish flow is narrow — CLOU and CIBR confirmed IMPROVING->LEADING rotations plus PBW's WEAKENING->LEADING re-acceleration — while EWZ's LEADING->LAGGING diagonal (2.84/10.90 past both boundaries) is the week's discontinuous crash.

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| UNG | LAGGING | 18.6 | ACCELERATING | ↙ | TEMPORARY | 78.24 |
| EWZ | LAGGING | 14.2 | ACCELERATING | ↙ | TEMPORARY | 89.10 |
| CLOU | LEADING | 10.9 | ACCELERATING | ↗ | TEMPORARY | 109.94 |
| XOP | LEADING | 10.4 | DECELERATING | ↙ | TEMPORARY | 115.41 |
| FCG | LEADING | 9.7 | DECELERATING | ↙ | TEMPORARY | 109.94 |
| IEO | LEADING | 9.2 | DECELERATING | ↙ | TEMPORARY | 112.64 |
| GDX | LAGGING | 9.1 | DECELERATING | ↙ | TEMPORARY | 69.88 |
| VDE | LEADING | 8.9 | DECELERATING | ↙ | TEMPORARY | 101.98 |
| XLE | LEADING | 8.8 | DECELERATING | ↙ | TEMPORARY | 100.91 |
| CIBR | LEADING | 8.7 | ACCELERATING | ↗ | TEMPORARY | 107.47 |

Dead money (velocity < 1.0): `ICLN` 0.16, `EWY` 0.19, `VBK` 0.44, `VOT` 0.68

> Read: Velocity polarity is stark — UNG +18.6 and EWZ +14.2 look fast but head ↙: accelerating deeper into LAGGING (EWZ's LEADING->LAGGING is a discontinuous crash), sells not buys. The genuine bid is CLOU +10.9 and CIBR +8.7, both ↗ into LEADING. Of 21 crossings ~16 are bearish: regime breaks (EWA/XLU/IYR/CORN) plus a broad WEAKENING->LAGGING breakdown wave across small-caps/value/international (IWM/IYT/XLB/XTN/VXUS/EWC/IWD/XBI/NANR).

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| AWAY | 84.59 | 94.55 | 2.0 | 12 | 0.0 |
| IHI | 77.92 | 81.98 | 1.9 | 12 | 0.0 |
| INDA | 88.49 | 96.89 | 2.2 | 12 | 0.0 |
| XSW | 89.38 | 99.64 | 8.4 | 12 | 0.0 |
| VHT | 87.85 | 85.10 | 1.7 | 11 | 0.0 |
| XLV | 87.16 | 84.28 | 2.0 | 10 | 0.0 |
| FXI | 87.66 | 92.79 | 2.4 | 9 | 0.0 |
| XLY | 92.43 | 92.74 | 1.0 | 9 | 0.0 |
| IAI | 91.63 | 88.39 | 1.1 | 8 | 0.0 |
| IYF | 90.64 | 90.67 | 2.0 | 8 | 0.0 |

> Read: 52 LAGGING — the majority of the universe — in four buckets: growth orphans (XSW/AWAY/INDA at 12w), structurally weak healthcare (IHI 12w, VHT 11w, XLV 10w), financials (IAI/IYF), and China/consumer (FXI/XLY). What funds the commodity bid: literally everything else.

## 8. Actionable Portfolio Tilts

- **Overweight** (9): `ARKK`, `CIBR`, `CLOU`, `EWY`, `PBW`, `QCLN`, `QQQ`, `SMH`, `XLK`
- **Hold-but-trim** — decelerating leaders (6): `FCG`, `IEO`, `USO`, `VDE`, `XLE`, `XOP`
- **Reduce** — weakening (10): `AMLP`, `BATT`, `EEM`, `IWM`, `LIT`, `REMX`, `SLX`, `TAN`, `VBK`, `XES`
- **Avoid** — structural laggards (13): `AWAY`, `FXI`, `IAI`, `IHI`, `INDA`, `IYF`, `JETS`, `PALL`, `VHT`, `XLF`, `XLV`, `XLY`, `XSW`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (1): `XLU`

**Net call:** Heading data changes the trade — the ↙-bar correctly pushes every energy leader out of Overweight despite 12/12 streaks; hold the commodity core on trailing stops and trim into strength, don't add. Fresh capital belongs to the ↗ names (CLOU/CIBR/SMH/QQQ/XLK). Trigger that flips the call: energy leaders' first LEADING->WEAKENING crossings confirm the top.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `BATT` (1/0), `LIT` (0/0), `PBW` (1/0), `VOT` (0/0), `XBI` (0/1)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
