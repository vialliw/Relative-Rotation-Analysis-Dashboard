# RRA Analysis Report — 2026-10-02

- **Data as-of:** 2026-10-02
- **Benchmark:** SPY | **Lookback:** 12 weeks | **Universe:** 96 tickers
- **Source:** `Relative_Rotation_Dashboard_ETFs_2026-10-02_analysis_prompt.json`
- **Query:** Analyze the RRA data to identify consistent leaders, high-velocity improvers, decaying momentum, and actionable portfolio tilts.
- **Quadrant rules:** lead: Strong RS and momentum - overweight; improving: Building momentum - tactical entry watch; weakening: Fading momentum - reduce exposure; lagging: Weak RS and momentum - avoid

## 1. Quadrant Census

**LEADING: 30** | **IMPROVING: 32** | **WEAKENING: 2** | **LAGGING: 32**

> Weekly read: Balance holds on the surface (30/32/2/32) but the churn turned bearish — six IMPROVING->LAGGING failures and six LEADING->IMPROVING breaks while energy re-accelerates (USO +25.8 into LEADING). The everything-rally is over; this is a rotation-back-to-commodities week.

## 2. Leadership Regime

Consistent leaders (consistency ≥ 75%), ranked by consistency then velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Hdg | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|
| XPH | LEADING | 101.24 | 109.55 | 12.3 | ACCELERATING | SW | 12 | 0 | 100.0 |
| XBI | LEADING | 104.67 | 111.55 | 10.5 | ACCELERATING | SW | 12 | 0 | 100.0 |
| CLOU | LEADING | 122.58 | 111.28 | 8.5 | ACCELERATING | NE | 12 | 0 | 100.0 |
| XSW | LEADING | 114.26 | 114.42 | 1.9 | ACCELERATING | NW | 12 | 0 | 100.0 |
| VHT | LEADING | 105.35 | 117.40 | 4.8 | ACCELERATING | SW | 11 | 1 | 91.7 |
| XLV | LEADING | 105.36 | 118.18 | 4.3 | ACCELERATING | SW | 11 | 1 | 91.7 |
| IBB | LEADING | 112.12 | 124.79 | 6.7 | ACCELERATING | SW | 10 | 0 | 83.3 |

> Read: Same four at 12/12 (CLOU/XBI/XPH/XSW) — but only CLOU heads NE; XPH/XBI/VHT/XLV/IBB are SW (accelerating in speed while sliding left), XSW is NW. Healthcare leadership is still the streak story — and already the distribution story.

## 3. Improving Trends

Top 10 IMPROVING tickers by 1-week velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Hdg | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|
| ITB | IMPROVING | 84.89 | 101.29 | 14.2 | ACCELERATING | SW | 3 | 0 | 25.0 |
| AWAY | IMPROVING | 91.82 | 101.53 | 9.2 | DECELERATING | SW | 9 | 0 | 75.0 |
| XRT | IMPROVING | 90.52 | 100.70 | 8.6 | ACCELERATING | SW | 4 | 0 | 33.3 |
| IYF | IMPROVING | 97.29 | 105.52 | 6.8 | DECELERATING | SW | 10 | 0 | 83.3 |
| PALL | IMPROVING | 95.15 | 139.58 | 6.8 | ACCELERATING | SW | 2 | 5 | 16.7 |
| INDA | IMPROVING | 92.73 | 109.41 | 6.7 | ACCELERATING | SW | 0 | 1 | 0.0 |
| SLV | IMPROVING | 95.39 | 127.79 | 6.6 | DECELERATING | NE | 0 | 9 | 0.0 |
| XLB | IMPROVING | 92.22 | 102.14 | 6.4 | ACCELERATING | SW | 3 | 6 | 25.0 |
| XLF | IMPROVING | 98.69 | 107.35 | 6.4 | ACCELERATING | SW | 10 | 0 | 83.3 |
| VGK | IMPROVING | 96.01 | 103.69 | 5.1 | ACCELERATING | SW | 6 | 4 | 50.0 |

> Read: 32 improvers and only one heading right: SLV +6.6D (NE). The rest of the top-10 — ITB +14.2A, AWAY, XRT, IYF, PALL, INDA, XLB, XLF, VGK — all head SW: fading leaders and failed bounces, not a successor bench. XLF/IYF/IHI are fresh LEADING->IMPROVING breaks; the improving list is now mostly a transit ward.

## 4. Weakening Momentum

WEAKENING quadrant:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Hdg | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|
| CIBR | WEAKENING | 114.94 | 92.63 | 5.3 | ACCELERATING | NE | 8 | 0 | 66.7 |
| XLK | WEAKENING | 101.04 | 81.91 | 1.4 | ACCELERATING | NE | 5 | 4 | 41.7 |

Decelerating LEADING tickers (distribution watch), top 10 by velocity:

| Ticker | Quadrant | RS-Ratio | RS-Mom | Vel 1w | Dir | Hdg | Lead wks | Lag wks | Consist % |
|---|---|---|---|---|---|---|---|---|---|
| CORN | LEADING | 110.55 | 133.32 | 6.6 | DECELERATING | NW | 5 | 7 | 41.7 |
| PLTM | LEADING | 100.60 | 134.99 | 5.7 | DECELERATING | NE | 1 | 6 | 8.3 |
| WEAT | LEADING | 108.33 | 125.20 | 4.8 | DECELERATING | NW | 4 | 4 | 33.3 |
| SOYB | LEADING | 108.81 | 120.71 | 4.0 | DECELERATING | NW | 5 | 6 | 41.7 |
| AMLP | LEADING | 101.89 | 113.65 | 2.7 | DECELERATING | NW | 4 | 3 | 33.3 |
| EWZ | LEADING | 104.68 | 124.19 | 1.9 | DECELERATING | SW | 4 | 7 | 33.3 |
| HERO | LEADING | 107.04 | 126.14 | 1.8 | DECELERATING | NE | 7 | 3 | 58.3 |
| ARKK | LEADING | 110.32 | 112.13 | 1.8 | DECELERATING | NE | 8 | 1 | 66.7 |
| NANR | LEADING | 106.01 | 121.28 | 1.3 | DECELERATING | NW | 6 | 5 | 50.0 |

> Read: Two names, two different stories: CIBR (66.7% consist) heads NE inside WEAKENING — ratio recovering, a possible repair; XLK is a LAGGING->WEAKENING squeeze (NE, Δmom +0.46) — sell the bounce, don't read it as tech's return. On the decel list, ags (CORN/WEAT/SOYB/CANE) cool NW while HERO/ARKK hold NE.

## 5. Velocity Analysis

Fastest movers (top 10 by |velocity_1w|):

| Ticker | Quadrant | Vel 1w | Dir | Hdg | RS-Mom |
|---|---|---|---|---|---|
| USO | LEADING | 25.8 | ACCELERATING | NE | 110.24 |
| COMT | LEADING | 14.4 | ACCELERATING | NE | 117.05 |
| ITB | IMPROVING | 14.2 | ACCELERATING | SW | 101.29 |
| JETS | LAGGING | 13.0 | ACCELERATING | SW | 88.95 |
| DBC | LEADING | 12.7 | ACCELERATING | NE | 117.76 |
| XPH | LEADING | 12.3 | ACCELERATING | SW | 109.55 |
| XBI | LEADING | 10.5 | ACCELERATING | SW | 111.55 |
| AWAY | IMPROVING | 9.2 | DECELERATING | SW | 101.53 |
| FTGC | LEADING | 9.1 | ACCELERATING | NE | 115.62 |
| XOP | LEADING | 9.0 | ACCELERATING | NW | 126.19 |

Dead money (velocity < 1.0): `SMOG` 0.63, `CPER` 0.83, `SGOV` 0.86, `LIT` 0.95

### Quadrant Crossings

- `DBB` LAGGING->IMPROVING — bottoming — early bullish (heading NE, Δratio 0.39, Δmom 1.93)
- `EWC` LEADING->IMPROVING — regime break — bearish shock (heading SW, Δratio -1.66, Δmom -1.80)
- `IAI` IMPROVING->LAGGING — failed improvement — bearish (heading SW, Δratio -2.46, Δmom -3.47)
- `IHI` LEADING->IMPROVING — regime break — bearish shock (heading SW, Δratio -1.46, Δmom -3.86)
- `IWD` LEADING->IMPROVING — regime break — bearish shock (heading SW, Δratio -2.32, Δmom -3.40)
- `IYF` LEADING->IMPROVING — regime break — bearish shock (heading SW, Δratio -3.75, Δmom -5.68)
- `IYR` IMPROVING->LAGGING — failed improvement — bearish (heading SW, Δratio -2.94, Δmom -3.20)
- `JETS` IMPROVING->LAGGING — failed improvement — bearish (heading SW, Δratio -5.72, Δmom -11.64)
- `KRE` IMPROVING->LAGGING — failed improvement — bearish (heading SW, Δratio -4.16, Δmom -7.37)
- `PLTM` IMPROVING->LEADING — rotation confirmed — bullish (heading NE, Δratio 0.63, Δmom 5.61)
- `USO` WEAKENING->LEADING — re-acceleration — bullish (heading NE, Δratio 6.64, Δmom 24.91)
- `VBR` IMPROVING->LAGGING — failed improvement — bearish (heading SW, Δratio -2.81, Δmom -5.06)
- `VTV` LEADING->IMPROVING — regime break — bearish shock (heading SW, Δratio -2.59, Δmom -3.80)
- `XLF` LEADING->IMPROVING — regime break — bearish shock (heading SW, Δratio -3.69, Δmom -5.20)
- `XLI` IMPROVING->LAGGING — failed improvement — bearish (heading SW, Δratio -2.21, Δmom -4.96)
- `XLK` LAGGING->WEAKENING — hard right break — squeeze, don't chase (heading NE, Δratio 1.35, Δmom 0.46)
- `XLY` IMPROVING->LAGGING — failed improvement — bearish (heading SW, Δratio -1.25, Δmom -1.18)

> Read: USO +25.8A is not just another squeeze — it crossed WEAKENING->LEADING on Δmom +24.9, and COMT/DBC/FTGC/XOP confirm the energy re-acceleration as a group. The bearish side is equally clear: JETS (−13.0, SW) plus six failed improvements (IAI/IYR/KRE/VBR/XLI/XLY) and six regime breaks (EWC/IHI/IWD/IYF/VTV/XLF) — the entire cyclical/financial complex is liquidating into the energy bid.

## 6. Structural Laggards

Top 10 LAGGING by lag-weeks:

| Ticker | RS-Ratio | RS-Mom | Vel 1w | Lag wks | Consist % |
|---|---|---|---|---|---|
| BATT | 87.76 | 89.55 | 1.9 | 12 | 0.0 |
| GRID | 91.63 | 90.19 | 1.1 | 12 | 0.0 |
| ICLN | 81.23 | 75.69 | 3.5 | 12 | 0.0 |
| IFRA | 86.75 | 93.11 | 5.0 | 12 | 0.0 |
| LIT | 83.78 | 81.57 | 0.9 | 12 | 0.0 |
| PBW | 73.85 | 63.01 | 2.0 | 12 | 0.0 |
| REMX | 68.82 | 77.22 | 3.8 | 12 | 0.0 |
| SLX | 95.82 | 91.90 | 2.8 | 12 | 0.0 |
| SMOG | 90.08 | 93.61 | 0.6 | 12 | 0.0 |
| TAN | 71.21 | 67.60 | 3.1 | 12 | 0.0 |

> Read: 32 LAGGING and the 12w cohort is unchanged clean energy (IFRA/REMX/ICLN/TAN/SLX/PBW/BATT) plus dead utilities/infra (GRID/SMOG/LIT) — the market's chosen losers keep funding the commodity re-bid.

## 7. Actionable Portfolio Tilts

- **Overweight** (14): `BCD`, `CANE`, `CLOU`, `COMT`, `COPX`, `DBC`, `FCG`, `FTGC`, `IEO`, `USO`, `VDE`, `XLE`, `XOP`, `XSW`
- **Hold-but-trim** — decelerating leaders (2): `CORN`, `PLTM`
- **Reduce** — weakening (2): `CIBR`, `XLK`
- **Avoid** — structural laggards (20): `BATT`, `EEM`, `EWY`, `GRID`, `ICLN`, `IFRA`, `IWF`, `IYR`, `LIT`, `PBW`, `QCLN`, `QQQ`, `REMX`, `SCHH`, `SLX`, `SMOG`, `TAN`, `VBK`, `XES`, `XME`
- **Watch** — improving, RS-mom ≥ 110 but RS-ratio < 100 (6): `FXI`, `GLD`, `IHI`, `PALL`, `SLV`, `XLC`

**Net call:** Follow the confirmation, not the streaks: rotate into the energy/commodity complex (USO/COMT/DBC/FTGC — all NE, now LEADING) and fund it from the SW-heading financial/cyclical improvers. Core hold: CLOU plus the metals watch (SLV/PLTM). Trigger: if USO's heading flips SW next week, this was the last squeeze — revert to metals-only.

## 8. Data Caveats

- `consistency_score` = lead_weeks_3m / lookback (12) — share of the window spent in LEADING. lead+lag < lookback is normal (IMPROVING/WEAKENING weeks are uncounted); it is NOT insufficient history.
- Minimal extreme-quadrant history (lead+lag ≤ 2 — score can't distinguish "new to universe" from "always middling"): `INDA` (0/1)
- `angle_deg` convention is not defined in the prompt; do not infer rotation direction from it alone — use quadrant + `heading` (or, on legacy payloads without a prior file, quadrant + velocity_direction).
- Tilt buckets are rule-generated; review before acting.
