import os
from pathlib import Path

import pandas as pd
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / ".env")

REQUIRED_VARS = ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD", "DB_PORT"]
missing = [v for v in REQUIRED_VARS if not os.getenv(v)]
if missing:
    raise RuntimeError(
        f"Variáveis de ambiente ausentes: {', '.join(missing)}. "
        "Configure o arquivo .env na raiz do projeto (veja .env.example)."
    )

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
    sslmode="require",
)

df = pd.read_csv('datasets/processed/sales_pipeline.csv')
df['data_entrada'] = pd.to_datetime(df['data_entrada']).dt.date
df['data_fechamento'] = pd.to_datetime(df['data_fechamento'], errors='coerce').dt.date
df['data_fechamento'] = df['data_fechamento'].where(pd.notna(df['data_fechamento']), None)

cursor = conn.cursor()
records = [tuple(row) for row in df.itertuples(index=False)]

sql = """
INSERT INTO sales_pipeline 
(leadid, cliente, segmento, responsavel_comercial, etapa, 
 valor_proposta, probabilidade, data_entrada, data_fechamento, 
 status, origem_lead)
VALUES %s
ON CONFLICT DO NOTHING
"""

execute_values(cursor, sql, records)
conn.commit()
print(f"✓ Linhas inseridas: {cursor.rowcount}")
cursor.close()
conn.close()