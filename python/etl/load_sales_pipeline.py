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