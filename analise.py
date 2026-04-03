import pandas as pd

df = pd.read_csv("data/jobs.csv")

techs = ["python", "sql", "react", "aws", "excel"]

for tech in techs:
    df[tech] = df["descricao"].str.lower().str.contains(tech, na=False)

resultado = df[techs].sum().sort_values(ascending=False)

print("\nTecnologias mais pedidas:\n")
print(resultado)