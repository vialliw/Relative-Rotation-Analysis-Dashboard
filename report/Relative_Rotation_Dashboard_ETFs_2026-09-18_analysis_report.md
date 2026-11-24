# RRA Analysis Report — 2026-09-18

- **Data as-of:** 2026-09-18
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-09-18_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 41** | **IMPROVING: 27** | **WEAKENING: 5** | **LAGGING: 23**

> Weekly read: Precious metals go parabolic — SLV +10.9A, PLTM +10.6A, both ↗ — and biotech/pharma joins the 12/12 club.
> But the compass turned hostile: every consistent leader now heads ↙ or ↖.
> Best two-sided tape since May, and the most fragile leadership of the window.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (27)**<br>• Energy/commodity: `UNG`↙<br>• Metals/hard-asset: `CPER`↗ `GLD`↗ `PLTM`↗ `SLV`↗ `XME`↙<br>• Defensive/rate-sensitive: `HYG`↖ `ITB`↙ `JNK`↖ `SGOV`↗ `TLT`↖ `XLP`↖ `XLU`↖<br>• Value/dividend/consumer: `VBR`↙ `XLB`↙ `XLY`↙ `XRT`↙<br>• Financials/REITs: `IYR`↙ `SCHH`↙<br>• Growth/mega-cap tech: `VOT`↙ `XLC`↗<br>• EM/Intl: `FXI`↖ `INDA`↖ `VNM`↗<br>• Transports/infra/industrials: `IYT`↙ `JETS`↙ `XLI`↙ | **LEADING (41)**<br>• Energy/commodity: `BCD`↗ `CANE`↗ `CORN`↗ `FCG`↗ `IEO`↗ `NANR`↗ `SOYB`↗ `VDE`↗ `WEAT`↗ `XLE`↗ `XOP`↗<br>• Metals/hard-asset: `COPX`↙ `GDX`↗ `PALL`↖<br>• Healthcare: `IBB`↙ `IHI`↙ `VHT`↙ `XBI`↖ `XLV`↙ `XPH`↙<br>• Value/dividend/consumer: `IWD`↙ `VOE`↙ `VTV`↙<br>• Financials/REITs: `IAI`↙ `IYF`↙ `KRE`↙ `XLF`↙<br>• Growth/mega-cap tech: `ARKK`↗ `AWAY`↙ `CLOU`↙ `DIA`↙ `HERO`↗ `XSW`↙<br>• EM/Intl: `EFA`↙ `EWA`↖ `EWC`↖ `EWJ`↗ `EWZ`↗ `VGK`↙ `VXUS`↖<br>• Other: `AMLP`↗ |
| **< 100** | **LAGGING (23)**<br>• Energy/commodity: `XES`↗<br>• Metals/hard-asset: `BATT`↖ `DBB`↗ `LIT`↖ `REMX`↖ `SLX`↙ `SMOG`↗<br>• Growth/mega-cap tech: `IWF`↗ `IWM`↙ `QQQ`↘ `SMH`↙ `VBK`↙ `XLK`↙<br>• Clean energy: `ICLN`↗ `PBW`↘ `QCLN`↘ `TAN`↙<br>• EM/Intl: `EEM`↖ `EWY`↖<br>• Transports/infra/industrials: `GRID`↗ `IFRA`↙ `XAR`↙ `XTN`↙ | **WEAKENING (5)**<br>• Energy/commodity: `COMT`↗ `DBC`↗ `FTGC`↗ `USO`↗<br>• Growth/mega-cap tech: `CIBR`↘ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XSW | LEADING | 112.97 | 113.61 | 6.4 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| CLOU | LEADING | 113.42 | 103.10 | 4.5 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| XPH | LEADING | 113.72 | 125.41 | 4.0 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| XBI | LEADING | 116.03 | 121.10 | 1.9 | DECELERATING | ↖ | CONFIRMED | 12 | 0 | 100.0 |
| AWAY | LEADING | 101.18 | 119.77 | 10.1 | ACCELERATING | ↙ | CONFIRMED | 11 | 0 | 91.7 |
| KRE | LEADING | 101.70 | 113.36 | 4.9 | ACCELERATING | ↙ | CONFIRMED | 9 | 0 | 75.0 |
| IAI | LEADING | 101.80 | 106.92 | 3.6 | ACCELERATING | ↙ | CONFIRMED | 9 | 0 | 75.0 |
| IYF | LEADING | 105.13 | 116.68 | 3.5 | ACCELERATING | ↙ | CONFIRMED | 9 | 0 | 75.0 |
| XLV | LEADING | 107.96 | 125.57 | 3.3 | DECELERATING | ↙ | CONFIRMED | 9 | 3 | 75.0 |
| XLF | LEADING | 106.10 | 117.44 | 3.1 | ACCELERATING | ↙ | CONFIRMED | 9 | 0 | 75.0 |

> Read: A new consistent cohort on paper — CLOU/XBI/XPH/XSW all 12/12, plus financials (IAI/IYF/XLF/KRE) — yet all ten leaders head left: nine ↙, XBI ↖. Streaks say persistence; headings say these are leaders in label this week and IMPROVING candidates next.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| SLV | IMPROVING | 90.46 | 110.39 | 10.9 | ACCELERATING | ↗ | TEMPORARY | 0 | 11 | 0.0 |
| PLTM | IMPROVING | 97.12 | 119.44 | 10.6 | ACCELERATING | ↗ | CONFIRMED | 0 | 8 | 0.0 |
| JETS | IMPROVING | 95.29 | 111.86 | 10.3 | ACCELERATING | ↙ | PENDING | 10 | 0 | 83.3 |
| ITB | IMPROVING | 93.40 | 126.99 | 8.3 | ACCELERATING | ↙ | PENDING | 3 | 1 | 25.0 |
| UNG | IMPROVING | 86.49 | 100.73 | 7.9 | ACCELERATING | ↙ | CONFIRMED | 0 | 6 | 0.0 |
| GLD | IMPROVING | 97.65 | 121.42 | 6.3 | ACCELERATING | ↗ | CONFIRMED | 0 | 8 | 0.0 |
| IYT | IMPROVING | 94.15 | 103.92 | 5.9 | ACCELERATING | ↙ | PENDING | 6 | 0 | 50.0 |
| XRT | IMPROVING | 97.39 | 115.58 | 5.1 | ACCELERATING | ↙ | TEMPORARY | 4 | 1 | 33.3 |
| XME | IMPROVING | 90.88 | 100.43 | 5.1 | ACCELERATING | ↙ | CONFIRMED | 0 | 8 | 0.0 |
| VNM | IMPROVING | 94.89 | 104.24 | 4.6 | DECELERATING | ↗ | TEMPORARY | 0 | 11 | 0.0 |

> Read: The genuine improving cohort is precious metals plus one EM: SLV +10.9A, PLTM +10.6A, GLD +6.3A, VNM +4.6D — all ↗. The rest of the top-10 are fading names parked in IMPROVING: JETS/ITB/UNG/IYT/XRT/XME all head ↙ (XRT is a fresh LEADING->IMPROVING regime break). The metals bid widening down the curve is real; the "broad" bench is half-broken.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| USO | WEAKENING | 112.88 | 69.61 | 14.6 | ACCELERATING | ↗ | PENDING | 0 | 10 | 0.0 |
| COMT | WEAKENING | 107.95 | 91.90 | 10.0 | ACCELERATING | ↗ | PENDING | 0 | 10 | 0.0 |
| DBC | WEAKENING | 108.99 | 95.17 | 9.3 | ACCELERATING | ↗ | PENDING | 0 | 10 | 0.0 |
| CIBR | WEAKENING | 107.52 | 89.45 | 7.2 | DECELERATING | ↘ | PENDING | 10 | 0 | 83.3 |
| FTGC | WEAKENING | 107.17 | 98.58 | 6.5 | ACCELERATING | ↗ | CONFIRMED | 0 | 9 | 0.0 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| GDX | LEADING | 114.27 | 154.74 | 12.3 | DECELERATING | ↗ | CONFIRMED | 4 | 7 | 33.3 |
| EWZ | LEADING | 105.98 | 120.68 | 9.7 | DECELERATING | ↗ | PENDING | 2 | 9 | 16.7 |
| PALL | LEADING | 100.32 | 142.16 | 9.1 | DECELERATING | ↖ | PENDING | 2 | 7 | 16.7 |
| CORN | LEADING | 111.89 | 119.14 | 8.8 | DECELERATING | ↗ | CONFIRMED | 3 | 9 | 25.0 |
| XOP | LEADING | 113.60 | 109.73 | 7.6 | DECELERATING | ↗ | PENDING | 2 | 8 | 16.7 |
| FCG | LEADING | 106.30 | 106.58 | 7.3 | DECELERATING | ↗ | TEMPORARY | 1 | 9 | 8.3 |
| IEO | LEADING | 118.54 | 116.12 | 7.3 | DECELERATING | ↗ | CONFIRMED | 3 | 4 | 25.0 |
| XSW | LEADING | 112.97 | 113.61 | 6.4 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| SOYB | LEADING | 109.44 | 111.73 | 5.9 | DECELERATING | ↗ | CONFIRMED | 3 | 8 | 25.0 |
| VDE | LEADING | 109.95 | 111.31 | 5.8 | DECELERATING | ↗ | PENDING | 2 | 8 | 16.7 |

> Read: Only 5 weakening, and only one is a leader: CIBR (83.3% consist) now ↘ — ratio still rising but momentum rolled. USO/COMT/DBC/FTGC are ↗ squeezes again — the same counter-trend pattern, still sells. On the decel list GDX/EWZ/CORN/XOP/FCG/IEO/VDE all hold ↗: rotation cooling, not breaking.

## 5. Quadrant Crossings

10 crossings this week: **8 confirmed / 2 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 3x IMPROVING->LAGGING, 3x LEADING->IMPROVING, 2x LAGGING->IMPROVING, 2x WEAKENING->LEADING. No diagonal/discontinuous transitions.

### Counter-clockwise — abrupt reversals

**LEADING->IMPROVING** — potential regime break / RS breakdown warning

- `XRT` CONFIRMED — ↙, Δratio -3.73, Δmom -3.52 (landed ratio 97.39, 2.61 past boundary); quadrant_persistence TEMPORARY
- `XLB` CONFIRMED — ↙, Δratio -3.14, Δmom -0.74 (landed ratio 97.07, 2.93 past boundary); quadrant_persistence TEMPORARY
- `VBR` PROVISIONAL_CROSSING — ↙, Δratio -2.37, Δmom -1.99 (landed ratio 99.78, only 0.22 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**IMPROVING->LAGGING** — failed recovery / bearish continuation

- `XTN` CONFIRMED — ↙, Δratio -4.52, Δmom -6.99 (landed mom 94.05, 5.95 past boundary); quadrant_persistence TEMPORARY
- `XAR` CONFIRMED — ↙, Δratio -3.44, Δmom -5.56 (landed mom 97.84, 2.16 past boundary); quadrant_persistence TEMPORARY
- `IWM` PROVISIONAL_CROSSING — ↙, Δratio -2.03, Δmom -2.17 (landed mom 99.62, only 0.38 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**WEAKENING->LEADING** — possible re-acceleration — verify follow-through

- `FCG` CONFIRMED — ↗, Δratio +1.47, Δmom +7.16 (landed mom 106.58, 6.58 past boundary); quadrant_persistence TEMPORARY
- `BCD` CONFIRMED — ↗, Δratio +2.39, Δmom +5.43 (landed mom 102.21, 2.21 past boundary); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**LAGGING->IMPROVING** — early recovery attempt — unconfirmed

- `SLV` CONFIRMED — ↗, Δratio +3.29, Δmom +10.42 (landed mom 110.39, 10.39 past boundary); quadrant_persistence TEMPORARY
- `VNM` CONFIRMED — ↗, Δratio +0.73, Δmom +4.54 (landed mom 104.24, 4.24 past boundary); quadrant_persistence TEMPORARY

> Read: two-sided tape with the damage confirmed — 8 of 10 crossings CONFIRMED. The bearish flow is the cyclical unwind continuing: XRT/XLB LEADING->IMPROVING regime breaks plus XTN/XAR IMPROVING->LAGGING failures — the old transport/retail leadership liquidating in both directions. The bullish flow is the metals bid widening: SLV's LAGGING->IMPROVING bottoming CONFIRMED 10.39 past the boundary with VNM behind it, and FCG/BCD's WEAKENING->LEADING re-accelerations keeping the energy squeeze alive — sells on strength, but confirmed strength. Only VBR (0.22) and IWM (0.38) sit on whipsaw watch.

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| USO | WEAKENING | 14.6 | ACCELERATING | ↗ | PENDING | 69.61 |
| GDX | LEADING | 12.3 | DECELERATING | ↗ | CONFIRMED | 154.74 |
| SLV | IMPROVING | 10.9 | ACCELERATING | ↗ | TEMPORARY | 110.39 |
| PLTM | IMPROVING | 10.6 | ACCELERATING | ↗ | CONFIRMED | 119.44 |
| JETS | IMPROVING | 10.3 | ACCELERATING | ↙ | PENDING | 111.86 |
| AWAY | LEADING | 10.1 | ACCELERATING | ↙ | CONFIRMED | 119.77 |
| COMT | WEAKENING | 10.0 | ACCELERATING | ↗ | PENDING | 91.90 |
| EWZ | LEADING | 9.7 | DECELERATING | ↗ | PENDING | 120.68 |
| DBC | WEAKENING | 9.3 | ACCELERATING | ↗ | PENDING | 95.17 |
| PALL | LEADING | 9.1 | DECELERATING | ↖ | PENDING | 142.16 |

Dead money (velocity < 1.0): `CPER` 0.24, `QQQ` 0.36, `JNK` 0.49, `HYG` 0.53, `SGOV` 0.92

> Read: USO +14.6A heads ↗ — the biggest squeeze yet, still a sell. GDX +12.3D cools a second week but stays ↗; SLV/PLTM took the baton. Crossings turn mixed: SLV's LAGGING->IMPROVING confirms the metals bottoming, but three failed improvements (IWM/XAR/XTN ->LAGGING) and three regime breaks (VBR/XLB/XRT LEADING->IMPROVING) show the old cyclical leadership liquidating.

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| BATT | 88.58 | 91.59 | 2.2 | 12 | 0.0 |
| DBB | 96.85 | 97.62 | 1.3 | 12 | 0.0 |
| ICLN | 78.91 | 69.77 | 2.0 | 12 | 0.0 |
| IFRA | 92.21 | 99.90 | 1.7 | 12 | 0.0 |
| LIT | 85.10 | 81.35 | 2.4 | 12 | 0.0 |
| REMX | 73.71 | 78.99 | 3.6 | 12 | 0.0 |
| SMOG | 90.76 | 91.86 | 2.0 | 12 | 0.0 |
| TAN | 68.24 | 63.60 | 2.8 | 12 | 0.0 |
| XES | 96.63 | 92.70 | 5.3 | 12 | 0.0 |
| GRID | 92.03 | 91.17 | 2.0 | 11 | 0.0 |

> Read: 23 LAGGING; the clean-energy cohort is now fully pinned (XES/REMX/TAN/LIT/BATT/SMOG all 12w, GRID/IFRA joining) — the structural short has consolidated into a single theme and funds everything above it.

## 8. Actionable Portfolio Tilts

- **Overweight** (9): `AMLP`, `ARKK`, `BCD`, `CANE`, `GLD`, `PLTM`, `SLV`, `WEAT`, `XBI`
- **Hold-but-trim** — decelerating leaders (10): `CORN`, `EWZ`, `FCG`, `GDX`, `IEO`, `PALL`, `SOYB`, `VDE`, `XOP`, `XSW`
- **Reduce** — weakening (5): `CIBR`, `COMT`, `DBC`, `FTGC`, `USO`
- **Avoid** — structural laggards (14): `BATT`, `DBB`, `EEM`, `GRID`, `ICLN`, `IFRA`, `LIT`, `PBW`, `QCLN`, `REMX`, `SLX`, `SMOG`, `TAN`, `XES`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (7): `FXI`, `INDA`, `ITB`, `JETS`, `XLB`, `XLP`, `XRT`

**Net call:** Metals broadening to SLV/PLTM is the one confirmed bid; the "new persistent leadership" in pharma/financials is all ↙-heading — hold XBI, do not add. Clean energy stays the funded short. Trigger: a second ↙ week on XPH/XBI plus failures in the ↙-heading improvers flips this to capital-preservation.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `INDA` (0/2)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
