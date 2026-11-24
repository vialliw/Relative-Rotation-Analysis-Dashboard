# RRA Analysis Report — 2026-10-23

- **Data as-of:** 2026-10-23
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-10-23_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 28** | **IMPROVING: 25** | **WEAKENING: 3** | **LAGGING: 40**

> Weekly read: Post-squeeze digestion — USO unwinds to +13.3D (still ↗) and LAGGING falls 47→40 as five laggards bottom into IMPROVING.
> The five 12/12 leaders all head ↘ or ↙ now — momentum is rolling across the entire leadership cohort even as breadth repairs underneath; a transition week, not a trend week.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (25)**<br>• Energy/commodity: `UNG`↗ `WEAT`↙ `XES`↗<br>• Metals/hard-asset: `BATT`↖ `DBB`↗ `GLD`↘ `PALL`↙ `PLTM`↙ `SLV`↖ `XME`↗<br>• Defensive/rate-sensitive: `HYG`↗ `JNK`↗ `SGOV`↗ `TLT`↗ `XLP`↗ `XLU`↗<br>• Value/dividend/consumer: `VOE`↗ `XLB`↗<br>• Growth/mega-cap tech: `IWF`↙ `XLC`↙<br>• EM/Intl: `EFA`↗ `EWA`↗ `EWC`↗ `FXI`↖<br>• Other: `AMLP`↙ | **LEADING (28)**<br>• Energy/commodity: `BCD`↖ `CANE`↗ `COMT`↗ `CORN`↙ `DBC`↖ `FCG`↗ `FTGC`↖ `IEO`↗ `NANR`↗ `SOYB`↙ `USO`↗ `VDE`↗ `XLE`↗ `XOP`↗<br>• Metals/hard-asset: `COPX`↖ `CPER`↗ `GDX`↗ `SLX`↖<br>• Healthcare: `IBB`↘ `IHI`↘ `VHT`↘ `XLV`↘<br>• Growth/mega-cap tech: `ARKK`↙ `CLOU`↙ `HERO`↙ `XSW`↘<br>• EM/Intl: `EWJ`↗ `EWZ`↗ |
| **< 100** | **LAGGING (40)**<br>• Metals/hard-asset: `LIT`↖ `REMX`↗ `SMOG`↗<br>• Healthcare: `XBI`↘ `XPH`↙<br>• Defensive/rate-sensitive: `ITB`↗<br>• Value/dividend/consumer: `VBR`↗ `VTV`↗ `XLY`↗ `XRT`↗<br>• Financials/REITs: `IAI`↙ `IYF`↘ `IYR`↗ `KRE`↘ `SCHH`↗ `XLF`↘<br>• Growth/mega-cap tech: `AWAY`↘ `DIA`↗ `IWM`↗ `QQQ`↖ `SMH`↖ `VBK`↗ `VOT`↗<br>• Clean energy: `ICLN`↗ `PBW`↖ `QCLN`↖ `TAN`↗<br>• EM/Intl: `EEM`↗ `EWY`↖ `INDA`↘ `VGK`↗ `VNM`↗ `VXUS`↗<br>• Transports/infra/industrials: `GRID`↖ `IFRA`↗ `IYT`↘ `JETS`↘ `XAR`↘ `XLI`↘ `XTN`↖ | **WEAKENING (3)**<br>• Value/dividend/consumer: `IWD`↗<br>• Growth/mega-cap tech: `CIBR`↙ `XLK`↖ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XSW | LEADING | 113.18 | 106.13 | 5.5 | ACCELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| IBB | LEADING | 103.76 | 103.58 | 5.0 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| CLOU | LEADING | 120.94 | 116.63 | 4.5 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| XLV | LEADING | 105.91 | 107.50 | 3.9 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| VHT | LEADING | 104.33 | 104.88 | 3.8 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| COPX | LEADING | 102.36 | 114.09 | 6.1 | ACCELERATING | ↖ | CONFIRMED | 10 | 2 | 83.3 |
| ARKK | LEADING | 104.01 | 102.84 | 3.6 | DECELERATING | ↙ | CONFIRMED | 10 | 1 | 83.3 |
| CANE | LEADING | 121.10 | 143.72 | 2.8 | DECELERATING | ↗ | CONFIRMED | 10 | 0 | 83.3 |
| HERO | LEADING | 106.19 | 124.85 | 1.9 | ACCELERATING | ↙ | CONFIRMED | 10 | 0 | 83.3 |
| NANR | LEADING | 110.88 | 133.17 | 5.4 | ACCELERATING | ↗ | CONFIRMED | 9 | 2 | 75.0 |

> Read: Same five 12/12 names (XSW/IBB/CLOU/XLV/VHT) for a third week, now joined by COPX/ARKK/CANE/HERO at 83% and NANR at 75% — the streak roster has never been deeper. Direction keeps deteriorating though: only CANE and NANR head ↗; the healthcare majors are all ↘ (ratio rising, momentum rolling over) and CLOU/ARKK/HERO head ↙. The spine is aging, not yet breaking.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| WEAT | IMPROVING | 97.33 | 116.46 | 9.0 | ACCELERATING | ↙ | TEMPORARY | 6 | 3 | 50.0 |
| XME | IMPROVING | 96.12 | 109.88 | 8.2 | ACCELERATING | ↗ | PENDING | 0 | 6 | 0.0 |
| PALL | IMPROVING | 84.73 | 116.62 | 6.4 | DECELERATING | ↙ | CONFIRMED | 2 | 2 | 16.7 |
| BATT | IMPROVING | 90.46 | 100.67 | 6.3 | ACCELERATING | ↖ | TEMPORARY | 0 | 11 | 0.0 |
| XES | IMPROVING | 95.94 | 113.99 | 6.1 | ACCELERATING | ↗ | CONFIRMED | 0 | 9 | 0.0 |
| XLB | IMPROVING | 96.60 | 102.30 | 5.1 | ACCELERATING | ↗ | TEMPORARY | 3 | 5 | 25.0 |
| XLP | IMPROVING | 99.83 | 106.55 | 4.3 | ACCELERATING | ↗ | CONFIRMED | 0 | 2 | 0.0 |
| XLU | IMPROVING | 90.66 | 100.23 | 4.2 | ACCELERATING | ↗ | TEMPORARY | 0 | 7 | 0.0 |
| TLT | IMPROVING | 92.56 | 102.15 | 4.0 | ACCELERATING | ↗ | TEMPORARY | 0 | 4 | 0.0 |
| XLC | IMPROVING | 95.86 | 112.63 | 2.7 | ACCELERATING | ↙ | CONFIRMED | 0 | 4 | 0.0 |

> Read: 25 improvers — but WEAT +9.0 topping the board is a LEADING->IMPROVING regime break heading ↙ (Δ-5.8/-6.9): the ag trade is cracking, not bottoming. The genuine ↗ bid is defensive/deep-value: XME +8.2, XES +6.1, XLB +5.1, and the rate-sensitive trio XLP +4.3 / XLU +4.2 / TLT +4.0 all heading ↗ — a textbook late-cycle bottoming rotation. BATT +6.3 is ↖ (momentum only); PALL/XLC are fading ↙.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| CIBR | WEAKENING | 111.33 | 91.16 | 4.4 | ACCELERATING | ↙ | CONFIRMED | 5 | 0 | 41.7 |
| XLK | WEAKENING | 101.55 | 86.38 | 1.6 | DECELERATING | ↖ | CONFIRMED | 2 | 4 | 16.7 |
| IWD | WEAKENING | 100.87 | 99.04 | 1.5 | ACCELERATING | ↗ | TEMPORARY | 8 | 2 | 66.7 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| USO | LEADING | 138.75 | 180.48 | 13.3 | DECELERATING | ↗ | CONFIRMED | 4 | 5 | 33.3 |
| FCG | LEADING | 112.58 | 145.68 | 7.4 | DECELERATING | ↗ | CONFIRMED | 6 | 4 | 50.0 |
| XLE | LEADING | 119.44 | 146.02 | 5.7 | DECELERATING | ↗ | CONFIRMED | 8 | 2 | 66.7 |
| VDE | LEADING | 117.99 | 144.92 | 5.5 | DECELERATING | ↗ | CONFIRMED | 7 | 3 | 58.3 |
| GDX | LEADING | 110.97 | 144.77 | 5.2 | DECELERATING | ↗ | CONFIRMED | 9 | 2 | 75.0 |
| IBB | LEADING | 103.76 | 103.58 | 5.0 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| XOP | LEADING | 119.97 | 153.11 | 4.6 | DECELERATING | ↗ | CONFIRMED | 7 | 3 | 58.3 |
| COMT | LEADING | 119.14 | 147.89 | 4.3 | DECELERATING | ↗ | CONFIRMED | 5 | 5 | 41.7 |
| XLV | LEADING | 105.91 | 107.50 | 3.9 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| IEO | LEADING | 125.95 | 154.81 | 3.9 | DECELERATING | ↗ | CONFIRMED | 8 | 0 | 66.7 |

> Read: No new regime breaks — CIBR accelerates ↙ deeper into WEAKENING (the last growth cell still falling), XLK drifts ↖, and IWD's seat is a LAGGING->WEAKENING squeeze (↗): a bounce to sell, not a breakdown. The decel board is all energy — USO 13.3, FCG 7.4, XLE 5.7, VDE 5.5, XOP 4.6, IEO 3.9, every one still heading ↗ (slowing, not reversing) — plus healthcare majors decelerating ↘. Distribution risk rising, unconfirmed.

## 5. Quadrant Crossings

11 crossings this week: **6 confirmed / 5 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 5x LAGGING->IMPROVING, 2x LEADING->IMPROVING, 1x IMPROVING->LEADING, 1x LAGGING->LEADING, 1x LAGGING->WEAKENING, 1x WEAKENING->LEADING. 1 diagonal/discontinuous transition.

### Counter-clockwise — abrupt reversals

**LEADING->IMPROVING** — potential regime break / RS breakdown warning

- `WEAT` CONFIRMED — ↙, Δratio -5.76, Δmom -6.93 (landed ratio 97.33, 2.67 past boundary); quadrant_persistence TEMPORARY
- `FXI` CONFIRMED — ↖, Δratio -2.30, Δmom +0.88 (landed ratio 98.16, 1.84 past boundary); quadrant_persistence TEMPORARY

**LAGGING->WEAKENING** — possible squeeze / counter-trend rally — not a buy signal

- `IWD` PROVISIONAL_CROSSING — ↗, Δratio +1.40, Δmom +0.49 (landed ratio 100.87, only 0.87 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**WEAKENING->LEADING** — possible re-acceleration — verify follow-through

- `SLX` CONFIRMED — ↖, Δratio -0.43, Δmom +5.57 (landed mom 102.95, 2.95 past boundary); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**IMPROVING->LEADING** — possible rotation into leadership — confirm next week

- `IHI` CONFIRMED — ↘, Δratio +4.23, Δmom -0.73 (landed ratio 101.67, 1.67 past boundary); quadrant_persistence TEMPORARY

**LAGGING->IMPROVING** — early recovery attempt — unconfirmed

- `XLB` CONFIRMED — ↗, Δratio +3.22, Δmom +3.95 (landed mom 102.30, 2.30 past boundary); quadrant_persistence TEMPORARY
- `TLT` CONFIRMED — ↗, Δratio +3.30, Δmom +2.34 (landed mom 102.15, 2.15 past boundary); quadrant_persistence TEMPORARY
- `BATT` PROVISIONAL_CROSSING — ↖, Δratio -1.14, Δmom +6.17 (landed mom 100.67, only 0.67 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `XLU` PROVISIONAL_CROSSING — ↗, Δratio +3.52, Δmom +2.36 (landed mom 100.23, only 0.23 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `EFA` PROVISIONAL_CROSSING — ↗, Δratio +0.37, Δmom +0.79 (landed mom 100.23, only 0.23 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

### Diagonal — discontinuous

**LAGGING->LEADING** — discontinuous regime change — investigate

- `EWJ` PROVISIONAL_CROSSING — ↗, Δratio +0.25, Δmom +1.69 (landed ratio 100.24, mom 101.54, only 0.24/1.54 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

> Read: the balance turns constructive — six clockwise rotations against four counter-clockwise and one diagonal, 6 of 11 confirmed. The warning side is two confirmed LEADING->IMPROVING regime breaks — WEAT out at 2.67 past (↙, the ag trade cracking) and FXI at 1.84 — plus IWD's provisional squeeze. The bid side is a bottoming complex: TLT and XLB confirmed off the lagging floor with XLU/EFA/BATT provisional at 0.23–0.67, IHI confirmed into LEADING, and SLX's confirmed WEAKENING->LEADING re-acceleration. EWJ's diagonal LAGGING->LEADING jump is discontinuous — investigate, don't trade; the five provisionals get their verdict on next week's print.

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| USO | LEADING | 13.3 | DECELERATING | ↗ | CONFIRMED | 180.48 |
| EWZ | LEADING | 9.9 | ACCELERATING | ↗ | CONFIRMED | 137.33 |
| WEAT | IMPROVING | 9.0 | ACCELERATING | ↙ | TEMPORARY | 116.46 |
| XME | IMPROVING | 8.2 | ACCELERATING | ↗ | PENDING | 109.88 |
| FCG | LEADING | 7.4 | DECELERATING | ↗ | CONFIRMED | 145.68 |
| LIT | LAGGING | 7.1 | ACCELERATING | ↖ | CONFIRMED | 94.34 |
| PALL | IMPROVING | 6.4 | DECELERATING | ↙ | CONFIRMED | 116.62 |
| BATT | IMPROVING | 6.3 | ACCELERATING | ↖ | TEMPORARY | 100.67 |
| CORN | LEADING | 6.2 | ACCELERATING | ↙ | CONFIRMED | 129.07 |
| COPX | LEADING | 6.1 | ACCELERATING | ↖ | CONFIRMED | 114.09 |

Dead money (velocity < 1.0): `IYT` 0.49, `XLI` 0.56, `GLD` 0.61, `XAR` 0.67, `VGK` 0.69, `VOT` 0.70, `EFA` 0.87, `BCD` 0.97

> Read: USO +13.3D ↗ confirms 10-16 was the squeeze climax — the unwind is orderly. New velocity is bottoming: XME +8.2A ↗ plus five LAGGING->IMPROVING crossings (BATT/EFA/TLT/XLB/XLU) repairing breadth, IHI promoted to LEADING, and SLX re-accelerating WEAKENING->LEADING. Respect the two regime breaks — FXI and WEAT both fell out of LEADING, WEAT the dangerous one (↙, Δ-5.8/-6.9). EWJ's LAGGING->LEADING jump is discontinuous — treat with suspicion.

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| EEM | 95.10 | 91.77 | 2.6 | 12 | 0.0 |
| EWY | 88.52 | 68.13 | 4.3 | 12 | 0.0 |
| GRID | 91.39 | 93.27 | 2.6 | 12 | 0.0 |
| ICLN | 84.20 | 88.31 | 4.1 | 12 | 0.0 |
| IFRA | 89.84 | 91.92 | 3.3 | 12 | 0.0 |
| LIT | 86.97 | 94.34 | 7.1 | 12 | 0.0 |
| PBW | 72.71 | 72.45 | 3.5 | 12 | 0.0 |
| QCLN | 79.31 | 74.41 | 4.4 | 12 | 0.0 |
| REMX | 67.75 | 79.55 | 4.8 | 12 | 0.0 |
| SMOG | 91.46 | 99.68 | 3.1 | 12 | 0.0 |

> Read: 40 LAGGING — second down week for the count. The 12w cohort is stable: clean energy (ICLN/LIT/PBW/QCLN/SMOG), EM Asia (EEM/EWY), infra/rare-earths (GRID/IFRA/REMX), with mega-cap growth (QQQ/SMH/VBK) and rate-sensitives (IYR/SCHH) filling the avoid tail. Notably this list is now producing the bottoming bid — XLU/TLT/XLB/EFA all crossed out of it this week; the funding pool is starting to recycle.

## 8. Actionable Portfolio Tilts

- **Overweight** (16): `BATT`, `CANE`, `COPX`, `CPER`, `EWJ`, `EWZ`, `IBB`, `IHI`, `NANR`, `SLX`, `VHT`, `XES`, `XLB`, `XLV`, `XME`, `XSW`
- **Hold-but-trim** — decelerating leaders (5): `FCG`, `GDX`, `USO`, `VDE`, `XLE`
- **Reduce** — weakening (3): `CIBR`, `IWD`, `XLK`
- **Avoid** — structural laggards (17): `EEM`, `EWY`, `GRID`, `ICLN`, `IFRA`, `IYR`, `LIT`, `PBW`, `QCLN`, `QQQ`, `REMX`, `SCHH`, `SMH`, `SMOG`, `TAN`, `VBK`, `VNM`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (10): `AMLP`, `FXI`, `GLD`, `PALL`, `PLTM`, `SGOV`, `SLV`, `UNG`, `WEAT`, `XLC`

**Net call:** The energy squeeze is done — stop trading it; the live rotation is defensive bottoming (XLP/XLU/TLT/XLB all heading ↗) plus metals (XME, SLX back in LEADING). Core hold: the 12/12 defensive spine, but it is aging (all ↘/↙) — trail stops rather than add. Trigger: a healthcare major's ↘ roll converting to a quadrant break, or the five bottoming names failing back to LAGGING — either flips this back to risk-off.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `INDA` (0/2), `UNG` (0/1), `XLP` (0/2)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
