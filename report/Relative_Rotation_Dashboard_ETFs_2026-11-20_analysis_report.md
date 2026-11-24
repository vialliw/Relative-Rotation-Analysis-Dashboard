# RRA Analysis Report — 2026-11-20

- **Data as-of:** 2026-11-20
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-11-20_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 35** | **IMPROVING: 18** | **WEAKENING: 9** | **LAGGING: 34**

> Weekly read: Crash-resolution week — LEADING expands 31→35 while WEAKENING doubles to 9 and the improving bench halves to 18.
> Last week's ↙-heading leaders resolved exactly as the headings warned (GDX/ARKK fell out of LEADING, CLOU to LAGGING).
> Two regimes print at once: confirmed defensive rotations in (TLT/XLU/HYG/JNK/UNG/INDA) and a junkyard of broken leaders.
> The inflection is complete — leadership is now defensive.

| RS-Momentum ↓ / RS-Ratio → | **< 100** | **≥ 100** |
|---|---|---|
| **≥ 100** | **IMPROVING (18)**<br>• Energy/commodity: `XES`↙<br>• Metals/hard-asset: `BATT`↙ `DBB`↘ `GDX`↙ `GLD`↙ `LIT`↙ `PLTM`↙ `REMX`↖ `SLV`↙ `SMOG`↖ `XME`↙<br>• Growth/mega-cap tech: `ARKK`↙ `IWF`↙ `XLC`↗<br>• Clean energy: `ICLN`↗<br>• EM/Intl: `EWA`↘ `EWZ`↘ `FXI`↘ | **LEADING (35)**<br>• Energy/commodity: `BCD`↘ `CANE`↙ `COMT`↙ `CORN`↗ `DBC`↘ `FCG`↙ `FTGC`↘ `IEO`↙ `NANR`↙ `SOYB`↗ `UNG`↗ `USO`↘ `VDE`↙ `XLE`↙ `XOP`↙<br>• Healthcare: `IBB`↘ `IHI`↘ `VHT`↘ `XLV`↘<br>• Defensive/rate-sensitive: `HYG`↗ `ITB`↗ `JNK`↗ `SGOV`↗ `TLT`↗ `XLP`↗ `XLU`↗<br>• Value/dividend/consumer: `VOE`↗ `VTV`↗ `XLB`↘ `XLY`↗ `XRT`↗<br>• Growth/mega-cap tech: `HERO`↘<br>• EM/Intl: `EWC`↙ `INDA`↗ `VNM`↗ |
| **< 100** | **LAGGING (34)**<br>• Energy/commodity: `WEAT`↗<br>• Metals/hard-asset: `COPX`↙ `CPER`↙ `PALL`↙ `SLX`↙<br>• Healthcare: `XPH`↗<br>• Financials/REITs: `IAI`↗ `KRE`↗<br>• Growth/mega-cap tech: `AWAY`↙ `CLOU`↙ `DIA`↘ `IWM`↗ `QQQ`↖ `SMH`↖ `VBK`↖ `VOT`↙ `XLK`↙<br>• Clean energy: `PBW`↖ `QCLN`↖ `TAN`↖<br>• EM/Intl: `EEM`↖ `EFA`↘ `EWJ`↙ `EWY`↖ `VGK`↘ `VXUS`↘<br>• Transports/infra/industrials: `GRID`↙ `IFRA`↗ `IYT`↗ `JETS`↗ `XAR`↙ `XLI`↗ `XTN`↗<br>• Other: `AMLP`↘ | **WEAKENING (9)**<br>• Healthcare: `XBI`↖<br>• Value/dividend/consumer: `IWD`↗ `VBR`↗<br>• Financials/REITs: `IYF`↗ `IYR`↗ `SCHH`↗ `XLF`↗<br>• Growth/mega-cap tech: `CIBR`↙ `XSW`↙ |

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| IEO | LEADING | 111.44 | 111.39 | 7.6 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| NANR | LEADING | 102.10 | 111.87 | 7.1 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| CANE | LEADING | 109.93 | 114.94 | 7.0 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| XLE | LEADING | 110.69 | 112.85 | 5.7 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| SOYB | LEADING | 107.05 | 105.81 | 5.7 | ACCELERATING | ↗ | CONFIRMED | 12 | 0 | 100.0 |
| HERO | LEADING | 109.21 | 116.89 | 3.7 | ACCELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| XLV | LEADING | 117.33 | 107.66 | 2.7 | ACCELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| VHT | LEADING | 115.01 | 105.37 | 2.4 | ACCELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| IBB | LEADING | 113.02 | 106.66 | 0.9 | DECELERATING | ↘ | CONFIRMED | 12 | 0 | 100.0 |
| XOP | LEADING | 106.21 | 110.31 | 7.6 | DECELERATING | ↙ | CONFIRMED | 11 | 0 | 91.7 |

> Read: The streak roster reshuffled — IEO/SOYB/XLE reached 12/12 while ARKK and GDX fell out to IMPROVING and XSW broke to WEAKENING. What remains splits in two: hard-asset leaders still on streak but ALL heading ↙ (IEO/NANR/CANE/XLE/XOP decelerating toward LAGGING) versus healthcare holding ↘ (XLV/VHT/IBB — ratio still rising, momentum rolling) and HERO ↘. SOYB +5.7A ↗ is the only leader genuinely moving up-right.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| GDX | IMPROVING | 99.34 | 132.78 | 15.1 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| SLV | IMPROVING | 80.06 | 116.38 | 9.2 | ACCELERATING | ↙ | CONFIRMED | 0 | 2 | 0.0 |
| XME | IMPROVING | 84.68 | 106.25 | 9.1 | ACCELERATING | ↙ | CONFIRMED | 0 | 3 | 0.0 |
| EWZ | IMPROVING | 92.03 | 110.38 | 8.0 | DECELERATING | ↘ | CONFIRMED | 8 | 0 | 66.7 |
| PLTM | IMPROVING | 87.83 | 116.67 | 7.6 | ACCELERATING | ↙ | CONFIRMED | 1 | 0 | 8.3 |
| ARKK | IMPROVING | 97.59 | 112.30 | 7.2 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| XES | IMPROVING | 87.28 | 104.40 | 6.6 | ACCELERATING | ↙ | CONFIRMED | 0 | 5 | 0.0 |
| BATT | IMPROVING | 81.98 | 103.95 | 5.5 | ACCELERATING | ↙ | CONFIRMED | 0 | 7 | 0.0 |
| ICLN | IMPROVING | 89.55 | 105.16 | 5.0 | ACCELERATING | ↗ | PENDING | 0 | 10 | 0.0 |
| GLD | IMPROVING | 94.37 | 115.80 | 5.0 | ACCELERATING | ↙ | CONFIRMED | 0 | 0 | 0.0 |

> Read: This bench is a junkyard of broken leaders — read Heading, not the quadrant. GDX +15.1 ↙ is a LEADING->IMPROVING regime break accelerating toward LAGGING (Δ-4.9/-14.3), not a re-acceleration; ARKK +7.2 ↙ is the same signature (Δ-6.9/-2.1) — a fallen leader, NOT an improver, and ↙-heading bars it from overweight. SLV/XME/PLTM/GLD/XES/BATT are all ↙ too — the metals complex is breaking down together; only ICLN +5.0 heads ↗. No successor regime here — the real rotations are in §5's crossings, not this list.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| SCHH | WEAKENING | 102.30 | 97.91 | 6.5 | ACCELERATING | ↗ | TEMPORARY | 0 | 8 | 0.0 |
| XSW | WEAKENING | 108.61 | 99.41 | 6.3 | ACCELERATING | ↙ | TEMPORARY | 11 | 0 | 91.7 |
| IYR | WEAKENING | 101.61 | 99.18 | 5.7 | ACCELERATING | ↗ | TEMPORARY | 0 | 7 | 0.0 |
| CIBR | WEAKENING | 100.95 | 79.83 | 3.5 | DECELERATING | ↙ | CONFIRMED | 1 | 0 | 8.3 |
| XLF | WEAKENING | 104.11 | 97.24 | 2.5 | ACCELERATING | ↗ | PENDING | 4 | 4 | 33.3 |
| IYF | WEAKENING | 101.40 | 95.62 | 2.4 | ACCELERATING | ↗ | TEMPORARY | 4 | 5 | 33.3 |
| VBR | WEAKENING | 101.82 | 98.83 | 2.1 | ACCELERATING | ↗ | TEMPORARY | 2 | 7 | 16.7 |
| IWD | WEAKENING | 105.57 | 99.18 | 2.0 | ACCELERATING | ↗ | CONFIRMED | 4 | 2 | 33.3 |
| XBI | WEAKENING | 100.91 | 93.72 | 1.1 | DECELERATING | ↖ | CONFIRMED | 5 | 3 | 41.7 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Heading | Persist | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|---|
| XOP | LEADING | 106.21 | 110.31 | 7.6 | DECELERATING | ↙ | CONFIRMED | 11 | 0 | 91.7 |
| IEO | LEADING | 111.44 | 111.39 | 7.6 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| NANR | LEADING | 102.10 | 111.87 | 7.1 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| FCG | LEADING | 102.78 | 112.84 | 7.1 | DECELERATING | ↙ | CONFIRMED | 10 | 0 | 83.3 |
| CANE | LEADING | 109.93 | 114.94 | 7.0 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| VDE | LEADING | 108.93 | 112.13 | 5.8 | DECELERATING | ↙ | CONFIRMED | 11 | 0 | 91.7 |
| XLE | LEADING | 110.69 | 112.85 | 5.7 | DECELERATING | ↙ | CONFIRMED | 12 | 0 | 100.0 |
| VNM | LEADING | 102.54 | 118.88 | 4.6 | DECELERATING | ↗ | PENDING | 2 | 5 | 16.7 |
| ITB | LEADING | 101.63 | 103.92 | 4.5 | DECELERATING | ↗ | TEMPORARY | 2 | 5 | 16.7 |
| CORN | LEADING | 100.73 | 106.24 | 4.0 | DECELERATING | ↗ | TEMPORARY | 9 | 0 | 75.0 |

> Read: XSW is the regime break — a 91.7% leader flipping LEADING->WEAKENING while accelerating ↙ at 6.3, the same signature CLOU printed before it fell to LAGGING (breakdown confirmed this week at Δ-8.1/-7.4). Most of the new weakening cluster is squeezes though — SCHH/IYR/XLF/IYF/VBR/IWD all heading ↗ off the lagging floor (hard-right bounces; trim, don't chase) — while CIBR grinds ↙ and XBI drifts ↖. The decel board is the energy complex finishing its breakdown: XOP/IEO/NANR/FCG/CANE/VDE/XLE all ↙ — last week's trims are now full exits.

## 5. Quadrant Crossings

21 crossings this week: **15 confirmed / 6 provisional** (geometric deadband 1.0 pt past the crossed boundary). By type: 7x IMPROVING->LEADING, 6x IMPROVING->LAGGING, 4x LAGGING->WEAKENING, 2x LEADING->IMPROVING, 1x LEADING->WEAKENING, 1x WEAKENING->LAGGING. No diagonal/discontinuous transitions.

### Counter-clockwise — abrupt reversals

**LEADING->IMPROVING** — potential regime break / RS breakdown warning

- `ARKK` CONFIRMED — ↙, Δratio -6.89, Δmom -2.07 (landed ratio 97.59, 2.41 past boundary); quadrant_persistence TEMPORARY
- `GDX` PROVISIONAL_CROSSING — ↙, Δratio -4.87, Δmom -14.27 (landed ratio 99.34, only 0.66 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**IMPROVING->LAGGING** — failed recovery / bearish continuation

- `COPX` CONFIRMED — ↙, Δratio -5.51, Δmom -10.12 (landed mom 95.43, 4.57 past boundary); quadrant_persistence TEMPORARY
- `PALL` CONFIRMED — ↙, Δratio -0.31, Δmom -5.68 (landed mom 97.34, 2.66 past boundary); quadrant_persistence TEMPORARY
- `EWJ` CONFIRMED — ↙, Δratio -1.33, Δmom -3.14 (landed mom 97.80, 2.20 past boundary); quadrant_persistence TEMPORARY
- `VGK` CONFIRMED — ↘, Δratio +1.28, Δmom -1.12 (landed mom 98.98, 1.02 past boundary); quadrant_persistence TEMPORARY
- `EFA` PROVISIONAL_CROSSING — ↘, Δratio +0.62, Δmom -1.67 (landed mom 99.05, only 0.95 past boundary — whipsaw watch); quadrant_persistence TEMPORARY
- `VXUS` PROVISIONAL_CROSSING — ↘, Δratio +0.05, Δmom -0.85 (landed mom 99.73, only 0.27 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LAGGING->WEAKENING** — possible squeeze / counter-trend rally — not a buy signal

- `SCHH` CONFIRMED — ↗, Δratio +5.25, Δmom +3.75 (landed ratio 102.30, 2.30 past boundary); quadrant_persistence TEMPORARY
- `IYR` CONFIRMED — ↗, Δratio +4.67, Δmom +3.20 (landed ratio 101.61, 1.61 past boundary); quadrant_persistence TEMPORARY
- `IYF` CONFIRMED — ↗, Δratio +2.40, Δmom +0.45 (landed ratio 101.40, 1.40 past boundary); quadrant_persistence TEMPORARY
- `VBR` CONFIRMED — ↗, Δratio +2.01, Δmom +0.78 (landed ratio 101.82, 1.82 past boundary); quadrant_persistence TEMPORARY

### Clockwise — normal rotation

**IMPROVING->LEADING** — possible rotation into leadership — confirm next week

- `UNG` CONFIRMED — ↗, Δratio +11.85, Δmom +5.60 (landed ratio 106.75, 6.75 past boundary); quadrant_persistence TEMPORARY
- `XLU` CONFIRMED — ↗, Δratio +5.59, Δmom +3.79 (landed ratio 104.09, 4.09 past boundary); quadrant_persistence TEMPORARY
- `TLT` CONFIRMED — ↗, Δratio +5.10, Δmom +2.51 (landed ratio 104.44, 4.44 past boundary); quadrant_persistence TEMPORARY
- `ITB` CONFIRMED — ↗, Δratio +3.51, Δmom +2.82 (landed ratio 101.63, 1.63 past boundary); quadrant_persistence TEMPORARY
- `HYG` CONFIRMED — ↗, Δratio +3.95, Δmom +1.14 (landed ratio 102.77, 2.77 past boundary); quadrant_persistence TEMPORARY
- `JNK` CONFIRMED — ↗, Δratio +3.87, Δmom +1.12 (landed ratio 102.60, 2.60 past boundary); quadrant_persistence TEMPORARY
- `CORN` PROVISIONAL_CROSSING — ↗, Δratio +3.83, Δmom +1.29 (landed ratio 100.73, only 0.73 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**LEADING->WEAKENING** — potential distribution / early reversal — watch

- `XSW` PROVISIONAL_CROSSING — ↙, Δratio -4.91, Δmom -3.99 (landed mom 99.41, only 0.59 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

**WEAKENING->LAGGING** — potential bearish continuation — confirm persistence

- `CLOU` PROVISIONAL_CROSSING — ↙, Δratio -8.11, Δmom -7.42 (landed ratio 99.04, only 0.96 past boundary — whipsaw watch); quadrant_persistence TEMPORARY

> Read: two flows at once — a confirmed defensive IMPROVING->LEADING rotation (TLT/XLU/HYG/JNK/UNG/ITB, plus provisional CORN: bonds, utilities, credit, ags, homebuilders — textbook late-cycle money) against a broken-leader junkyard exiting left. ARKK's LEADING->IMPROVING break is CONFIRMED at 2.41 past the line; GDX's is only PROVISIONAL at 0.66 — its ↙ heading is still unambiguous weakness but the crossing itself could whipsaw back next week. The four LAGGING->WEAKENING squeezes (SCHH/IYR/IYF/VBR) are ↗ counter-trend bounces — exits, not entries. Provisional names (GDX/CORN/XSW/CLOU/EFA/VXUS) get their verdict on next week's print: hold past the boundary and the story confirms; flip back and they were whipsaw.

## 6. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Heading | Persist | RS-Mom |
|---|---|---|---|---|---|---|
| GDX | IMPROVING | 15.1 | ACCELERATING | ↙ | TEMPORARY | 132.78 |
| UNG | LEADING | 13.1 | ACCELERATING | ↗ | TEMPORARY | 107.43 |
| COPX | LAGGING | 11.5 | ACCELERATING | ↙ | TEMPORARY | 95.43 |
| CLOU | LAGGING | 11.0 | ACCELERATING | ↙ | TEMPORARY | 89.84 |
| SLV | IMPROVING | 9.2 | ACCELERATING | ↙ | CONFIRMED | 116.38 |
| XME | IMPROVING | 9.1 | ACCELERATING | ↙ | CONFIRMED | 106.25 |
| INDA | LEADING | 8.1 | ACCELERATING | ↗ | PENDING | 109.80 |
| EWZ | IMPROVING | 8.0 | DECELERATING | ↘ | CONFIRMED | 110.38 |
| XOP | LEADING | 7.6 | DECELERATING | ↙ | CONFIRMED | 110.31 |
| PLTM | IMPROVING | 7.6 | ACCELERATING | ↙ | CONFIRMED | 116.67 |

Dead money (velocity < 1.0): `VOT` 0.58, `VXUS` 0.85, `IBB` 0.88, `VBK` 0.92

> Read: The velocity tape is the crash in one column — GDX +15.1 ↙ accelerating is the board's fastest move, a breakdown at speed, with SLV/XME/PLTM behind it and COPX +11.5/CLOU +11.0 accelerating ↙ deeper into LAGGING (breakdowns accelerating, not squeezes — exit liquidity only). The genuine ↗ flows are defensive: UNG +13.1 confirmed into LEADING, INDA +8.1A ↗, and a seven-name IMPROVING->LEADING cluster — TLT/XLU/HYG/JNK/CORN/ITB — bonds, utilities, credit, ags, homebuilders: textbook late-cycle defensive rotation. The four LAGGING->WEAKENING squeezes (SCHH/IYR/IYF/VBR) are exits, not entries; the confirmed ARKK regime break is the sell signal; GDX's break is provisional at 0.66 past the boundary though its ↙ heading is unambiguous.

## 7. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| EEM | 93.15 | 98.18 | 1.3 | 12 | 0.0 |
| EWY | 84.42 | 89.71 | 6.3 | 12 | 0.0 |
| GRID | 87.49 | 96.40 | 1.2 | 12 | 0.0 |
| IFRA | 97.00 | 98.91 | 4.0 | 12 | 0.0 |
| PBW | 74.82 | 91.07 | 5.0 | 12 | 0.0 |
| QCLN | 83.58 | 99.36 | 6.0 | 12 | 0.0 |
| QQQ | 95.51 | 96.91 | 1.9 | 12 | 0.0 |
| SMH | 82.94 | 81.15 | 5.4 | 12 | 0.0 |
| TAN | 82.59 | 98.60 | 5.7 | 12 | 0.0 |
| VBK | 93.33 | 95.45 | 0.9 | 12 | 0.0 |

> Read: 34 LAGGING — and the funding pool is now explicitly cap-weighted growth: QQQ/SMH/VBK all at 12 lag weeks with XLK/IWM/XLI joining the avoid tail, beside the standing clean-energy (PBW/QCLN/TAN), EM-Asia (EEM/EWY), infra/transports (GRID/IFRA/IYT/JETS/XAR/XTN) and financials (KRE/IAI) buckets. Nothing here shows reversal velocity — the defensive bid is funded and still has fuel.

## 8. Actionable Portfolio Tilts

- **Overweight** (23): `BCD`, `CORN`, `DBC`, `FTGC`, `HERO`, `HYG`, `IBB`, `ICLN`, `IHI`, `INDA`, `JNK`, `SGOV`, `SOYB`, `TLT`, `UNG`, `VHT`, `VOE`, `VTV`, `XLB`, `XLP`, `XLU`, `XLV`, `XRT`
- **Hold-but-trim** — decelerating leaders (7): `CANE`, `FCG`, `IEO`, `NANR`, `VDE`, `XLE`, `XOP`
- **Reduce** — weakening (9): `CIBR`, `IWD`, `IYF`, `IYR`, `SCHH`, `VBR`, `XBI`, `XLF`, `XSW`
- **Avoid** — structural laggards (21): `EEM`, `EWY`, `GRID`, `IAI`, `IFRA`, `IWM`, `IYT`, `JETS`, `KRE`, `PBW`, `QCLN`, `QQQ`, `SLX`, `SMH`, `TAN`, `VBK`, `VOT`, `XAR`, `XLI`, `XLK`, `XTN`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (7): `ARKK`, `EWZ`, `GDX`, `GLD`, `PLTM`, `SLV`, `SMOG`

**Net call:** Rotate into the confirmed defensive rotation — TLT, XLU, XLP, HYG/JNK, UNG, SGOV — and exit the ↙-heading energy/ag leadership wholesale (XLE/XOP/IEO/VDE/FCG/CANE/NANR); GDX and ARKK are broken leaders accelerating toward LAGGING — sell any bounce, watch-list only. Core hold: healthcare (XLV/VHT/IBB) on streak, mind the ↘ roll. Trigger: healthcare's ↘ headings flipping ↙, or TLT/XLU failing back out of LEADING — if the defensive rotation loses its bid, the next stop is SGOV/cash.

## 9. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `CIBR` (1/0), `FXI` (2/0), `GLD` (0/0), `HYG` (1/0), `JNK` (1/0), `PLTM` (1/0), `SGOV` (2/0), `SLV` (0/2), `TLT` (1/1), `UNG` (1/0), `XLC` (0/0)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- `crossing_status` = geometric deadband on the actually-crossed axis (ratio for L<->I & W<->L; momentum for L<->W & I<->L; diagonals both) — PROVISIONAL_CROSSING within 1.0 pt of 100, CONFIRMED beyond; whipsaw-verdict needs a second week. `quadrant_persistence` = consecutive weeks occupying the current quadrant (TEMPORARY/PENDING/CONFIRMED) — occupancy duration only, NOT crossing validity; `heading` FLAT reserved for |Δ|<0.05 on both axes (0 occurrences this week).
- Tilt buckets are rule-generated; review before acting.
