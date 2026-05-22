import pandas as pd

df = pd.read_csv('datasets/processed/operational_projects_clean.csv')
duplicados = df[df.duplicated(subset=['projectid'], keep=False)]
print(f'Total de duplicados: {len(duplicados)}')
print(duplicados['projectid'].value_counts().head(10))
