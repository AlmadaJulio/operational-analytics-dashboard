import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect(
    host="db.gwxuophzchihjnjrohse.supabase.co",
    database="postgres",
    user="postgres",
    password="@DAtabase2026",
    port="5432"
)

df = pd.read_csv('datasets/processed/projects_aggregated.csv')

cursor = conn.cursor()
records = [tuple(row) for row in df.itertuples(index=False)]

sql = """
INSERT INTO projects_aggregated 
(projectid, projeto, cliente, bu, pm, horas_orcadas, 
 horas_reais, variancia_horas, perc_desvio, criticidade)
VALUES %s
ON CONFLICT DO NOTHING
"""

execute_values(cursor, sql, records)
conn.commit()
print(f"✓ Linhas inseridas: {cursor.rowcount}")
cursor.close()
conn.close()
