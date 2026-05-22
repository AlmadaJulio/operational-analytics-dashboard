import pandas as pd
import os

pasta = 'datasets/processed'

for arquivo in os.listdir(pasta):
    if arquivo.endswith('.csv'):
        caminho = os.path.join(pasta, arquivo)
        df = pd.read_csv(caminho)
        df.columns = df.columns.str.lower().str.strip()
        df.to_csv(caminho, index=False)
        print(f'✓ {arquivo} — colunas: {list(df.columns)}')