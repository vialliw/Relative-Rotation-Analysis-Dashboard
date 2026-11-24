# RRA Analysis Report — 2026-11-13

- **Data as-of:** 2026-11-13
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-11-13_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 31** | **IMPROVING: 29** | **WEAKENING: 5** | **LAGGING: 31**

> Weekly read: Distribution climax — headline breadth still looks fine (LEADING 31, IMPROVING 29), but the heading column is a one-way street: nine of ten consistent leaders and nearly the entire improving top-10 point ↙/↘, toward LAGGING.
> SGOV (T-bills) rotating into LEADING is the tell — capital is leaving before the quadrants admit it; the arc's pivot week.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (29)**<br>• Energy/commodity: `CORN`↘ `UNG`↘ `XES`↙<br>• Metals/hard-asset: `BATT`↙ `COPX`↙ `DBB`↙ `GLD`↙ `LIT`↖ `PALL`↙ `PLTM`↙ `REMX`↖ `SLV`↙ `SMOG`↗ `XME`↙<br>• Defensive/rate-sensitive: `HYG`↘ `ITB`↗ `JNK`↘ `TLT`↗ `XLU`↗<br>• Growth/mega-cap tech: `IWF`↖ `XLC`↗<br>• Clean energy: `ICLN`↗<br>• EM/Intl: `EFA`↘ `EWA`↙ `EWJ`↙ `EWZ`↙ `FXI`↘ `VGK`↘ `VXUS`↘ | **LEADING (31)**<br>• Energy/commodity: `BCD`↙ `CANE`↙ `COMT`↙ `DBC`↙ `FCG`↙ `FTGC`↙ `IEO`↙ `NANR`↙ `SOYB`↘ `USO`↙ `VDE`↙ `XLE`↙ `XOP`↙<br>• Metals/hard-asset: `GDX`↙<br>• Healthcare: `IBB`↗ `IHI`↘ `VHT`↘ `XLV`↘<br>• Defensive/rate-sensitive: `SGOV`↘ `XLP`↗<br>• Value/dividend/consumer: `VOE`↘ `VTV`↘ `XLB`↘ `XLY`↗ `XRT`↗<br>• Growth/mega-cap tech: `ARKK`↖ `HERO`↘ `XSW`↙<br>• EM/Intl: `EWC`↘ `INDA`↗ `VNM`↗ |
| **< 100** | **LAGGING (31)**<br>• Energy/commodity: `WEAT`↘<br>• Metals/hard-asset: `CPER`↙ `SLX`↙<br>• Healthcare: `XPH`↗<br>• Value/dividend/consumer: `VBR`↗<br>• Financials/REITs: `IAI`↗ `IYF`↘ `IYR`↗ `KRE`↗ `SCHH`↗<br>• Growth/mega-cap tech: `AWAY`↙ `DIA`↗ `IWM`↗ `QQQ`↖ `SMH`↖ `VBK`↗ `VOT`↗ `XLK`↖<br>• Clean energy: `PBW`↗ `QCLN`↗ `TAN`↗<br>• EM/Intl: `EEM`↖ `EWY`↖<br>• Transports/infra/industrials: `GRID`↖ `IFRA`↗ `IYT`↗ `JETS`↗ `XAR`↘ `XLI`↘ `XTN`↗<br>• Other: `AMLP`↙ | **WEAKENING (5)**<br>• Healthcare: `XBI`↗<br>• Value/dividend/consumer: `IWD`↘<br>• Financials/REITs: `XLF`↗<br>• Growth/mega-cap tech: `CIBR`↙ `CLOU`↙ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| GDX | LEADING | 104.21 | 147.05 | 10.9 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| CANE | LEADING | 113.36 | 121.08 | 10.3 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| NANR | LEADING | 104.33 | 118.65 | 8.8 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| ARKK | LEADING | 104.48 | 114.37 | 5.6 | DECELERATING | ↖ | CONFIRMED | 12 | 0 | 100.0 |
| XSW | LEADING | 113.52 | 103.41 | 3.6 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| XLV | LEADING | 114.66 | 108.11 | 2.7 | ACCELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| VHT | LEADING | 112.64 | 105.74 | 2.3 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| IBB | LEADING | 112.96 | 107.54 | 1.9 | DECELERATING | ↗ | CONFIRMED | 12 | 0 | 100.0 |
| HERO | LEADING | 108.25 | 120.47 | 1.6 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| IEO | LEADING | 114.39 | 118.35 | 12.8 | DECELERATING | ↙ | CONFIRMED | 11 | 0 | 91.7 |

> Read: Ten consistent leaders headed by GDX at the board's top RS-momentum (147) — and the heading column is the alarm: GDX +10.9, CANE +10.3, NANR +8.8 and XSW all accelerating ↙ (fast falls, not rises), IEO ↙-decel, ARKK ↖, XLV/VHT/HERO ↘; only IBB still heads ↗. The metals/ag/energy hard-asset bloc sits on perfect streaks while rotating toward LAGGING at speed — leadership living on borrowed time. SGOV's promotion into LEADING confirms the risk-off bid underneath.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | IMPROVING | 90.09 | 118.18 | 16.0 | ACCELERATING | ↙ | PENDING | 8 | 1 | 66.7 |
| COPX | IMPROVING | 87.43 | 105.54 | 10.2 | ACCELERATING | ↙ | CONFIRMED | 9 | 0 | 75.0 |
| REMX | IMPROVING | 72.52 | 107.25 | 8.3 | DECELERATING | ↖ | TEMPORARY | 0 | 11 | 0.0 |
| SLV | IMPROVING | 83.97 | 124.74 | 8.0 | ACCELERATING | ↙ | CONFIRMED | 0 | 3 | 0.0 |
| PLTM | IMPROVING | 89.57 | 124.03 | 7.1 | ACCELERATING | ↙ | CONFIRMED | 1 | 0 | 8.3 |
| UNG | IMPROVING | 94.90 | 101.84 | 6.3 | ACCELERATING | ↘ | CONFIRMED | 0 | 0 | 0.0 |
| PALL | IMPROVING | 77.28 | 103.02 | 6.2 | ACCELERATING | ↙ | CONFIRMED | 2 | 0 | 16.7 |
| XME | IMPROVING | 90.29 | 113.34 | 5.8 | ACCELERATING | ↙ | CONFIRMED | 0 | 3 | 0.0 |
| FXI | IMPROVING | 95.00 | 106.22 | 5.4 | DECELERATING | ↘ | CONFIRMED | 2 | 0 | 16.7 |
| CORN | IMPROVING | 96.90 | 104.95 | 5.3 | DECELERATING | ↘ | CONFIRMED | 8 | 1 | 66.7 |

> Read: The heading check guts this list — nine of ten head ↙ or ↘: EWZ +16.0 ↙ accelerating toward LAGGING (the broken Brazil trade deepening), COPX +10.2 ↙, SLV/PLTM/PALL/XME all accelerating ↙, UNG/FXI/CORN ↘. The "metals improving" theme is really the metals complex falling together; the lone constructive cell is REMX +8.3 ↖ (momentum-only off a deep floor), and the real rotations are in §5 (INDA/VNM/XRT/ITB). No genuine successor regime — this bench is wreckage.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| CLOU | WEAKENING | 107.15 | 97.26 | 9.9 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| CIBR | WEAKENING | 103.76 | 81.97 | 4.7 | ACCELERATING | ↙ | CONFIRMED | 2 | 0 | 16.7 |
| XBI | WEAKENING | 101.28 | 92.71 | 3.8 | DECELERATING | ↗ | PENDING | 6 | 3 | 50.0 |
| XLF | WEAKENING | 101.62 | 96.85 | 2.4 | ACCELERATING | ↗ | TEMPORARY | 5 | 4 | 41.7 |
| IWD | WEAKENING | 103.63 | 98.92 | 1.2 | ACCELERATING | ↘ | CONFIRMED | 5 | 2 | 41.7 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| USO | LEADING | 121.03 | 133.60 | 17.7 | DECELERATING | ↙ | CONFIRMED | 7 | 2 | 58.3 |
| IEO | LEADING | 114.39 | 118.35 | 12.8 | DECELERATING | ↙ | CONFIRMED | 11 | 0 | 91.7 |
| XOP | LEADING | 109.44 | 117.19 | 12.7 | DECELERATING | ↙ | CONFIRMED | 10 | 0 | 83.3 |
| FCG | LEADING | 105.06 | 119.56 | 11.4 | DECELERATING | ↙ | CONFIRMED | 9 | 1 | 75.0 |
| XLE | LEADING | 112.31 | 118.31 | 10.5 | DECELERATING | ↙ | CONFIRMED | 11 | 0 | 91.7 |
| VDE | LEADING | 110.80 | 117.60 | 10.4 | DECELERATING | ↙ | CONFIRMED | 10 | 0 | 83.3 |
| DBC | LEADING | 108.78 | 118.39 | 8.7 | DECELERATING | ↙ | CONFIRMED | 8 | 2 | 66.7 |
| COMT | LEADING | 112.11 | 125.07 | 8.1 | DECELERATING | ↙ | CONFIRMED | 8 | 2 | 66.7 |
| FTGC | LEADING | 101.72 | 108.57 | 6.3 | DECELERATING | ↙ | CONFIRMED | 8 | 1 | 66.7 |
| VNM | LEADING | 100.05 | 115.06 | 5.8 | DECELERATING | ↗ | TEMPORARY | 1 | 6 | 8.3 |

> Read: CLOU is the regime break — a 91.7% consistent leader flipping LEADING->WEAKENING while accelerating ↙ at 9.9 (Δ-7.9/-6.0): textbook leadership failure, with CIBR accelerating ↙ behind it. Below, the entire energy/commodity complex decelerates ↙ at the board's top velocities — USO 17.7, IEO 12.8, XOP 12.7, FCG 11.4, XLE 10.5, VDE 10.4, DBC/COMT/FTGC ~8 — final distribution, as flagged last week. XLF's seat is a LAGGING->WEAKENING squeeze (↗); sell the bounce.

## 5. Quadrant Crossings

12 crossings this week: **9 confirmed / 3 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 4x IMPROVING->LEADING, 3x IMPROVING->LAGGING, 3x LAGGING->IMPROVING, 1x LAGGING->WEAKENING, 1x LEADING->WEAKENING. No diagonal/discontinuous transitions.

### Counter-clockwise — abrupt reversals

**IMPROVING->LAGGING** — failed recovery / bearish continuation

- `AMLP` CONFIRMED — ↙, Δratio -0.20, Δmom -5.13 (landed mom 97.21, 2.79 past boundary); quadrant_persistence TEMPORARY
- `SLX` CONFIRMED — ↙, Δratio -2.33, Δmom -4.53 (landed mom 98.34, 1.66 past boundary); quadrant_persistence TEMPORARY
- `CPER` PROVISIONAL_CROSSING — ↙, Δratio -2.29, Δmom -3.77 (landed mom 99.71, only 0.29 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LAGGING->WEAKENING** — possible squeeze / counter-trend rally — not a buy signal

- `XLF` CONFIRMED — ↗, Δratio +2.42, Δmom +0.07 (landed ratio 101.62, 1.62 past boundary); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**IMPROVING->LEADING** — possible rotation into leadership — confirm next week

- `INDA` CONFIRMED — ↗, Δratio +3.92, Δmom +2.51 (landed ratio 101.64, 1.64 past boundary); quadrant_persistence TEMPORARY
- `XRT` CONFIRMED — ↗, Δratio +2.30, Δmom +1.48 (landed ratio 101.21, 1.21 past boundary); quadrant_persistence TEMPORARY
- `SGOV` CONFIRMED — ↘, Δratio +1.47, Δmom -1.74 (landed ratio 101.17, 1.17 past boundary); quadrant_persistence TEMPORARY
- `VNM` PROVISIONAL_CROSSING — ↗, Δratio +0.92, Δmom +5.77 (landed ratio 100.05, only 0.05 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LEADING->WEAKENING** — potential distribution / early reversal — watch

- `CLOU` CONFIRMED — ↙, Δratio -7.87, Δmom -6.03 (landed mom 97.26, 2.74 past boundary); quadrant_persistence TEMPORARY

**LAGGING->IMPROVING** — early recovery attempt — unconfirmed

- `REMX` CONFIRMED — ↖, Δratio -0.90, Δmom +8.22 (landed mom 107.25, 7.25 past boundary); quadrant_persistence TEMPORARY
- `ITB` CONFIRMED — ↗, Δratio +1.43, Δmom +4.34 (landed mom 101.10, 1.10 past boundary); quadrant_persistence TEMPORARY
- `ICLN` PROVISIONAL_CROSSING — ↗, Δratio +1.09, Δmom +4.57 (landed mom 100.18, only 0.18 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

> Read: clockwise flow outnumbers counter-clockwise eight-to-four, but the crossing that matters is bearish and confirmed — CLOU's LEADING->WEAKENING break at 2.74 past on Δ-7.9/-6.0 ↙ is a real leadership failure (labeled 'normal aging', it isn't), with AMLP and SLX confirmed out to LAGGING and CPER's 0.29 slide provisional. The constructive side is defensive-flavored: SGOV's confirmed promotion to LEADING is the risk-off tell, INDA/XRT confirmed into LEADING beside VNM's hair-thin 0.05 provisional, and the off-the-floor repairs (REMX 7.25 deep, ITB confirmed, ICLN provisional) are bottoming attempts, not leadership. XLF's confirmed LAGGING->WEAKENING squeeze is a bounce to sell; the three provisionals get their verdict on next week's print.

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| USO | LEADING | 17.7 | DECELERATING | ↙ | CONFIRMED | 133.60 |
| EWZ | IMPROVING | 16.0 | ACCELERATING | ↙ | PENDING | 118.18 |
| IEO | LEADING | 12.8 | DECELERATING | ↙ | CONFIRMED | 118.35 |
| XOP | LEADING | 12.7 | DECELERATING | ↙ | CONFIRMED | 117.19 |
| FCG | LEADING | 11.4 | DECELERATING | ↙ | CONFIRMED | 119.56 |
| GDX | LEADING | 10.9 | ACCELERATING | ↙ | CONFIRMED | 147.05 |
| XLE | LEADING | 10.5 | DECELERATING | ↙ | CONFIRMED | 118.31 |
| VDE | LEADING | 10.4 | DECELERATING | ↙ | CONFIRMED | 117.60 |
| CANE | LEADING | 10.3 | ACCELERATING | ↙ | CONFIRMED | 121.08 |
| COPX | IMPROVING | 10.2 | ACCELERATING | ↙ | CONFIRMED | 105.54 |

Dead money (velocity < 1.0): `AWAY` 0.39, `VXUS` 0.45, `DIA` 0.49, `GRID` 0.53, `VOT` 0.58, `XLB` 0.66, `XAR` 0.70

> Read: Velocity polarity is fully inverted — the ten fastest movers all head ↙: energy decelerating at max velocity (USO 17.7, IEO/XOP ~12.8) while metals and EWZ accelerate downward (GDX 10.9, CANE 10.3, COPX 10.2, EWZ 16.0). Nothing large moves ↗; the only up-right cells are off-the-floor bottoming crosses (ICLN, ITB) and REMX's ↖ squeeze. The crossings split four bullish (INDA/VNM/XRT rotations + SGOV's promotion) against five bearish — CLOU's LEADING->WEAKENING is labeled "normal aging" but at Δ-7.9/-6.0 ↙ it is a real break — plus the XLF squeeze to sell.

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| EEM | 94.24 | 97.48 | 1.1 | 12 | 0.0 |
| EWY | 89.26 | 85.64 | 6.0 | 12 | 0.0 |
| GRID | 88.67 | 96.46 | 0.5 | 12 | 0.0 |
| IFRA | 94.11 | 96.08 | 2.5 | 12 | 0.0 |
| PBW | 78.72 | 88.03 | 6.2 | 12 | 0.0 |
| QCLN | 86.37 | 94.06 | 8.3 | 12 | 0.0 |
| QQQ | 97.18 | 96.03 | 1.7 | 12 | 0.0 |
| SMH | 87.74 | 78.63 | 3.9 | 12 | 0.0 |
| TAN | 83.61 | 93.02 | 5.3 | 12 | 0.0 |
| VBK | 94.23 | 95.27 | 1.7 | 11 | 0.0 |

> Read: 31 LAGGING — the count stopped falling. SMH joins QQQ at 12 lag weeks — mega-cap growth and semis are now structurally defunded — alongside the standing clean-energy (PBW/QCLN/TAN), EM-Asia (EEM/EWY) and grid/infra (GRID/IFRA) buckets. This cohort financed the hard-asset run; with that run now breaking ↙, watch whether the funding reverses back into it — VBK at 11 lag weeks is the canary.

## 8. Actionable Portfolio Tilts

- **Overweight** (15): `ARKK`, `EWC`, `HERO`, `IBB`, `IHI`, `INDA`, `SGOV`, `SOYB`, `UNG`, `VHT`, `VOE`, `VTV`, `XLP`, `XLV`, `XRT`
- **Hold-but-trim** — decelerating leaders (10): `COMT`, `DBC`, `FCG`, `FTGC`, `IEO`, `USO`, `VDE`, `VNM`, `XLE`, `XOP`
- **Reduce** — weakening (5): `CIBR`, `CLOU`, `IWD`, `XBI`, `XLF`
- **Avoid** — structural laggards (18): `EEM`, `EWY`, `GRID`, `IFRA`, `IWM`, `IYR`, `IYT`, `PBW`, `QCLN`, `QQQ`, `SCHH`, `SLX`, `SMH`, `TAN`, `VBK`, `VOT`, `XAR`, `XTN`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (5): `EWZ`, `GLD`, `PLTM`, `SLV`, `XME`

**Net call:** Do not chase the metals "improvement" — GDX/SLV/PLTM/COPX are all heading ↙; the last hard-asset bid is breaking. Rotate into what is actually confirming: the defensive/value cohort (healthcare XLV/VHT/IBB/IHI, VTV/VOE, XRT, INDA) plus SGOV, funded by exiting energy and ags wholesale. Trigger: the ↙-heading streak names (GDX/CANE/NANR/XSW) flipping to WEAKENING/LAGGING next week makes the regime change official — de-risk, don't rotate.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `CIBR` (2/0), `FXI` (2/0), `GLD` (0/0), `HYG` (0/0), `JNK` (0/0), `PALL` (2/0), `PLTM` (1/0), `SGOV` (1/0), `TLT` (0/1), `UNG` (0/0), `XLC` (0/1)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
