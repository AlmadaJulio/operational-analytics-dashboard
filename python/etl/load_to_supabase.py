import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect(
    host="",
    database="postgres",
    user="postgres",
    password="",
    port="5432"
)

df = pd.read_csv('datasets/processed/operational_projects_clean.csv')
df['data_referencia'] = pd.to_datetime(df['data_referencia']).dt.date

cursor = conn.cursor()

records = [tuple(row) for row in df.itertuples(index=False)]

sql = """
INSERT INTO operational_projects_clean 
(projectid, projeto, cliente, bu, pm, fase, especialidade, 
 ano, mes, horas_orcadas, horas_reais, variancia_horas, 
 status_horas, data_referencia)
VALUES %s
ON CONFLICT DO NOTHING
"""

execute_values(cursor, sql, records)
conn.commit()
print(f"✓ {cursor.rowcount} linhas inseridas")
cursor.close()
conn.close()