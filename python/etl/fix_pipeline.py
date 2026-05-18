import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Julio Almada\Documents\DATA_ANALYTICS\datasets\processed\sales_pipeline.csv')

print("ANTES:")
print(df['Etapa'].value_counts().sort_values(ascending=False))

etapas = ['Prospecção', 'Apresentação', 'Proposta', 'Negociação', 'Fechamento']
pesos  = [35, 25, 20, 12, 8]

np.random.seed(42)
df['Etapa'] = np.random.choice(etapas, size=len(df), p=[p/100 for p in pesos])

prob_map = {
    'Prospecção':   (5,  15),
    'Apresentação': (15, 30),
    'Proposta':     (30, 50),
    'Negociação':   (50, 75),
    'Fechamento':   (75, 100)
}

df['Probabilidade'] = df['Etapa'].apply(
    lambda e: np.random.randint(*prob_map[e])
)

df.to_csv(r'C:\Users\Julio Almada\Documents\DATA_ANALYTICS\datasets\processed\sales_pipeline.csv', index=False)

print("\nDEPOIS:")
print(df['Etapa'].value_counts().sort_values(ascending=False))
print("\n✅ Arquivo salvo.")