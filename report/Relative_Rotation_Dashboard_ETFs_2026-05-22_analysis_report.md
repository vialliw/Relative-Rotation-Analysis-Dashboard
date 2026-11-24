# RRA Analysis Report — 2026-05-22

- **Data as-of:** 2026-05-22
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-05-22_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 22** | **IMPROVING: 6** | **WEAKENING: 12** | **LAGGING: 56**

> Weekly read: Same energy-led regime but narrowing — perfect leaders drop 15 to 10, LAGGING grows to 56, and every surviving leader heads ↙.
> The first genuine rotation seeds are heading-confirmed: XSW +11.4 and ARKK +6.3 both ↗.
> Arc week 2: mature regime, earliest credible successor signal.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (6)**<br>• Energy/commodity: `CORN`↙<br>• Defensive/rate-sensitive: `XLU`↙<br>• Financials/REITs: `SCHH`↙<br>• Growth/mega-cap tech: `ARKK`↗ `VOT`↗ `XSW`↗ | **LEADING (22)**<br>• Energy/commodity: `CANE`↙ `COMT`↙ `DBC`↙ `FCG`↙ `FTGC`↙ `IEO`↙ `SOYB`↙ `USO`↙ `WEAT`↙ `XOP`↙<br>• Metals/hard-asset: `SMOG`↙<br>• Growth/mega-cap tech: `CIBR`↗ `CLOU`↗ `IWF`↗ `QQQ`↗ `SMH`↗ `XLK`↗<br>• Clean energy: `ICLN`↗ `PBW`↗ `QCLN`↗<br>• EM/Intl: `EWY`↙<br>• Transports/infra/industrials: `GRID`↙ |
| **< 100** | **LAGGING (56)**<br>• Energy/commodity: `NANR`↙ `UNG`↘<br>• Metals/hard-asset: `COPX`↙ `CPER`↘ `DBB`↗ `GDX`↙ `GLD`↙ `PALL`↗ `PLTM`↗ `SLV`↗ `XME`↘<br>• Healthcare: `IBB`↙ `IHI`↙ `VHT`↙ `XBI`↘ `XLV`↙ `XPH`↙<br>• Defensive/rate-sensitive: `HYG`↙ `ITB`↙ `JNK`↙ `SGOV`↙ `TLT`↙ `XLP`↙<br>• Value/dividend/consumer: `IWD`↙ `VBR`↙ `VOE`↙ `VTV`↙ `XLB`↙ `XLY`↗ `XRT`↙<br>• Financials/REITs: `IAI`↗ `IYF`↙ `IYR`↙ `KRE`↙ `XLF`↙<br>• Growth/mega-cap tech: `AWAY`↗ `DIA`↙ `HERO`↗ `IWM`↙ `XLC`↙<br>• EM/Intl: `EFA`↙ `EWA`↙ `EWC`↙ `EWJ`↙ `EWZ`↙ `FXI`↙ `INDA`↙ `VGK`↙ `VNM`↙ `VXUS`↙<br>• Transports/infra/industrials: `IFRA`↙ `IYT`↙ `JETS`↙ `XAR`↗ `XLI`↙ `XTN`↙ | **WEAKENING (12)**<br>• Energy/commodity: `BCD`↙ `VDE`↙ `XES`↙ `XLE`↙<br>• Metals/hard-asset: `BATT`↙ `LIT`↖ `REMX`↙ `SLX`↙<br>• Growth/mega-cap tech: `VBK`↗<br>• Clean energy: `TAN`↘<br>• EM/Intl: `EEM`↙<br>• Other: `AMLP`↙ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XOP | LEADING | 109.44 | 106.43 | 10.9 | ACCELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| IEO | LEADING | 107.07 | 104.15 | 10.6 | ACCELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| FCG | LEADING | 106.93 | 101.34 | 10.3 | ACCELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| USO | LEADING | 168.38 | 164.77 | 7.5 | ACCELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| GRID | LEADING | 105.59 | 105.68 | 7.1 | ACCELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| COMT | LEADING | 120.67 | 116.84 | 4.5 | DECELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| DBC | LEADING | 117.90 | 111.67 | 2.9 | DECELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| FTGC | LEADING | 111.92 | 106.14 | 2.6 | DECELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| EWY | LEADING | 134.30 | 101.97 | 2.6 | ACCELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| WEAT | LEADING | 106.56 | 109.84 | 2.2 | DECELERATING | ↙ | PENDING | 12 | 0 | 100.0 |

> Read: Perfect-leader count drops 15 to 10 in one week — BCD/EWY/GRID/IFRA/SCHH/VDE/XLE lost streaks (VDE/XLE straight to WEAKENING, SCHH regime-broke to IMPROVING). The survivors are still 100% commodity complex — and all 10 head ↙, including the 'accelerators': XOP/IEO/FCG/USO are speeding toward LAGGING, not pressing new highs.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XSW | IMPROVING | 94.78 | 109.64 | 11.4 | ACCELERATING | ↗ | TEMPORARY | 0 | 11 | 0.0 |
| XLU | IMPROVING | 93.97 | 104.81 | 8.1 | ACCELERATING | ↙ | PENDING | 10 | 0 | 83.3 |
| ARKK | IMPROVING | 99.05 | 114.84 | 6.3 | ACCELERATING | ↗ | PENDING | 0 | 7 | 0.0 |
| SCHH | IMPROVING | 98.84 | 102.13 | 5.2 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| CORN | IMPROVING | 97.01 | 103.53 | 3.5 | ACCELERATING | ↙ | PENDING | 9 | 1 | 75.0 |
| VOT | IMPROVING | 97.42 | 104.56 | 0.7 | DECELERATING | ↗ | PENDING | 0 | 0 | 0.0 |

> Read: The 6-deep bench splits cleanly on heading — genuine improvers XSW +11.4 ↗ (off 11 lag weeks, Δmom +10.0), ARKK +6.3 ↗, VOT ↗; the rest are fading leaders (XLU/CORN ↙, SCHH ↙ fresh off a LEADING->IMPROVING regime break). The software/speculative probe is real; the 'improving' defensives are breakdowns in disguise.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| VDE | WEAKENING | 103.22 | 94.64 | 8.9 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| XLE | WEAKENING | 102.63 | 93.67 | 8.7 | DECELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| XES | WEAKENING | 113.64 | 94.37 | 8.4 | ACCELERATING | ↙ | PENDING | 10 | 0 | 83.3 |
| AMLP | WEAKENING | 101.17 | 95.61 | 3.6 | ACCELERATING | ↙ | PENDING | 10 | 0 | 83.3 |
| EEM | WEAKENING | 102.26 | 96.95 | 2.9 | ACCELERATING | ↙ | PENDING | 10 | 0 | 83.3 |
| SLX | WEAKENING | 102.20 | 84.88 | 2.8 | DECELERATING | ↙ | PENDING | 5 | 0 | 41.7 |
| BCD | WEAKENING | 104.79 | 98.31 | 2.7 | DECELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| LIT | WEAKENING | 112.59 | 97.85 | 2.2 | DECELERATING | ↖ | PENDING | 0 | 0 | 0.0 |
| BATT | WEAKENING | 102.67 | 91.62 | 2.0 | DECELERATING | ↙ | PENDING | 1 | 0 | 8.3 |
| REMX | WEAKENING | 106.17 | 86.13 | 1.9 | DECELERATING | ↙ | PENDING | 8 | 0 | 66.7 |
| TAN | WEAKENING | 105.42 | 94.16 | 1.2 | DECELERATING | ↘ | PENDING | 5 | 0 | 41.7 |
| VBK | WEAKENING | 100.99 | 98.66 | 0.6 | ACCELERATING | ↗ | PENDING | 9 | 0 | 75.0 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| COMT | LEADING | 120.67 | 116.84 | 4.5 | DECELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| DBC | LEADING | 117.90 | 111.67 | 2.9 | DECELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| FTGC | LEADING | 111.92 | 106.14 | 2.6 | DECELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| WEAT | LEADING | 106.56 | 109.84 | 2.2 | DECELERATING | ↙ | PENDING | 12 | 0 | 100.0 |
| QCLN | LEADING | 114.26 | 106.65 | 2.1 | DECELERATING | ↗ | PENDING | 4 | 0 | 33.3 |
| CANE | LEADING | 100.40 | 105.68 | 0.6 | DECELERATING | ↙ | PENDING | 6 | 0 | 50.0 |

> Read: Regime breaks lead the section — former perfect leaders BCD/VDE/XLE crossed LEADING->WEAKENING, and SCHH went LEADING->IMPROVING. The weakening list is near-uniform ↙ (only LIT ↖, TAN ↘, VBK ↗ flickers): the complex is shedding members from the top down. The decelerating-leader table is just the commodity core aging (COMT/DBC/FTGC/WEAT) — orderly, not panicked.

## 5. Quadrant Crossings

11 crossings this week: **8 confirmed / 3 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 3x IMPROVING->LAGGING, 3x LEADING->WEAKENING, 1x IMPROVING->LEADING, 1x LAGGING->IMPROVING, 1x LEADING->IMPROVING, 1x LEADING->LAGGING, 1x WEAKENING->LAGGING. 1 diagonal/discontinuous transition.

### Counter-clockwise — abrupt reversals

**LEADING->IMPROVING** — potential regime break / RS breakdown warning

- `SCHH` CONFIRMED — ↙, Δratio -3.31, Δmom -3.99 (landed ratio 98.84, 1.16 past boundary); quadrant_persistence TEMPORARY

**IMPROVING->LAGGING** — failed recovery / bearish continuation

- `EWA` CONFIRMED — ↙, Δratio -3.99, Δmom -6.84 (landed mom 96.53, 3.47 past boundary); quadrant_persistence TEMPORARY
- `TLT` CONFIRMED — ↙, Δratio -2.41, Δmom -3.04 (landed mom 97.56, 2.44 past boundary); quadrant_persistence TEMPORARY
- `IYR` PROVISIONAL_CROSSING — ↙, Δratio -2.74, Δmom -3.50 (landed mom 99.94, only 0.06 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**IMPROVING->LEADING** — possible rotation into leadership — confirm next week

- `IWF` PROVISIONAL_CROSSING — ↗, Δratio +1.38, Δmom +2.16 (landed ratio 100.97, only 0.97 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LEADING->WEAKENING** — potential distribution / early reversal — watch

- `VDE` CONFIRMED — ↙, Δratio -5.04, Δmom -7.34 (landed mom 94.64, 5.36 past boundary); quadrant_persistence TEMPORARY
- `XLE` CONFIRMED — ↙, Δratio -4.80, Δmom -7.24 (landed mom 93.67, 6.33 past boundary); quadrant_persistence TEMPORARY
- `BCD` CONFIRMED — ↙, Δratio -0.97, Δmom -2.49 (landed mom 98.31, 1.69 past boundary); quadrant_persistence TEMPORARY

**WEAKENING->LAGGING** — potential bearish continuation — confirm persistence

- `IWM` PROVISIONAL_CROSSING — ↙, Δratio -0.58, Δmom -0.89 (landed ratio 99.80, only 0.20 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LAGGING->IMPROVING** — early recovery attempt — unconfirmed

- `XSW` CONFIRMED — ↗, Δratio +5.41, Δmom +10.00 (landed mom 109.64, 9.64 past boundary); quadrant_persistence TEMPORARY

### Diagonal — discontinuous

**LEADING->LAGGING** — discontinuous regime change — investigate

- `IFRA` CONFIRMED — ↙, Δratio -4.53, Δmom -4.72 (landed ratio 97.33, mom 96.14, 2.67/3.86 past boundary); quadrant_persistence TEMPORARY

> Read: still one-directional — 9 of 11 crossings are bearish-flavored and all the key ones confirmed: VDE and XLE punch through LEADING->WEAKENING at 5.36 and 6.33 past the boundary, BCD ages out behind them, SCHH's LEADING->IMPROVING regime break is CONFIRMED, and IFRA's LEADING->LAGGING diagonal is the week's discontinuous loss. The lone confirmed bullish flow is XSW's LAGGING->IMPROVING bottoming — 9.64 past the momentum boundary, the successor signal the census hinted at. Provisionals get next week's verdict: IWF's IMPROVING->LEADING rotation (0.97 past — whipsaw watch), IYR's failed improvement (0.06) and IWM's breakdown (0.20).

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| XSW | IMPROVING | 11.4 | ACCELERATING | ↗ | TEMPORARY | 109.64 |
| CIBR | LEADING | 11.3 | ACCELERATING | ↗ | PENDING | 115.97 |
| CLOU | LEADING | 11.1 | ACCELERATING | ↗ | PENDING | 120.22 |
| XOP | LEADING | 10.9 | ACCELERATING | ↙ | PENDING | 106.43 |
| UNG | LAGGING | 10.7 | DECELERATING | ↘ | PENDING | 67.82 |
| IEO | LEADING | 10.6 | ACCELERATING | ↙ | PENDING | 104.15 |
| FCG | LEADING | 10.3 | ACCELERATING | ↙ | PENDING | 101.34 |
| EWZ | LAGGING | 9.5 | DECELERATING | ↙ | PENDING | 81.21 |
| VDE | WEAKENING | 8.9 | ACCELERATING | ↙ | TEMPORARY | 94.64 |
| XLE | WEAKENING | 8.7 | DECELERATING | ↙ | TEMPORARY | 93.67 |

Dead money (velocity < 1.0): `IHI` 0.13, `CANE` 0.57, `ICLN` 0.62, `XBI` 0.63, `VBK` 0.64, `VOT` 0.66, `XLY` 0.95, `DBB` 0.99

> Read: The three fastest movers are all tech heading ↗ — XSW +11.4, CIBR +11.3, CLOU +11.1 — direction-confirmed growth re-bid beneath the commodity surface. The mirror image: XOP/IEO/FCG accelerating ↙. The crossings show the cost — IFRA's discontinuous LEADING->LAGGING, EWA/IYR/TLT failed improvements, IWM breakdown confirmed — against bullish XSW bottoming and IWF rotation-confirmed.

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| AWAY | 86.11 | 98.20 | 4.0 | 12 | 0.0 |
| IHI | 77.79 | 81.95 | 0.1 | 12 | 0.0 |
| INDA | 85.82 | 94.25 | 3.8 | 12 | 0.0 |
| VHT | 87.62 | 84.06 | 1.1 | 12 | 0.0 |
| XLV | 86.74 | 82.85 | 1.5 | 11 | 0.0 |
| FXI | 86.15 | 90.69 | 2.6 | 9 | 0.0 |
| IAI | 93.63 | 90.16 | 2.7 | 9 | 0.0 |
| IYF | 89.94 | 89.47 | 1.4 | 9 | 0.0 |
| JETS | 84.22 | 75.30 | 1.9 | 9 | 16.7 |
| PALL | 77.41 | 64.41 | 2.0 | 9 | 16.7 |

> Read: 56 LAGGING and still healthcare-led (AWAY/INDA/VHT/IHI all 12w, XLV 11w), plus financials (IAI/IYF), travel/metals (JETS/PALL) and China (FXI). LAGGING rising while LEADING shrinks = breadth still deteriorating under the headline leadership.

## 8. Actionable Portfolio Tilts

- **Overweight** (10): `ARKK`, `CIBR`, `CLOU`, `ICLN`, `IWF`, `PBW`, `QQQ`, `SMH`, `XLK`, `XSW`
- **Hold-but-trim** — decelerating leaders (0): 
- **Reduce** — weakening (12): `AMLP`, `BATT`, `BCD`, `EEM`, `LIT`, `REMX`, `SLX`, `TAN`, `VBK`, `VDE`, `XES`, `XLE`
- **Avoid** — structural laggards (12): `AWAY`, `FXI`, `IAI`, `IHI`, `INDA`, `IYF`, `JETS`, `PALL`, `VHT`, `XLF`, `XLV`, `XLY`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (0): none

**Net call:** Hold the commodity core on trailing stops — every leader heads ↙, so expect stops to keep triggering — but fresh capital goes to the ↗ cluster (XSW/CIBR/CLOU/IWF/ARKK), which is the earliest heading-confirmed successor. The trigger that kills it: those tech probes flipping ↙, which would leave no successor regime at all.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `BATT` (1/0), `LIT` (0/0), `PBW` (2/0), `VOT` (0/0), `XBI` (0/2)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
