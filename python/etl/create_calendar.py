import pandas as pd

print("Criando dimensão calendário...")

# Criar intervalo de datas
calendar = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    freq="D"
)

# Criar dataframe
df_calendar = pd.DataFrame({
    "Data": calendar
})

# Colunas calendário
df_calendar["Ano"] = df_calendar["Data"].dt.year
df_calendar["Mes"] = df_calendar["Data"].dt.month
df_calendar["Mes_Nome"] = df_calendar["Data"].dt.month_name()
df_calendar["Quarter"] = df_calendar["Data"].dt.quarter
df_calendar["Dia"] = df_calendar["Data"].dt.day
df_calendar["Dia_Semana"] = df_calendar["Data"].dt.day_name()

# Exportar CSV
output_path = "datasets/processed/dim_calendar.csv"

df_calendar.to_csv(output_path, index=False)

print("\nDimensão calendário criada com sucesso.")
print(df_calendar.head())