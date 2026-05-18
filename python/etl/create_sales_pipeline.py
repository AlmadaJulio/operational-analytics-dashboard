import pandas as pd
import random
from datetime import datetime, timedelta

clientes = [
    "Volvo",
    "Bosch",
    "Siemens",
    "GE Healthcare",
    "Embraer",
    "Toyota",
    "Scania",
    "BMW",
    "Petrobras",
    "John Deere"
]

segmentos = [
    "Automotive",
    "Healthcare",
    "Industrial",
    "Energy",
    "Aerospace"
]

responsaveis = [
    "Carlos Lima",
    "Fernanda Souza",
    "Ricardo Alves",
    "Juliana Martins"
]

etapas = [
    "Prospecção",
    "Apresentação",
    "Proposta",
    "Negociação",
    "Fechamento"
]

status_opcoes = [
    "Aberto",
    "Fechado",
    "Perdido"
]

origens = [
    "LinkedIn",
    "Indicação",
    "Evento",
    "Website",
    "Cold Call"
]

dados = []

for i in range(1, 101):

    data_entrada = datetime(2025, 1, 1) + timedelta(
        days=random.randint(0, 180)
    )

    status = random.choices(
        status_opcoes,
        weights=[50, 35, 15]
    )[0]

    if status == "Fechado":
        etapa = "Fechamento"
    else:
        etapa = random.choice(etapas[:-1])

    data_fechamento = (
        data_entrada + timedelta(days=random.randint(15, 90))
        if status == "Fechado"
        else None
    )

    valor = random.randint(50000, 500000)

    dados.append({
        "LeadID": f"LEAD-{1000+i}",
        "Cliente": random.choice(clientes),
        "Segmento": random.choice(segmentos),
        "Responsavel_Comercial": random.choice(responsaveis),
        "Etapa": etapa,
        "Valor_Proposta": valor,
        "Probabilidade": random.randint(10, 100),
        "Data_Entrada": data_entrada,
        "Data_Fechamento": data_fechamento,
        "Status": status,
        "Origem_Lead": random.choice(origens)
    })

df = pd.DataFrame(dados)

print(df.head())

df.to_csv(
    "datasets/processed/sales_pipeline.csv",
    index=False
)

print("\nSales pipeline criado com sucesso.")