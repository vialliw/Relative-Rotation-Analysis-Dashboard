# Relative Rotation Analysis Dashboard

<p align="center">
<video src="https://github.com/user-attachments/assets/27def6b3-4c2f-43ef-9d2f-bc21bcec12d4?raw=true" width="800" autoplay loop muted playsinline></video>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#methodology">Methodology</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/status-production-brightgreen.svg" alt="Production Ready">
</p>

---

## Overview

**Relative Rotation Analysis Dashboard** is an open-source, production-grade financial visualization tool that implements the relative rotation methodology for analyzing market sector dynamics. Built with Python, Plotly, and DuckDB, it provides institutional-quality analysis capabilities previously restricted to premium platforms.

### What Makes This Different?

- **Dynamic Scaling Engine:** Automatically optimizes visualization for current market conditions
- **High-Performance Backend:** DuckDB integration enables sub-second query execution
- **Interactive Timeline Control:** Scrub through historical data with animation and slider controls
- **Professional Visualization:** 13-color chromatic spectrum with spline-smoothed trajectories
- **Zero Cost:** Completely free and customizable for personal or commercial use

---

## Features

### Core Functionality

✅ **Quantitative RS-Ratio and RS-Momentum Calculation**
- RS-Ratio (Relative Trend Strength)
- RS-Momentum (Trend Acceleration)
- 100-baseline normalization for consistent interpretation

✅ **Advanced Visualization**
- Smooth vector trajectories using scipy spline interpolation
- Quadrant overlays (Leading, Weakening, Lagging, Improving)
- Real-time velocity calculations
- Synchronized head/trail toggling

✅ **Interactive Controls**
- Play/Pause animation
- Timeline slider for historical analysis
- Individual ticker visibility toggles
- Hover tooltips with precision metrics

✅ **Performance Optimized**
- Weekly data aggregation for noise reduction
- Symmetric axis scaling prevents data compression
- Efficient frame generation (<50ms per frame)

---

## Quick Start

### Prerequisites

```bash
Python 3.8 or higher
pip (Python package manager)
```

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/relative-rotation-dashboard.git
cd relative-rotation-dashboard
```

**2. Create virtual environment (recommended)**
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

### Basic Usage

**1. Prepare your data (one-time setup)**

```python
import yfinance as yf
import duckdb
import pandas as pd

# Download weekly data
tickers = ['SPY', 'XLK', 'XLY', 'XLF', 'XLV', 'XLI', 'XLE', 'XLU', 'XLP', 'XLRE', 'XLB', 'XLC', 'VTV']
data = yf.download(tickers, period='2y', interval='1wk')

# Create DuckDB database
conn = duckdb.connect('market_data.duckdb')

# Flatten multi-index and insert data
df_flat = data['Close'].reset_index().melt(id_vars='Date', var_name='Ticker', value_name='Close')
df_flat['Open'] = df_flat['Close']  # Simplified for weekly data
df_flat['High'] = df_flat['Close']
df_flat['Low'] = df_flat['Close']
df_flat['Volume'] = 0

conn.execute('''
    CREATE TABLE IF NOT EXISTS weekly_close (
        Date DATE,
        Ticker VARCHAR,
        Open DOUBLE,
        High DOUBLE,
        Low DOUBLE,
        "Close" DOUBLE,
        Volume BIGINT,
        PRIMARY KEY(Date, Ticker)
    )
''')

conn.execute('INSERT INTO weekly_close SELECT * FROM df_flat')
conn.close()
```

**2. Run the dashboard**

```bash
python src/plot_rrg_chart.py market_data.duckdb --period 14 --trail 5
```

The dashboard will automatically open in your default browser.

---

## Methodology

The RRG calculation implements a two-factor quantitative model:

### 1. RS-Ratio (X-Axis) - Relative Trend

Measures an asset's performance relative to a benchmark:

```
RS = Price(Asset) / Price(Benchmark)
RS-Ratio = 100 + [ROC(RS, period) × Rolling_Mean(3)] × 100
```

- Values > 100: Outperforming the benchmark
- Values < 100: Underperforming the benchmark

### 2. RS-Momentum (Y-Axis) - Trend Acceleration

Measures the rate of change in relative strength:

```
RS-Momentum = 100 + [ROC(RS-Ratio, period) × Rolling_Mean(3)] × 100
```

- Values > 100: Relative strength is improving
- Values < 100: Relative strength is deteriorating

### Quadrant Interpretation

| Quadrant | RS-Ratio | RS-Momentum | Interpretation | Action |
|----------|----------|-------------|----------------|--------|
| **Leading** | >100 | >100 | Strong outperformance, accelerating | Hold/Buy |
| **Weakening** | >100 | <100 | Still outperforming but losing momentum | Take Profits |
| **Lagging** | <100 | <100 | Underperforming and deteriorating | Avoid/Sell |
| **Improving** | <100 | >100 | Underperforming but gaining momentum | Watch/Accumulate |

### Technical Details

**Dynamic Scaling Algorithm:**
```python
# Ensures 90% chart utilization while maintaining (100,100) center
all_vals = np.concatenate([rs_ratio.values, rs_momentum.values])
max_deviation = max(abs(all_vals.max() - 100), abs(all_vals.min() - 100)) / 0.9
axis_limits = [100 - max_deviation, 100 + max_deviation]
```

**Spline Smoothing:**
```python
# Cubic spline interpolation for smooth trajectories
t = np.linspace(0, 1, len(data_points))
t_new = np.linspace(0, 1, 25)  # 25 interpolated points
smooth_x = make_interp_spline(t, x_values, k=2)(t_new)
smooth_y = make_interp_spline(t, y_values, k=2)(t_new)
```

---

## Usage

### Command Line Options

```bash
python src/plot_rrg_chart.py <database_path> [options]

Required Arguments:
  database_path         Path to DuckDB database file

Optional Arguments:
  --period INT         Lookback period for calculations (default: 14)
  --trail INT          Number of trailing periods to display (default: 5)
  --output PATH        Custom output file path (default: auto-generated)
```

### Examples

**Basic sector analysis:**
```bash
python src/plot_rrg_chart.py market_data.duckdb
```

**Custom parameters:**
```bash
python src/plot_rrg_chart.py market_data.duckdb --period 21 --trail 10
```

**Save to specific location:**
```bash
python src/plot_rrg_chart.py market_data.duckdb --output ~/Desktop/rrg_analysis.html
```

### Customization

**Modify ticker list** (in `plot_rrg_chart.py`):
```python
tickers = ['XLK', 'XLY', 'XLF', 'XLV', 'XLI', 'XLE', 'XLU', 'XLP', 'XLRE', 'XLB', 'XLC', 'VTV', 'IYT']
benchmark = 'SPY'  # Change to QQQ, DIA, etc.
```

**Adjust color palette** (line 18):
```python
colors = [
    '#FF0000', '#FF007F', '#FF7F00', '#FF00FF', '#FFFF00',  # Warm spectrum
    '#7FFF00', '#00FF00', '#00FF7F', '#00FFFF', '#007FFF',  # Cool spectrum
    '#0000FF', '#4B0082', '#8B00FF'                         # Deep spectrum
]
```

**Change animation speed** (line 180):
```python
"frame": {"duration": 100}  # Milliseconds per frame (50-200 recommended)
```

---

## Documentation

### Repository Structure

```
relative-rotation-dashboard/
├── src/
│   └── plot_rrg_chart.py           # Main plotting engine
├── docs/
│   ├── DEVELOPMENT_JOURNEY.md      # AI-assisted development blog
│   ├── methodology.md              # Detailed calculation formulas
│   └── images/                     # Screenshots and diagrams
├── examples/
│   ├── basic_usage.py              # Simple example
│   └── data_preparation.py         # Data pipeline example
├── tests/
│   └── test_calculations.py        # Unit tests (coming soon)
├── requirements.txt                # Python dependencies
├── LICENSE                         # MIT License
└── README.md                       # This file
```

### Additional Resources

- **[Development Journey](docs/DEVELOPMENT_JOURNEY.md):** Complete case study of AI-assisted development process
- **[Methodology Deep Dive](docs/methodology.md):** Mathematical formulas and technical specifications
- **[Contributing Guide](CONTRIBUTING.md):** Guidelines for contributions
- **[Changelog](CHANGELOG.md):** Version history and updates

---

## Performance

### Benchmarks

| Metric | Value |
|--------|-------|
| Data query time | <100ms (2 years weekly) |
| Calculation pipeline | <200ms (13 tickers) |
| Frame generation | ~50ms per frame |
| HTML file size | ~8MB |
| Browser load time | 1-2 seconds |
| Animation FPS | 10 frames/second |

### System Requirements

**Minimum:**
- Python 3.8+
- 2GB RAM
- Modern web browser (Chrome, Firefox, Safari, Edge)

**Recommended:**
- Python 3.10+
- 4GB RAM
- Chrome or Firefox for best performance

---

## Roadmap

### Version 1.1 (Q2 2026)
- [ ] CLI argument parser for dynamic benchmark selection
- [ ] YAML/JSON configuration file support
- [ ] Export to PNG/PDF for reports
- [ ] Alternative color scheme presets

### Version 1.2 (Q3 2026)
- [ ] ATR-based volatility normalization
- [ ] Correlation matrix overlay
- [ ] Quadrant transition alerts
- [ ] Historical pattern matching

### Version 2.0 (Q4 2026)
- [ ] Real-time data streaming integration
- [ ] Multi-asset class support (commodities, forex)
- [ ] Web dashboard (Dash/Streamlit)
- [ ] REST API endpoint

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick Start for Contributors:**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Commit with clear messages: `git commit -m 'Add amazing feature'`
5. Push to your fork: `git push origin feature/amazing-feature`
6. Open a Pull Request

**Areas We Need Help:**
- Unit test coverage
- Alternative RRG calculation methods
- Data source plugins (Alpha Vantage, IEX Cloud)
- Performance optimization
- Documentation improvements

---

## License & Disclaimer

### Software License

**MIT License** - See [LICENSE](LICENSE) file for details.

This software is free for personal and commercial use with attribution.

### Trademark Notice

"RRG" and "Relative Rotation Graphs" are registered trademarks of [RRG Research](https://www.relativerotationgraphs.com/). This project is an independent implementation of relative rotation analysis concepts and is not affiliated with, endorsed by, or sponsored by RRG Research.

### Financial Disclaimer

This software is provided for educational and informational purposes only. It is not financial advice. Always conduct your own research and consult with a qualified financial advisor before making investment decisions. Past performance does not guarantee future results.

---

## Acknowledgments

**Technology Stack:**
- [Plotly](https://plotly.com/) - Interactive visualization
- [DuckDB](https://duckdb.org/) - High-performance analytics database
- [SciPy](https://scipy.org/) - Scientific computing library
- [NumPy](https://numpy.org/) - Numerical computation
- [Pandas](https://pandas.pydata.org/) - Data manipulation

**Inspiration:**
- Julius de Kempenaer - Original RRG® methodology
- StockCharts.com - Educational sector rotation content
- The open-source community

**AI Development Partner:**
This project was developed through iterative collaboration with ChatGPT, Gemini, Claude (Anthropic), showcasing the power of AI-augmented software engineering.

---

## Citation

If you use this software in your research or projects, please cite:

```bibtex
@software{relative_rotation_dashboard,
  author = {Vialli Wong},
  title = {Relative Rotation Analysis Dashboard},
  year = {2026},
  url = {https://github.com/yourusername/relative-rotation-dashboard},
  version = {1.0.0}
}
```

---

## Contact & Support

**Issues:** [GitHub Issues](https://github.com/yourusername/relative-rotation-dashboard/issues)

**Discussions:** [GitHub Discussions](https://github.com/yourusername/relative-rotation-dashboard/discussions)

**Email:** vialliw@yahoo.com

**Star the repo** ⭐ if you find it useful!

---

<p align="center">
  Made with ❤️ using Python and AI collaboration
</p>

<p align="center">
  <a href="#top">Back to Top ↑</a>
</p>
