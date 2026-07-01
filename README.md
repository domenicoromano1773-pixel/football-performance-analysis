# Football Performance Analysis

Python script that analyzes player performance data from a football tournament dataset, using pandas for aggregation and statistical analysis.

## What it does

- Loads and inspects a dataset of 54,600 player-match records (75 columns)
- Identifies top scorers, average rating by position, and total goals by team
- Calculates correlations between key performance metrics
- Exports a multi-sheet Excel report with all findings

## Key insight

Player rating correlates much more strongly with minutes played (0.84) than with goals scored (0.22) — meaning consistency on the pitch matters more to overall rating than scoring alone in this dataset.

## Dataset
For downloading the dataset ->
Source: [Kaggle]](https://www.kaggle.com/datasets/rauffauzanrambe/fifa-world-cup-2026-player-performance-dataset))

## Output

Generates `final_Report.xlsx` with 4 sheets: top scorers, rating by position, goals by team, and correlation matrix.
