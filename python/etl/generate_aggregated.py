import pandas as pd

df = pd.read_csv(r'C:\Users\Julio Almada\Documents\DATA_ANALYTICS\datasets\processed\operational_projects_clean.csv')

df_proj = df.groupby(['ProjectID', 'Projeto', 'Cliente', 'BU', 'PM']).agg(
    Horas_Orcadas=('Horas_Orcadas', 'sum'),
    Horas_Reais=('Horas_Reais', 'sum'),
    Variancia_Horas=('Variancia_Horas', 'sum')
).reset_index()

df_proj['Perc_Desvio'] = (df_proj['Variancia_Horas'] / df_proj['Horas_Orcadas'] * 100).round(1)

df_proj['Criticidade'] = df_proj['Perc_Desvio'].apply(
    lambda x: 'Crítico' if x < -15 else ('Atenção' if x < 0 else 'Normal')
)

df_proj.to_csv(
    r'C:\Users\Julio Almada\Documents\DATA_ANALYTICS\datasets\processed\projects_aggregated.csv',
    index=False
)

print(f"✅ projects_aggregated gerado — {len(df_proj)} projetos")
print(df_proj[['ProjectID', 'Horas_Orcadas', 'Horas_Reais', 'Criticidade']].head())