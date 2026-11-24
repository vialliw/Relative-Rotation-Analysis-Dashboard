# RRA Analysis Report — 2026-08-07

- **Data as-of:** 2026-08-07
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-08-07_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 17** | **IMPROVING: 9** | **WEAKENING: 11** | **LAGGING: 59**

> Weekly read: Regime handoff week — SMH falls to WEAKENING (↙), QQQ breaks LEADING->IMPROVING, and not one consistent leader heads ↗.
> Metals and defensives accelerate off the floor: the coil is releasing.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (9)**<br>• Energy/commodity: `CANE`↗<br>• Healthcare: `IHI`↗<br>• Defensive/rate-sensitive: `ITB`↗<br>• Value/dividend/consumer: `XRT`↗<br>• Growth/mega-cap tech: `ARKK`↙ `HERO`↗ `QQQ`↙ `VOT`↘<br>• EM/Intl: `INDA`↗ | **LEADING (17)**<br>• Healthcare: `IBB`↗ `VHT`↗ `XBI`↗ `XLV`↗ `XPH`↗<br>• Value/dividend/consumer: `IWD`↗<br>• Financials/REITs: `IAI`↖ `IYF`↗ `KRE`↗ `XLF`↗<br>• Growth/mega-cap tech: `AWAY`↘ `CIBR`↙ `CLOU`↖ `DIA`↗ `XLK`↙ `XSW`↙<br>• Transports/infra/industrials: `JETS`↗ |
| **< 100** | **LAGGING (59)**<br>• Energy/commodity: `BCD`↖ `COMT`↖ `CORN`↖ `DBC`↖ `FCG`↖ `FTGC`↖ `NANR`↗ `SOYB`↖ `UNG`↖ `USO`↖ `VDE`↖ `WEAT`↖ `XES`↖ `XLE`↖ `XOP`↖<br>• Metals/hard-asset: `BATT`↗ `COPX`↗ `DBB`↗ `GDX`↗ `GLD`↗ `LIT`↙ `PALL`↗ `PLTM`↗ `REMX`↙ `SLV`↗ `SLX`↗ `SMOG`↙ `XME`↗<br>• Defensive/rate-sensitive: `HYG`↗ `JNK`↗ `SGOV`↗ `TLT`↗ `XLP`↖ `XLU`↖<br>• Value/dividend/consumer: `XLB`↗ `XLY`↘<br>• Financials/REITs: `IYR`↖ `SCHH`↖<br>• Growth/mega-cap tech: `IWF`↙ `VBK`↖ `XLC`↗<br>• Clean energy: `ICLN`↙ `PBW`↙ `QCLN`↙ `TAN`↖<br>• EM/Intl: `EEM`↙ `EFA`↗ `EWA`↗ `EWC`↗ `EWY`↙ `EWZ`↗ `FXI`↗ `VGK`↗ `VNM`↙ `VXUS`↗<br>• Transports/infra/industrials: `GRID`↙ `IFRA`↖ `XAR`↗ `XTN`↙ | **WEAKENING (11)**<br>• Energy/commodity: `IEO`↖<br>• Metals/hard-asset: `CPER`↗<br>• Value/dividend/consumer: `VBR`↗ `VOE`↗ `VTV`↗<br>• Growth/mega-cap tech: `IWM`↖ `SMH`↙<br>• EM/Intl: `EWJ`↗<br>• Transports/infra/industrials: `IYT`↖ `XLI`↗<br>• Other: `AMLP`↗ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XLK | LEADING | 107.29 | 107.00 | 5.9 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| CIBR | LEADING | 130.09 | 145.90 | 2.3 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| CLOU | LEADING | 118.11 | 135.50 | 1.9 | DECELERATING | ↖ | CONFIRMED | 12 | 0 | 100.0 |
| XSW | LEADING | 112.28 | 142.10 | 2.0 | DECELERATING | ↙ | CONFIRMED | 9 | 0 | 75.0 |

> Read: Four consistent leaders left after SMH and QQQ lost their streaks — XLK/CIBR/XSW all head ↙, CLOU ↖. Streaks intact, trajectories pointing down: the last of the growth regime is held by inertia, not by fresh buying.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| CANE | IMPROVING | 99.35 | 100.96 | 8.3 | DECELERATING | ↗ | TEMPORARY | 1 | 7 | 8.3 |
| IHI | IMPROVING | 94.70 | 107.93 | 8.3 | ACCELERATING | ↗ | PENDING | 0 | 10 | 0.0 |
| ARKK | IMPROVING | 90.58 | 100.68 | 6.1 | DECELERATING | ↙ | CONFIRMED | 4 | 0 | 33.3 |
| HERO | IMPROVING | 91.95 | 103.11 | 4.5 | ACCELERATING | ↗ | TEMPORARY | 0 | 11 | 0.0 |
| QQQ | IMPROVING | 99.97 | 100.53 | 3.7 | DECELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| ITB | IMPROVING | 95.01 | 103.10 | 3.5 | ACCELERATING | ↗ | CONFIRMED | 0 | 7 | 0.0 |
| XRT | IMPROVING | 98.32 | 103.58 | 2.1 | ACCELERATING | ↗ | CONFIRMED | 0 | 7 | 0.0 |
| INDA | IMPROVING | 93.61 | 100.18 | 1.7 | ACCELERATING | ↗ | TEMPORARY | 0 | 8 | 0.0 |
| VOT | IMPROVING | 99.47 | 103.22 | 0.5 | DECELERATING | ↘ | CONFIRMED | 4 | 0 | 33.3 |

> Read: Genuine improvers finally exist — IHI +8.3 ↗ (second week accelerating), HERO +4.5, ITB +3.5, XRT +2.1, INDA, CANE all ↗. But the two biggest names are impostors: ARKK +6.1 and QQQ +3.7 head ↙ — faded leaders parked in IMPROVING, not improvers.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| IEO | WEAKENING | 101.42 | 79.89 | 8.7 | DECELERATING | ↖ | PENDING | 1 | 7 | 8.3 |
| SMH | WEAKENING | 107.96 | 96.60 | 8.2 | DECELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| AMLP | WEAKENING | 101.60 | 92.33 | 7.1 | DECELERATING | ↗ | PENDING | 0 | 9 | 0.0 |
| EWJ | WEAKENING | 100.48 | 94.36 | 4.8 | ACCELERATING | ↗ | TEMPORARY | 0 | 9 | 0.0 |
| VTV | WEAKENING | 103.17 | 99.40 | 4.1 | ACCELERATING | ↗ | CONFIRMED | 0 | 9 | 0.0 |
| CPER | WEAKENING | 101.01 | 98.89 | 4.0 | ACCELERATING | ↗ | TEMPORARY | 0 | 10 | 0.0 |
| VOE | WEAKENING | 101.34 | 96.64 | 4.0 | ACCELERATING | ↗ | PENDING | 0 | 10 | 0.0 |
| XLI | WEAKENING | 100.19 | 94.46 | 3.6 | ACCELERATING | ↗ | TEMPORARY | 0 | 11 | 0.0 |
| VBR | WEAKENING | 101.13 | 97.68 | 3.0 | ACCELERATING | ↗ | PENDING | 0 | 9 | 0.0 |
| IYT | WEAKENING | 101.14 | 99.83 | 1.6 | ACCELERATING | ↖ | CONFIRMED | 2 | 4 | 16.7 |
| IWM | WEAKENING | 100.88 | 98.42 | 0.8 | DECELERATING | ↖ | CONFIRMED | 4 | 3 | 33.3 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XLK | LEADING | 107.29 | 107.00 | 5.9 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| IWD | LEADING | 104.97 | 100.93 | 3.1 | DECELERATING | ↗ | TEMPORARY | 1 | 5 | 8.3 |
| IYF | LEADING | 103.41 | 109.11 | 2.5 | DECELERATING | ↗ | CONFIRMED | 3 | 6 | 25.0 |
| XLF | LEADING | 104.24 | 111.02 | 2.3 | DECELERATING | ↗ | CONFIRMED | 3 | 6 | 25.0 |
| CIBR | LEADING | 130.09 | 145.90 | 2.3 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| AWAY | LEADING | 102.33 | 121.46 | 2.2 | DECELERATING | ↘ | PENDING | 5 | 1 | 41.7 |
| XSW | LEADING | 112.28 | 142.10 | 2.0 | DECELERATING | ↙ | CONFIRMED | 9 | 0 | 75.0 |
| CLOU | LEADING | 118.11 | 135.50 | 1.9 | DECELERATING | ↖ | CONFIRMED | 12 | 0 | 100.0 |
| IAI | LEADING | 100.23 | 107.80 | 1.4 | DECELERATING | ↖ | CONFIRMED | 3 | 4 | 25.0 |
| XBI | LEADING | 107.22 | 100.83 | 1.2 | DECELERATING | ↗ | CONFIRMED | 6 | 5 | 50.0 |

> Read: Regime break confirmed: SMH formally WEAKENING on an ↙ heading (Δmom -7.5) — concentrated-semi leadership ends this arc. The rest of the list is ↗ squeezes (AMLP/EWJ/VTV/CPER/VOE/XLI/VBR) plus momentum-only lifters (IEO/IYT/IWM ↖) — value, industrials and Japan lifting off the floor through WEAKENING.

## 5. Quadrant Crossings

14 crossings this week: **4 confirmed / 10 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 3x LAGGING->IMPROVING, 3x LAGGING->WEAKENING, 3x WEAKENING->LAGGING, 2x WEAKENING->LEADING, 1x IMPROVING->LAGGING, 1x LEADING->IMPROVING, 1x LEADING->WEAKENING. No diagonal/discontinuous transitions.

### Counter-clockwise — abrupt reversals

**LEADING->IMPROVING** — potential regime break / RS breakdown warning

- `QQQ` PROVISIONAL_CROSSING — ↙, Δratio -1.35, Δmom -3.41 (landed ratio 99.97, only 0.03 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**IMPROVING->LAGGING** — failed recovery / bearish continuation

- `IWF` PROVISIONAL_CROSSING — ↙, Δratio -0.36, Δmom -2.72 (landed mom 99.23, only 0.77 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LAGGING->WEAKENING** — possible squeeze / counter-trend rally — not a buy signal

- `CPER` CONFIRMED — ↗, Δratio +1.99, Δmom +3.48 (landed ratio 101.01, 1.01 past boundary); quadrant_persistence TEMPORARY
- `EWJ` PROVISIONAL_CROSSING — ↗, Δratio +2.81, Δmom +3.89 (landed ratio 100.48, only 0.48 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `XLI` PROVISIONAL_CROSSING — ↗, Δratio +1.39, Δmom +3.35 (landed ratio 100.19, only 0.19 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**WEAKENING->LEADING** — possible re-acceleration — verify follow-through

- `IWD` PROVISIONAL_CROSSING — ↗, Δratio +0.59, Δmom +3.03 (landed mom 100.93, only 0.93 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `KRE` PROVISIONAL_CROSSING — ↗, Δratio +0.01, Δmom +2.50 (landed mom 100.83, only 0.83 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**LEADING->WEAKENING** — potential distribution / early reversal — watch

- `SMH` CONFIRMED — ↙, Δratio -3.30, Δmom -7.50 (landed mom 96.60, 3.40 past boundary); quadrant_persistence TEMPORARY

**WEAKENING->LAGGING** — potential bearish continuation — confirm persistence

- `EWY` CONFIRMED — ↙, Δratio -3.84, Δmom -4.78 (landed ratio 98.24, 1.76 past boundary); quadrant_persistence TEMPORARY
- `WEAT` PROVISIONAL_CROSSING — ↖, Δratio -4.36, Δmom +3.90 (landed ratio 99.34, only 0.66 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `SCHH` PROVISIONAL_CROSSING — ↖, Δratio -1.13, Δmom +1.94 (landed ratio 99.94, only 0.06 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LAGGING->IMPROVING** — early recovery attempt — unconfirmed

- `HERO` CONFIRMED — ↗, Δratio +2.69, Δmom +3.54 (landed mom 103.11, 3.11 past boundary); quadrant_persistence TEMPORARY
- `CANE` PROVISIONAL_CROSSING — ↗, Δratio +1.11, Δmom +8.25 (landed mom 100.96, only 0.96 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `INDA` PROVISIONAL_CROSSING — ↗, Δratio +1.65, Δmom +0.38 (landed mom 100.18, only 0.18 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

> Read: 14 crossings but only 4 confirmed, split evenly 7 counter-clockwise / 7 clockwise — boundary churn, and the one that matters is confirmed: SMH's LEADING->WEAKENING regime break at 3.40 past the line on a ↙ heading ends the concentrated-semi arc. EWY's WEAKENING->LAGGING (1.76), CPER's ↗ squeeze and HERO's ↗ LAGGING->IMPROVING bottoming round out the confirmed four. The provisional pile is the real watch list: QQQ's LEADING->IMPROVING sits 0.03 past the boundary — a coin-flip whipsaw — while the squeeze cluster (EWJ/XLI) and the WEAKENING->LEADING re-accelerations (IWD/KRE) all land thin; direction stays unresolved until they settle.

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| GDX | LAGGING | 12.8 | ACCELERATING | ↗ | CONFIRMED | 72.42 |
| XAR | LAGGING | 10.2 | ACCELERATING | ↗ | CONFIRMED | 97.71 |
| COPX | LAGGING | 9.9 | ACCELERATING | ↗ | CONFIRMED | 83.57 |
| XLE | LAGGING | 9.0 | DECELERATING | ↖ | CONFIRMED | 80.59 |
| VDE | LAGGING | 8.8 | DECELERATING | ↖ | CONFIRMED | 79.43 |
| NANR | LAGGING | 8.7 | ACCELERATING | ↗ | CONFIRMED | 79.23 |
| IEO | WEAKENING | 8.7 | DECELERATING | ↖ | PENDING | 79.89 |
| XOP | LAGGING | 8.4 | DECELERATING | ↖ | CONFIRMED | 75.24 |
| CANE | IMPROVING | 8.3 | DECELERATING | ↗ | TEMPORARY | 100.96 |
| IHI | IMPROVING | 8.3 | ACCELERATING | ↗ | PENDING | 107.93 |

Dead money (velocity < 1.0): `VBK` 0.06, `XPH` 0.32, `VOT` 0.52, `EEM` 0.55, `XLY` 0.68, `XLC` 0.69, `IWM` 0.80

> Read: Metals take the velocity crown with direction to match — GDX +12.8, XAR +10.2, COPX +9.9, NANR all ↗ accelerating: real bottoming, not squeezes. Flags: EWJ/CPER/XLI LAGGING->WEAKENING squeezes are sells; QQQ's regime break and EWY/WEAT/SCHH breakdowns confirm the exit side.

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| COPX | 93.73 | 83.57 | 9.9 | 12 | 0.0 |
| DBB | 95.09 | 91.13 | 3.9 | 12 | 0.0 |
| EFA | 99.13 | 94.71 | 4.0 | 12 | 0.0 |
| EWA | 95.86 | 84.96 | 4.6 | 12 | 0.0 |
| EWC | 97.80 | 93.38 | 2.7 | 12 | 0.0 |
| EWZ | 85.47 | 69.51 | 4.5 | 12 | 0.0 |
| FXI | 91.98 | 97.12 | 5.1 | 12 | 0.0 |
| GDX | 80.89 | 72.42 | 12.8 | 12 | 0.0 |
| GLD | 83.07 | 77.74 | 6.2 | 12 | 0.0 |
| HYG | 94.98 | 94.59 | 3.9 | 12 | 0.0 |

> Read: 59 LAGGING in three buckets: metals (GDX/COPX/GLD — now the fastest ↗ movers on the board), DM/EM ex-US (EFA/EWA/EWC/EWZ/FXI), and credit (HYG/JNK). The lag-list is producing the next leadership cohort.

## 8. Actionable Portfolio Tilts

- **Overweight** (8): `CLOU`, `DIA`, `IBB`, `IHI`, `JETS`, `KRE`, `VHT`, `XLV`
- **Hold-but-trim** — decelerating leaders (1): `XLK`
- **Reduce** — weakening (11): `AMLP`, `CPER`, `EWJ`, `IEO`, `IWM`, `IYT`, `SMH`, `VBR`, `VOE`, `VTV`, `XLI`
- **Avoid** — structural laggards (45): `BATT`, `BCD`, `COMT`, `COPX`, `CORN`, `DBB`, `DBC`, `EFA`, `EWA`, `EWC`, `EWZ`, `FCG`, `FTGC`, `FXI`, `GDX`, `GLD`, `HYG`, `IFRA`, `IYR`, `JNK`, `NANR`, `PALL`, `PLTM`, `REMX`, `SCHH`, `SGOV`, `SLV`, `SMOG`, `SOYB`, `TLT`, `UNG`, `VDE`, `VGK`, `VNM`, `VXUS`, `XAR`, `XES`, `XLB`, `XLC`, `XLE`, `XLP`, `XLU`, `XLY`, `XME`, `XOP`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (0): none

**Net call:** Rotate: exit SMH (WEAKENING, ↙) and treat QQQ's regime break as a sell, not a dip-buy; build the successor regime — ↗-bottoming metals (GDX/COPX) and healthcare (IHI/VHT/XLV). Core hold: the defensive/financial overweight bloc (XLV/VHT/IBB/KRE/DIA). Trigger: GDX/COPX stalling or flipping ↙ below RS-ratio 100 cancels the metals leg.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `EWY` (1/1)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
