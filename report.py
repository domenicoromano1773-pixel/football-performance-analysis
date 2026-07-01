import pandas as pd
df = pd.read_csv('fifa_world_cup_2026_player_performance.csv')
print(df.info())
print(df.head())
print(df.isnull().sum())  
# --- 1. Top 10 marcatori ---
top_scorers = df.groupby('player_name')['goals'].sum().sort_values(ascending=False).head(10)
print("\n=== TOP 10 MARCATORI ===")
print(top_scorers)

# --- 2. Rating medio per posizione ---
rating_by_position = df.groupby('position')['player_rating'].mean().sort_values(ascending=False)
print("\n=== RATING MEDIO PER POSIZIONE ===")
print(rating_by_position)

# --- 3. Squadra con più goal totali ---
goals_by_team = df.groupby('team')['goals'].sum().sort_values(ascending=False)
print("\n=== GOAL TOTALI PER SQUADRA ===")
print(goals_by_team)

# --- 4. Correlazione tra metriche chiave ---
correlazioni = df[['minutes_played', 'goals', 'assists', 'player_rating']].corr()
print("\n=== CORRELAZIONI ===")
print(correlazioni)

# --- 5. Esporta report in Excel con più fogli ---
with pd.ExcelWriter('report_finale.xlsx') as writer:
    top_scorers.to_excel(writer, sheet_name='Top Marcatori')
    rating_by_position.to_excel(writer, sheet_name='Rating per Posizione')
    goals_by_team.to_excel(writer, sheet_name='Goal per Squadra')
    correlazioni.to_excel(writer, sheet_name='Correlazioni')

print("\nReport esportato: report_finale.xlsx")
print(df.isnull().sum())