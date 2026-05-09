import pandas as pd

print("Iniciando ETL...")

# =========================================
# LEITURA
# =========================================

file_path = "datasets/raw/operational_projects.xlsx"

df = pd.read_excel(file_path)

# =========================================
# LIMPEZA
# =========================================

# Remover espaços nomes colunas
df.columns = df.columns.str.strip()

# =========================================
# FEATURE ENGINEERING
# =========================================

# Variância horas
df["Variancia_Horas"] = (
    df["Horas_Reais"] - df["Horas_Orcadas"]
)

# Percentual utilização
df["Pct_Utilizacao"] = (
    df["Horas_Reais"] / df["Horas_Orcadas"]
) * 100

# Status orçamento
df["Status_Orcamento"] = df["Variancia_Horas"].apply(
    lambda x: "Acima Orcado" if x > 0 else "Dentro Orcado"
)

# Data referência
df["Data_Referencia"] = pd.to_datetime(
    df["Ano"].astype(str)
    + "-"
    + df["Mes"].astype(str)
    + "-01"
)

# Nome mês
df["Mes_Nome"] = df["Data_Referencia"].dt.month_name()

# Quarter
df["Quarter"] = df["Data_Referencia"].dt.quarter

# =========================================
# EXPORTAÇÃO
# =========================================

output_path = (
    "datasets/processed/"
    "operational_projects_clean.csv"
)

df.to_csv(output_path, index=False)

# =========================================
# OUTPUT
# =========================================

print("\nETL finalizado com sucesso.")

print("\nColunas disponíveis:")
print(df.columns)

print("\nPrévia:")
print(df.head())