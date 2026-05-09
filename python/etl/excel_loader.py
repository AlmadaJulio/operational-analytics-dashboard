import pandas as pd

print("Python funcionando")

df = pd.DataFrame({
    "Projeto": ["Projeto A", "Projeto B", "Projeto C"],
    "Horas": [120, 85, 210],
    "Status": ["Concluído", "Em andamento", "Planejado"]
})

print(df)