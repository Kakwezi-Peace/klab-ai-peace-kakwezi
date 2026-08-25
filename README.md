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