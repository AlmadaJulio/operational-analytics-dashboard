import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / ".env")

#print("HOST:", os.getenv("DB_HOST"))
#print("USER:", os.getenv("DB_USER"))
#print("PASS:", os.getenv("DB_PASSWORD"))

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
    sslmode="require"
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

try:
    execute_values(cursor, sql, records)
    conn.commit()
    print("Linhas inseridas:", cursor.rowcount)
except Exception as e:
    conn.rollback()
    print("Erro:", e)
finally:
    cursor.close()
    conn.close()
