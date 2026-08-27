# klab-ai-peace-kakwezi

AI Intensive Bootcamp — kLab Academy, Cohort 2.

## Setup

1. Create virtual environment: `python -m venv .venv`
2. Activate it: `.venv\Scripts\Activate.ps1` (Windows PowerShell)
3. Install dependencies: `pip install -r requirements.txt`

## Structure

- `notebooks/` — exploration and experiments
- `src/` — stable, reusable code
- `data/` — raw and processed datasets
- `reports/` — write-ups and findings


## Assignment 2 — Dataset

- **Name:** World Happiness Report (2015–2022)
- **Source:** Kaggle — https://www.kaggle.com/datasets/mathurinache/world-happiness-report
- **License:** CC0: Public Domain
- **Notes:** Combined across 8 yearly CSV files into a single dataset (1,230 rows) since each year alone is under the 200-row minimum. Column names, formats, and units differed across years and required cleaning , see `notebooks/assignment2_whr.ipynb` for full details.



## Assignment 3: Predict Car Prices (Carvana)

Predicts used car prices using two supervised regression models, comparing a
simple linear approach against an ensemble tree-based approach.

### Dataset
- `data/raw/carvana.csv` — 22,000 real car listings (Name, Year, Miles, Price)
- Source: [Carvana - Predict Car Prices (Kaggle)](https://www.kaggle.com/datasets/ravishah1/carvana-predict-car-prices)

### Steps
1. **Load & explore** — checked shape, nulls, and summary stats
2. **Clean data** — `Year` contained invalid outliers (e.g. `20173`); values outside
   1990–2026 were set to NaN and dropped (2,851 rows removed, 19,149 remained)
3. **Linear Regression** — trained on `Year` + `Miles` to predict `Price`
4. **Random Forest** — trained on the same features for comparison
5. **Evaluation** — compared RMSE and R² on a held-out test set (80/20 split)

### Results

| Metric | Linear Regression | Random Forest |
|---|---|---|
| RMSE | $5,330.28 | $4,331.92 |
| R²   | 0.3071 | 0.5423 |

**Random Forest performed better** on both metrics, since Price doesn't move in
a perfectly straight line with Year/Miles — depreciation and market effects bend
in ways Linear Regression can't capture. Linear Regression remains useful for its
interpretable coefficients (e.g. each extra model year adds ~$684 to price).

### Files
- `notebooks/assignment3_carvana.ipynb` — full analysis
- `reports/a3_chart1.png` — Price vs Miles
- `reports/a3_chart2.png` — Price vs Year