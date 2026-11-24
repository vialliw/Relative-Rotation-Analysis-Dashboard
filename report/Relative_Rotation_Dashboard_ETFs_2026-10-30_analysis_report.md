# RRA Analysis Report — 2026-10-30

- **Data as-of:** 2026-10-30
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-10-30_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 28** | **IMPROVING: 32** | **WEAKENING: 2** | **LAGGING: 34**

> Weekly read: Breadth inflection — IMPROVING swells to 32 (series high) and LAGGING falls to 34; seven names bottomed off the lagging floor.
> But the improvement lives in beaten-down names while leadership took its first real regime breaks (CORN/COPX/SLX/EWJ out of LEADING) and energy's heading went ↙ — this is rotation underneath a cracking top, not a clean rally.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (32)**<br>• Energy/commodity: `CORN`↙ `UNG`↙ `WEAT`↙ `XES`↙<br>• Metals/hard-asset: `BATT`↖ `COPX`↖ `DBB`↖ `GLD`↙ `LIT`↖ `PALL`↙ `PLTM`↙ `SLV`↖ `SLX`↖ `SMOG`↗ `XME`↖<br>• Defensive/rate-sensitive: `HYG`↗ `JNK`↗ `SGOV`↘ `TLT`↗ `XLU`↗<br>• Value/dividend/consumer: `XLB`↗ `XLY`↗<br>• Growth/mega-cap tech: `XLC`↙<br>• EM/Intl: `EFA`↗ `EWA`↗ `EWJ`↖ `FXI`↙ `INDA`↗ `VGK`↗ `VNM`↗ `VXUS`↗<br>• Other: `AMLP`↙ | **LEADING (28)**<br>• Energy/commodity: `BCD`↙ `CANE`↙ `COMT`↙ `DBC`↙ `FCG`↘ `FTGC`↙ `IEO`↙ `NANR`↙ `SOYB`↙ `USO`↙ `VDE`↙ `XLE`↙ `XOP`↙<br>• Metals/hard-asset: `CPER`↖ `GDX`↖<br>• Healthcare: `IBB`↘ `IHI`↗ `VHT`↗ `XLV`↗<br>• Defensive/rate-sensitive: `XLP`↗<br>• Value/dividend/consumer: `VOE`↗ `VTV`↗<br>• Growth/mega-cap tech: `ARKK`↗ `CLOU`↙ `HERO`↘ `XSW`↘<br>• EM/Intl: `EWC`↗ `EWZ`↖ |
| **< 100** | **LAGGING (34)**<br>• Metals/hard-asset: `REMX`↗<br>• Healthcare: `XBI`↗ `XPH`↘<br>• Defensive/rate-sensitive: `ITB`↗<br>• Value/dividend/consumer: `VBR`↗ `XRT`↗<br>• Financials/REITs: `IAI`↘ `IYF`↘ `IYR`↗ `KRE`↗ `SCHH`↗ `XLF`↘<br>• Growth/mega-cap tech: `AWAY`↗ `DIA`↗ `IWF`↙ `IWM`↗ `QQQ`↖ `SMH`↖ `VBK`↗ `VOT`↖ `XLK`↖<br>• Clean energy: `ICLN`↗ `PBW`↗ `QCLN`↗ `TAN`↗<br>• EM/Intl: `EEM`↖ `EWY`↖<br>• Transports/infra/industrials: `GRID`↖ `IFRA`↗ `IYT`↗ `JETS`↗ `XAR`↗ `XLI`↗ `XTN`↗ | **WEAKENING (2)**<br>• Value/dividend/consumer: `IWD`↗<br>• Growth/mega-cap tech: `CIBR`↙ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| CLOU | LEADING | 119.18 | 110.52 | 6.3 | ACCELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| IBB | LEADING | 107.80 | 103.46 | 4.0 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| XLV | LEADING | 109.72 | 107.74 | 3.8 | DECELERATING | ↗ | CONFIRMED | 12 | 0 | 100.0 |
| XSW | LEADING | 116.49 | 104.39 | 3.7 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| VHT | LEADING | 107.93 | 104.94 | 3.6 | DECELERATING | ↗ | CONFIRMED | 12 | 0 | 100.0 |
| CANE | LEADING | 120.88 | 138.96 | 4.8 | ACCELERATING | ↙ | CONFIRMED | 11 | 0 | 91.7 |
| ARKK | LEADING | 105.44 | 104.52 | 2.2 | DECELERATING | ↗ | CONFIRMED | 11 | 1 | 91.7 |
| HERO | LEADING | 106.60 | 123.55 | 1.4 | DECELERATING | ↘ | CONFIRMED | 11 | 0 | 91.7 |
| GDX | LEADING | 108.08 | 152.15 | 7.9 | ACCELERATING | ↖ | CONFIRMED | 10 | 1 | 83.3 |
| NANR | LEADING | 109.42 | 132.81 | 1.5 | DECELERATING | ↙ | CONFIRMED | 10 | 1 | 83.3 |

> Read: Ten consistent leaders — eight at 11-12/12 — but the cohort splits: healthcare re-stabilizes (XLV/VHT heading ↗, IBB ↘-decel) and ARKK quietly turns ↗, while the hard-asset/soft names deteriorate — CANE +4.8A and CLOU +6.3A accelerating ↙, NANR ↙-decel, GDX rolling ↖. Streaks say the spine is intact; headings say the ag/cloud layer is losing altitude on both axes.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| WEAT | IMPROVING | 91.30 | 105.11 | 12.8 | ACCELERATING | ↙ | PENDING | 6 | 2 | 50.0 |
| CORN | IMPROVING | 97.37 | 119.44 | 10.4 | ACCELERATING | ↙ | TEMPORARY | 8 | 3 | 66.7 |
| VNM | IMPROVING | 95.14 | 101.48 | 7.7 | ACCELERATING | ↗ | TEMPORARY | 0 | 8 | 0.0 |
| LIT | IMPROVING | 86.66 | 101.03 | 6.7 | DECELERATING | ↖ | TEMPORARY | 0 | 11 | 0.0 |
| COPX | IMPROVING | 96.88 | 116.30 | 5.9 | DECELERATING | ↖ | TEMPORARY | 10 | 1 | 83.3 |
| FXI | IMPROVING | 95.13 | 118.39 | 5.6 | ACCELERATING | ↙ | PENDING | 2 | 0 | 16.7 |
| XLB | IMPROVING | 99.84 | 106.60 | 5.4 | ACCELERATING | ↗ | PENDING | 3 | 4 | 25.0 |
| BATT | IMPROVING | 88.83 | 105.71 | 5.3 | DECELERATING | ↖ | PENDING | 0 | 10 | 0.0 |
| XME | IMPROVING | 95.20 | 115.06 | 5.3 | DECELERATING | ↖ | CONFIRMED | 0 | 5 | 0.0 |
| PALL | IMPROVING | 81.51 | 113.01 | 4.8 | DECELERATING | ↙ | CONFIRMED | 2 | 1 | 16.7 |

> Read: 32 improvers — series high — but the two fastest are a warning, not a bid: WEAT +12.8 and CORN +10.4 are accelerating ↙, and CORN is a LEADING->IMPROVING regime break (Δ-3.9/-9.6). Last week's ag-bottoming read is wrong — ag leadership is breaking. The genuine ↗ improvers are VNM +7.7 (EM-Asia) and XLB +5.4; the metals/materials bench (COPX/XME/BATT/LIT) is ↖ momentum-only, and FXI/PALL fade ↙. Successor regime = EM-Asia + materials — thin.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| CIBR | WEAKENING | 109.90 | 87.18 | 4.2 | DECELERATING | ↙ | CONFIRMED | 4 | 0 | 33.3 |
| IWD | WEAKENING | 102.08 | 99.62 | 1.3 | DECELERATING | ↗ | PENDING | 7 | 2 | 58.3 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| USO | LEADING | 133.58 | 173.38 | 8.8 | DECELERATING | ↙ | CONFIRMED | 5 | 4 | 41.7 |
| XLE | LEADING | 118.72 | 140.66 | 5.4 | DECELERATING | ↙ | CONFIRMED | 9 | 1 | 75.0 |
| VDE | LEADING | 117.25 | 139.66 | 5.3 | DECELERATING | ↙ | CONFIRMED | 8 | 2 | 66.7 |
| IBB | LEADING | 107.80 | 103.46 | 4.0 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| XLV | LEADING | 109.72 | 107.74 | 3.8 | DECELERATING | ↗ | CONFIRMED | 12 | 0 | 100.0 |
| IHI | LEADING | 105.29 | 119.73 | 3.8 | DECELERATING | ↗ | PENDING | 9 | 0 | 75.0 |
| XLP | LEADING | 103.18 | 108.26 | 3.8 | DECELERATING | ↗ | TEMPORARY | 1 | 1 | 8.3 |
| XSW | LEADING | 116.49 | 104.39 | 3.7 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| VHT | LEADING | 107.93 | 104.94 | 3.6 | DECELERATING | ↗ | CONFIRMED | 12 | 0 | 100.0 |
| FCG | LEADING | 113.05 | 142.35 | 3.4 | DECELERATING | ↘ | CONFIRMED | 7 | 3 | 58.3 |

> Read: No new WEAKENING admissions — just CIBR grinding ↙ and IWD drifting ↗ — so distribution is still narrow. The threat migrated to the decel board: USO 8.8, XLE 5.4 and VDE 5.3 now decelerate heading ↙ — both deltas negative, a real rollover (last week they were still ↗) — while healthcare XLV/VHT/IHI/XLP decelerate ↗ in good order. Energy is the first leadership bloc in genuine retreat; ags are following via the CORN/COPX/SLX regime breaks.

## 5. Quadrant Crossings

17 crossings this week: **10 confirmed / 7 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 7x LAGGING->IMPROVING, 4x LEADING->IMPROVING, 3x IMPROVING->LEADING, 1x IMPROVING->LAGGING, 1x LAGGING->LEADING, 1x WEAKENING->LAGGING. 1 diagonal/discontinuous transition.

### Counter-clockwise — abrupt reversals

**LEADING->IMPROVING** — potential regime break / RS breakdown warning

- `CORN` CONFIRMED — ↙, Δratio -3.94, Δmom -9.63 (landed ratio 97.37, 2.63 past boundary); quadrant_persistence TEMPORARY
- `COPX` CONFIRMED — ↖, Δratio -5.48, Δmom +2.21 (landed ratio 96.88, 3.12 past boundary); quadrant_persistence TEMPORARY
- `SLX` CONFIRMED — ↖, Δratio -2.40, Δmom +1.91 (landed ratio 97.68, 2.32 past boundary); quadrant_persistence TEMPORARY
- `EWJ` PROVISIONAL_CROSSING — ↖, Δratio -0.30, Δmom +1.66 (landed ratio 99.94, only 0.06 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**IMPROVING->LAGGING** — failed recovery / bearish continuation

- `IWF` PROVISIONAL_CROSSING — ↙, Δratio -1.08, Δmom -0.33 (landed mom 99.74, only 0.26 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**IMPROVING->LEADING** — possible rotation into leadership — confirm next week

- `XLP` CONFIRMED — ↗, Δratio +3.35, Δmom +1.71 (landed ratio 103.18, 3.18 past boundary); quadrant_persistence TEMPORARY
- `VOE` CONFIRMED — ↗, Δratio +1.38, Δmom +0.51 (landed ratio 101.01, 1.01 past boundary); quadrant_persistence TEMPORARY
- `EWC` PROVISIONAL_CROSSING — ↗, Δratio +0.86, Δmom +0.59 (landed ratio 100.54, only 0.54 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**WEAKENING->LAGGING** — potential bearish continuation — confirm persistence

- `XLK` PROVISIONAL_CROSSING — ↖, Δratio -1.83, Δmom +0.79 (landed ratio 99.72, only 0.28 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LAGGING->IMPROVING** — early recovery attempt — unconfirmed

- `VNM` CONFIRMED — ↗, Δratio +4.12, Δmom +6.49 (landed mom 101.48, 1.48 past boundary); quadrant_persistence TEMPORARY
- `LIT` CONFIRMED — ↖, Δratio -0.31, Δmom +6.68 (landed mom 101.03, 1.03 past boundary); quadrant_persistence TEMPORARY
- `XLY` CONFIRMED — ↗, Δratio +3.65, Δmom +3.18 (landed mom 101.83, 1.83 past boundary); quadrant_persistence TEMPORARY
- `SMOG` CONFIRMED — ↗, Δratio +1.08, Δmom +3.60 (landed mom 103.27, 3.27 past boundary); quadrant_persistence TEMPORARY
- `INDA` CONFIRMED — ↗, Δratio +2.77, Δmom +2.44 (landed mom 101.37, 1.37 past boundary); quadrant_persistence TEMPORARY
- `VGK` PROVISIONAL_CROSSING — ↗, Δratio +1.57, Δmom +1.69 (landed mom 100.05, only 0.05 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `VXUS` PROVISIONAL_CROSSING — ↗, Δratio +0.31, Δmom +1.65 (landed mom 100.11, only 0.11 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

### Diagonal — discontinuous

**LAGGING->LEADING** — discontinuous regime change — investigate

- `VTV` PROVISIONAL_CROSSING — ↗, Δratio +1.54, Δmom +0.89 (landed ratio 101.11, mom 100.74, only 1.11/0.74 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

> Read: the balance flips constructive — eleven clockwise crossings against five counter-clockwise plus one diagonal, 10 of 17 confirmed. The bearish side is all at the top: three confirmed LEADING->IMPROVING regime breaks (CORN 2.63, COPX 3.12, SLX 2.32 past) with EWJ's a hair-thin provisional at 0.06, and IWF's provisional slide back to LAGGING. The clockwise side is a genuine bottoming bid — five confirmed LAGGING->IMPROVING repairs (VNM/LIT/XLY/SMOG/INDA) with VGK/VXUS <0.12 past on whipsaw watch — plus XLP's confirmed promotion beside VOE (EWC provisional). XLK's provisional WEAKENING->LAGGING slide and VTV's discontinuous LAGGING->LEADING diagonal are the two to verify — hold past the boundary and they confirm; flip back and they were whipsaw.

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| WEAT | IMPROVING | 12.8 | ACCELERATING | ↙ | PENDING | 105.11 |
| EWZ | LEADING | 10.7 | ACCELERATING | ↖ | CONFIRMED | 137.81 |
| CORN | IMPROVING | 10.4 | ACCELERATING | ↙ | TEMPORARY | 119.44 |
| USO | LEADING | 8.8 | DECELERATING | ↙ | CONFIRMED | 173.38 |
| REMX | LAGGING | 8.5 | ACCELERATING | ↗ | CONFIRMED | 87.89 |
| IEO | LEADING | 8.1 | ACCELERATING | ↙ | CONFIRMED | 146.89 |
| GDX | LEADING | 7.9 | ACCELERATING | ↖ | CONFIRMED | 152.15 |
| VNM | IMPROVING | 7.7 | ACCELERATING | ↗ | TEMPORARY | 101.48 |
| XOP | LEADING | 7.5 | ACCELERATING | ↙ | CONFIRMED | 145.70 |
| ITB | LAGGING | 6.8 | ACCELERATING | ↗ | CONFIRMED | 89.73 |

Dead money (velocity < 1.0): `XLI` 0.72, `DBB` 0.79, `IAI` 0.84, `SCHH` 0.85, `JNK` 0.95, `HYG` 0.97, `IYF` 0.97, `IYR` 0.99, `SGOV` 0.99

> Read: Velocity is now a two-way tape — WEAT +12.8 and CORN +10.4 accelerate ↙ (breakdown speed, not bottoming speed) and IEO +8.1/XOP +7.5 accelerate ↙ inside LEADING: the energy squeeze is over and reversing. The real bids: REMX +8.5 ↗ off a deep floor (squeeze — don't chase), EWZ +10.7 ↖ (momentum only), VNM +7.7 and ITB +6.8 ↗. Seventeen crossings skew constructive — seven bottoming (INDA/LIT/SMOG/VGK/VNM/VXUS/XLY), three rotations into LEADING (XLP/VOE confirmed, EWC provisional) — against XLK's WEAKENING->LAGGING slide (provisional) and four LEADING->IMPROVING regime breaks (COPX/CORN/EWJ/SLX): the top is breaking while the bottom repairs.

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| EEM | 94.10 | 94.01 | 2.5 | 12 | 0.0 |
| EWY | 87.73 | 72.80 | 4.7 | 12 | 0.0 |
| GRID | 90.30 | 95.05 | 2.1 | 12 | 0.0 |
| ICLN | 84.26 | 91.44 | 3.1 | 12 | 0.0 |
| IFRA | 90.95 | 93.93 | 2.3 | 12 | 0.0 |
| PBW | 74.00 | 76.34 | 4.1 | 12 | 0.0 |
| QCLN | 80.80 | 79.14 | 5.0 | 12 | 0.0 |
| QQQ | 98.03 | 93.00 | 1.1 | 12 | 0.0 |
| REMX | 69.47 | 87.89 | 8.5 | 12 | 0.0 |
| TAN | 75.31 | 84.58 | 2.3 | 12 | 0.0 |

> Read: 34 LAGGING — count still falling. The 12w cohort buckets cleanly: clean energy (ICLN/PBW/QCLN/TAN), EM Asia (EEM/EWY), grid/infra (GRID/IFRA) — REMX trying to leave at +8.5 ↗ — and the fourth bucket is new: mega-cap growth, with QQQ printing its 12th lag week and SMH/VBK/IWF in the avoid tail. This cohort is the funding pool for the defensive/EM rotation.

## 8. Actionable Portfolio Tilts

- **Overweight** (12): `ARKK`, `COPX`, `EWZ`, `GDX`, `HERO`, `IBB`, `IHI`, `VHT`, `VNM`, `XLB`, `XLV`, `XSW`
- **Hold-but-trim** — decelerating leaders (3): `USO`, `VDE`, `XLE`
- **Reduce** — weakening (2): `CIBR`, `IWD`
- **Avoid** — structural laggards (15): `EEM`, `EWY`, `GRID`, `ICLN`, `IFRA`, `IWF`, `IYR`, `PBW`, `QCLN`, `QQQ`, `REMX`, `SCHH`, `SMH`, `TAN`, `VBK`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (9): `CORN`, `FXI`, `GLD`, `PALL`, `PLTM`, `SLV`, `XES`, `XLC`, `XME`

**Net call:** Redirect the ag trade into what actually confirmed — healthcare re-accelerating ↗ (XLV/VHT/IHI), XLP's promotion to LEADING, and EM-Asia (VNM, EWZ on momentum). Energy's heading flip to ↙ downgrades it from trim-into-strength to reduce; the CORN/WEAT/COPX regime breaks do the same for ags. Trigger: CORN or WEAT re-crossing to LEADING reinstates the ag bid; healthcare majors heading ↙ would break the last intact spine.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `FXI` (2/0), `GLD` (0/2), `HYG` (0/2), `INDA` (0/2), `JNK` (0/2), `SGOV` (0/2), `UNG` (0/0), `XLP` (1/1)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
