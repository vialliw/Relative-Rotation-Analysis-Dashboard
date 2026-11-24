# RRA Analysis Report — 2026-10-16

- **Data as-of:** 2026-10-16
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-10-16_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 27** | **IMPROVING: 19** | **WEAKENING: 3** | **LAGGING: 47**

> Weekly read: Squeeze-climax week — USO +29.9A ↗ tops the board while LAGGING jumps 41→47 and IMPROVING thins to 19.
> The healthcare/software spine holds all five 12/12 streaks, but every one of them now heads ↙ or ↖: positionally led, directionally stalling — the widest breadth deterioration of the series so far.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (19)**<br>• Energy/commodity: `UNG`↗ `XES`↖<br>• Metals/hard-asset: `DBB`↗ `GLD`↘ `PALL`↙ `PLTM`↙ `SLV`↙ `XME`↗<br>• Healthcare: `IHI`↘<br>• Defensive/rate-sensitive: `HYG`↗ `JNK`↗ `SGOV`↗ `XLP`↘<br>• Value/dividend/consumer: `VOE`↘<br>• Growth/mega-cap tech: `IWF`↖ `XLC`↙<br>• EM/Intl: `EWA`↘ `EWC`↘<br>• Other: `AMLP`↖ | **LEADING (27)**<br>• Energy/commodity: `BCD`↗ `CANE`↗ `COMT`↗ `CORN`↙ `DBC`↗ `FCG`↗ `FTGC`↗ `IEO`↗ `NANR`↗ `SOYB`↙ `USO`↗ `VDE`↗ `WEAT`↙ `XLE`↗ `XOP`↗<br>• Metals/hard-asset: `COPX`↗ `CPER`↗ `GDX`↘<br>• Healthcare: `IBB`↙ `VHT`↙ `XLV`↙<br>• Growth/mega-cap tech: `ARKK`↙ `CLOU`↖ `HERO`↘ `XSW`↙<br>• EM/Intl: `EWZ`↗ `FXI`↗ |
| **< 100** | **LAGGING (47)**<br>• Metals/hard-asset: `BATT`↗ `LIT`↗ `REMX`↙ `SMOG`↗<br>• Healthcare: `XBI`↙ `XPH`↙<br>• Defensive/rate-sensitive: `ITB`↘ `TLT`↘ `XLU`↘<br>• Value/dividend/consumer: `IWD`↘ `VBR`↘ `VTV`↘ `XLB`↘ `XLY`↘ `XRT`↘<br>• Financials/REITs: `IAI`↙ `IYF`↙ `IYR`↘ `KRE`↙ `SCHH`↘ `XLF`↙<br>• Growth/mega-cap tech: `AWAY`↘ `DIA`↘ `IWM`↙ `QQQ`↖ `SMH`↖ `VBK`↙ `VOT`↘<br>• Clean energy: `ICLN`↗ `PBW`↗ `QCLN`↗ `TAN`↗<br>• EM/Intl: `EEM`↙ `EFA`↘ `EWJ`↘ `EWY`↙ `INDA`↘ `VGK`↘ `VNM`↙ `VXUS`↘<br>• Transports/infra/industrials: `GRID`↗ `IFRA`↘ `IYT`↙ `JETS`↙ `XAR`↘ `XLI`↙ `XTN`↙ | **WEAKENING (3)**<br>• Metals/hard-asset: `SLX`↗<br>• Growth/mega-cap tech: `CIBR`↙ `XLK`↖ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| IBB | LEADING | 102.67 | 108.43 | 9.8 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| VHT | LEADING | 101.25 | 107.10 | 5.7 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| XLV | LEADING | 102.35 | 109.18 | 4.9 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| XSW | LEADING | 110.91 | 111.18 | 4.0 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| CLOU | LEADING | 121.09 | 121.08 | 3.9 | DECELERATING | ↖ | CONFIRMED | 12 | 0 | 100.0 |
| CANE | LEADING | 119.23 | 141.69 | 7.0 | ACCELERATING | ↗ | CONFIRMED | 9 | 1 | 75.0 |
| ARKK | LEADING | 104.76 | 106.32 | 5.0 | ACCELERATING | ↙ | CONFIRMED | 9 | 1 | 75.0 |
| COPX | LEADING | 105.59 | 108.93 | 2.2 | DECELERATING | ↗ | CONFIRMED | 9 | 3 | 75.0 |
| HERO | LEADING | 106.71 | 126.70 | 0.5 | DECELERATING | ↘ | CONFIRMED | 9 | 1 | 75.0 |

> Read: The streak roster grows to nine — IBB joins 12/12 with CLOU/VHT/XLV/XSW, CANE/ARKK/COPX/HERO at 75-83% — healthcare + software is the dominant consistent regime. Direction is the worry: all five perfect names head ↙ (IBB +9.8 "ACCELERATING" is accelerating toward LAGGING) except CLOU drifting ↖; CANE +7.0 ↗ is the cohort's only genuine riser.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| PALL | IMPROVING | 87.96 | 122.12 | 9.2 | DECELERATING | ↙ | CONFIRMED | 2 | 3 | 16.7 |
| XME | IMPROVING | 95.08 | 101.77 | 5.6 | ACCELERATING | ↗ | TEMPORARY | 0 | 7 | 0.0 |
| XES | IMPROVING | 94.74 | 108.00 | 5.4 | DECELERATING | ↖ | PENDING | 0 | 10 | 0.0 |
| UNG | IMPROVING | 91.10 | 108.40 | 3.7 | ACCELERATING | ↗ | CONFIRMED | 0 | 2 | 0.0 |
| IHI | IMPROVING | 97.44 | 119.28 | 3.6 | DECELERATING | ↘ | CONFIRMED | 7 | 0 | 58.3 |
| XLP | IMPROVING | 96.05 | 104.50 | 2.5 | ACCELERATING | ↘ | CONFIRMED | 0 | 3 | 0.0 |
| GLD | IMPROVING | 97.72 | 126.80 | 2.3 | ACCELERATING | ↘ | CONFIRMED | 0 | 4 | 0.0 |
| DBB | IMPROVING | 98.93 | 105.52 | 2.1 | DECELERATING | ↗ | CONFIRMED | 0 | 9 | 0.0 |
| SGOV | IMPROVING | 97.15 | 109.35 | 1.6 | ACCELERATING | ↗ | CONFIRMED | 0 | 4 | 0.0 |
| PLTM | IMPROVING | 98.91 | 135.11 | 1.4 | DECELERATING | ↙ | PENDING | 1 | 4 | 8.3 |

> Read: 19 improvers, low-velocity and defensive-flavored — but PALL +9.2 tops the list heading ↙ (fading leader, not improver). The genuine ↗ risers: XME +5.6 (LAGGING->IMPROVING bottoming), UNG +3.7, DBB +2.1, and SGOV +1.6 — T-bills improving is a quiet risk-off tell. The metals bench (GLD/SLV/PLTM, all ↘/↙) is coiled on RS-momentum ≥110 but not yet rotating right — watch, don't buy.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| SLX | WEAKENING | 100.51 | 97.38 | 4.5 | ACCELERATING | ↗ | TEMPORARY | 0 | 11 | 0.0 |
| CIBR | WEAKENING | 112.60 | 95.40 | 3.1 | DECELERATING | ↙ | CONFIRMED | 6 | 0 | 50.0 |
| XLK | WEAKENING | 102.36 | 85.01 | 1.6 | DECELERATING | ↖ | CONFIRMED | 3 | 4 | 25.0 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| COMT | LEADING | 118.60 | 143.58 | 12.5 | DECELERATING | ↗ | CONFIRMED | 4 | 6 | 33.3 |
| XOP | LEADING | 119.08 | 148.57 | 11.4 | DECELERATING | ↗ | CONFIRMED | 6 | 4 | 50.0 |
| DBC | LEADING | 118.35 | 140.57 | 10.6 | DECELERATING | ↗ | CONFIRMED | 4 | 6 | 33.3 |
| IEO | LEADING | 124.65 | 151.11 | 10.3 | DECELERATING | ↗ | CONFIRMED | 7 | 0 | 58.3 |
| GDX | LEADING | 110.30 | 139.64 | 6.5 | DECELERATING | ↘ | CONFIRMED | 8 | 3 | 66.7 |
| FTGC | LEADING | 109.35 | 128.39 | 4.9 | DECELERATING | ↗ | CONFIRMED | 4 | 5 | 33.3 |
| BCD | LEADING | 108.68 | 127.70 | 4.7 | DECELERATING | ↗ | CONFIRMED | 5 | 6 | 41.7 |
| EWZ | LEADING | 113.21 | 128.60 | 4.4 | DECELERATING | ↗ | CONFIRMED | 6 | 5 | 50.0 |
| FXI | LEADING | 100.46 | 122.20 | 4.2 | DECELERATING | ↗ | PENDING | 2 | 2 | 16.7 |
| CLOU | LEADING | 121.09 | 121.08 | 3.9 | DECELERATING | ↖ | CONFIRMED | 12 | 0 | 100.0 |

> Read: No regime break — SLX's WEAKENING seat is a LAGGING->WEAKENING squeeze (↗ +2.0/+4.1), a bounce not a breakdown; CIBR keeps grinding ↙ and XLK drifts ↖, so growth stays done. The decel board is the story: COMT/XOP/DBC/IEO decelerating above 10 while still heading ↗ — the energy bid is slowing at the top of its run, not yet reversing; GDX (↘) is the first hard-asset name losing momentum.

## 5. Quadrant Crossings

11 crossings this week: **4 confirmed / 7 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 8x IMPROVING->LAGGING, 1x LAGGING->IMPROVING, 1x LAGGING->WEAKENING, 1x WEAKENING->IMPROVING. 1 diagonal/discontinuous transition.

### Counter-clockwise — abrupt reversals

**IMPROVING->LAGGING** — failed recovery / bearish continuation

- `XBI` CONFIRMED — ↙, Δratio -5.65, Δmom -11.03 (landed mom 90.03, 9.97 past boundary); quadrant_persistence TEMPORARY
- `IYF` CONFIRMED — ↙, Δratio -0.69, Δmom -2.86 (landed mom 97.53, 2.47 past boundary); quadrant_persistence TEMPORARY
- `VTV` CONFIRMED — ↘, Δratio +0.68, Δmom -1.29 (landed mom 98.72, 1.28 past boundary); quadrant_persistence TEMPORARY
- `INDA` PROVISIONAL_CROSSING — ↘, Δratio +0.72, Δmom -3.89 (landed mom 99.23, only 0.77 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `XLF` PROVISIONAL_CROSSING — ↙, Δratio -0.29, Δmom -3.03 (landed mom 99.19, only 0.81 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `TLT` PROVISIONAL_CROSSING — ↘, Δratio +1.77, Δmom -0.42 (landed mom 99.81, only 0.19 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `EFA` PROVISIONAL_CROSSING — ↘, Δratio +0.10, Δmom -1.70 (landed mom 99.44, only 0.56 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `EWJ` PROVISIONAL_CROSSING — ↘, Δratio +0.26, Δmom -1.05 (landed mom 99.85, only 0.15 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LAGGING->WEAKENING** — possible squeeze / counter-trend rally — not a buy signal

- `SLX` PROVISIONAL_CROSSING — ↗, Δratio +1.97, Δmom +4.07 (landed ratio 100.51, only 0.51 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**LAGGING->IMPROVING** — early recovery attempt — unconfirmed

- `XME` CONFIRMED — ↗, Δratio +2.19, Δmom +5.20 (landed mom 101.77, 1.77 past boundary); quadrant_persistence TEMPORARY

### Diagonal — discontinuous

**WEAKENING->IMPROVING** — discontinuous regime change — investigate

- `IWF` PROVISIONAL_CROSSING — ↖, Δratio -0.76, Δmom +0.61 (landed ratio 99.52, mom 100.47, only 0.48/0.47 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

> Read: almost entirely one-directional — nine counter-clockwise crossings against one clockwise and one diagonal, only 4 of 11 confirmed. The story is the eight-name IMPROVING->LAGGING flush: XBI is CONFIRMED at 9.97 past — the second leg of its two-week LEADING->LAGGING collapse — with IYF and VTV confirmed behind it while INDA/XLF/TLT/EFA/EWJ all sit <0.85 past on whipsaw watch. The lone clockwise print is constructive — XME confirmed LAGGING->IMPROVING at 1.77 — against SLX's provisional squeeze (sell, don't chase) and IWF's discontinuous WEAKENING->IMPROVING diagonal, which gets investigated not traded. The five provisional failures get their verdict on next week's print: hold past the boundary and the breakdown confirms; flip back and they were whipsaw.

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| USO | LEADING | 29.9 | ACCELERATING | ↗ | CONFIRMED | 167.22 |
| COMT | LEADING | 12.5 | DECELERATING | ↗ | CONFIRMED | 143.58 |
| XBI | LAGGING | 12.4 | DECELERATING | ↙ | TEMPORARY | 90.03 |
| XOP | LEADING | 11.4 | DECELERATING | ↗ | CONFIRMED | 148.57 |
| XPH | LAGGING | 10.9 | DECELERATING | ↙ | PENDING | 89.76 |
| DBC | LEADING | 10.6 | DECELERATING | ↗ | CONFIRMED | 140.57 |
| FCG | LEADING | 10.6 | ACCELERATING | ↗ | CONFIRMED | 138.83 |
| IEO | LEADING | 10.3 | DECELERATING | ↗ | CONFIRMED | 151.11 |
| IBB | LEADING | 9.8 | ACCELERATING | ↙ | CONFIRMED | 108.43 |
| XLE | LEADING | 9.6 | ACCELERATING | ↗ | CONFIRMED | 140.83 |

Dead money (velocity < 1.0): `REMX` 0.45, `EEM` 0.50, `HERO` 0.51, `EWY` 0.56, `JNK` 0.57, `HYG` 0.60, `VOT` 0.66, `XTN` 0.80, `XLC` 0.82, `SLV` 0.87, `AMLP` 0.88, `QQQ` 0.95, `IWF` 0.97

> Read: USO +29.9A ↗ — the largest squeeze climax of the series, still rotating up-right. Below it the polarity splits clean: energy/commodity leaders decelerate ↗ while the failures accelerate ↙ — XBI 12.4 ↙ completes the two-week LEADING->LAGGING collapse, XPH 10.9 ↙ behind it. The crossings are one-directional bearish: eight IMPROVING->LAGGING failures (EFA/EWJ/INDA/IYF/TLT/VTV/XBI/XLF) vs a single bottoming (XME); IWF's WEAKENING->IMPROVING jump is discontinuous — treat with suspicion. Dead money explodes to 13 names incl. QQQ — half the tape is frozen while oil squeezes.

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| BATT | 91.60 | 94.50 | 4.2 | 12 | 0.0 |
| EEM | 94.96 | 89.21 | 0.5 | 12 | 0.0 |
| GRID | 92.77 | 91.00 | 1.2 | 12 | 0.0 |
| ICLN | 83.61 | 84.26 | 4.6 | 12 | 0.0 |
| IFRA | 87.74 | 89.35 | 1.6 | 12 | 0.0 |
| LIT | 86.97 | 87.26 | 4.5 | 12 | 0.0 |
| PBW | 74.03 | 69.22 | 3.4 | 12 | 0.0 |
| QCLN | 80.27 | 70.09 | 4.3 | 12 | 0.0 |
| REMX | 67.73 | 74.71 | 0.5 | 12 | 0.0 |
| SMOG | 91.26 | 96.54 | 2.4 | 12 | 0.0 |

> Read: 47 LAGGING — the worst breadth print of the window. Buckets: clean energy owns the 12w cohort (ICLN/LIT/PBW/QCLN/BATT/SMOG), EM broad (EEM/EWY/VNM), grid/infra/rare-earths (GRID/IFRA/REMX), and two new structural weak zones — mega-cap growth (QQQ/SMH/VBK) and rate-sensitive real estate (IYR/SCHH/XLU). Everything not energy or defensive is being defunded.

## 8. Actionable Portfolio Tilts

- **Overweight** (10): `CANE`, `CLOU`, `COPX`, `FCG`, `HERO`, `NANR`, `USO`, `VDE`, `XLE`, `XME`
- **Hold-but-trim** — decelerating leaders (5): `COMT`, `DBC`, `GDX`, `IEO`, `XOP`
- **Reduce** — weakening (3): `CIBR`, `SLX`, `XLK`
- **Avoid** — structural laggards (19): `BATT`, `EEM`, `EWY`, `GRID`, `ICLN`, `IFRA`, `IYR`, `LIT`, `PBW`, `QCLN`, `QQQ`, `REMX`, `SCHH`, `SMH`, `SMOG`, `TAN`, `VBK`, `VNM`, `XLU`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (7): `AMLP`, `GLD`, `IHI`, `PALL`, `PLTM`, `SLV`, `XLC`

**Net call:** Late-cycle configuration confirmed: hold the energy complex (USO/XLE/VDE/FCG/CANE) but treat +29.9 as a squeeze to sell into, and keep the healthcare spine on streaks while its ↙ headings bar adds. The one live probe is metals bottoming — XME confirmed ↗, GLD/SLV on watch. Trigger: energy's ↗ deceleration flipping to ↙ heading, or a 12/12 healthcare name breaking to IMPROVING — either ends the current regime.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `INDA` (0/2), `UNG` (0/2)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
