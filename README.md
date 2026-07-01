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
<img width="701" height="519" alt="Screenshot 2026-07-01 115740" src="https://github.com/user-attachments/assets/48782d2a-38e6-4fe8-a0d1-6b3c8db8d18b" />
<img width="482" height="165" alt="Screenshot 2026-07-01 115803" src="https://github.com/user-attachments/assets/c025ed98-3f58-4f0c-9df6-287a0f40f0e4" />
<img width="881" height="521" alt="Screenshot 2026-07-01 115759" src="https://github.com/user-attachments/assets/1653b188-a8ba-435b-88f0-fade501b7bc2" />
<img width="733" height="523" alt="Screenshot 2026-07-01 115745" src="https://github.com/user-attachments/assets/c2cfc3aa-f26e-41d5-8e17-d177c59939c9" />
