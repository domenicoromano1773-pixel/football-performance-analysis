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

Generates `final_report.xlsx` with 4 sheets: top scorers, rating by position, goals by team, and correlation matrix.

### Top Goalscorers

| Player | Goals |
|---|---|
| Memphis Zerrouki | 24 |
| Kasey Hector | 16 |
| Eric Rodriguez | 15 |
| Vinicius Nunes | 15 |
| Mohannad Majeed | 15 |
| Dominik Kramaric | 15 |
| Eric Mba | 14 |
| Randal Duarte | 14 |
| Saleh Al-Qahtani | 13 |
| Andre Bassogog | 13 |

### Rating by Position

| Position | Avg. Rating |
|---|---|
| Forward | 3.88 |
| Midfielder | 3.86 |
| Defender | 3.79 |
| Goalkeeper | 2.07 |

### Goals by Team (Top 10)

| Team | Goals |
|---|---|
| Qatar | 95 |
| Netherlands | 94 |
| Panama | 90 |
| Cameroon | 88 |
| Saudi Arabia | 82 |
| Jamaica | 79 |
| Tunisia | 78 |
| Costa Rica | 76 |
| Ghana | 75 |
| Iran | 72 |

### Correlation Matrix

| | minutes_played | goals | assists | player_rating |
|---|---|---|---|---|
| minutes_played | 1.00 | 0.22 | 0.22 | 0.84 |
| goals | 0.22 | 1.00 | 0.09 | 0.22 |
| assists | 0.22 | 0.09 | 1.00 | 0.20 |
| player_rating | 0.84 | 0.22 | 0.20 | 1.00 |
