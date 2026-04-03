import streamlit as st
import pandas as pd
import os

# Caminho correto do arquivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "jobs.csv")

df = pd.read_csv(file_path)

st.title("Job Market Insights")

st.markdown("""
Dashboard interativo que analisa vagas de tecnologia,
identificando tendências e habilidades mais demandadas.
""")

# ---------------- SIDEBAR ----------------
st.sidebar.title("Filtros")

filtro_titulo = st.sidebar.text_input("Filtrar por cargo")

filtro_tecnologia = st.sidebar.text_input("Filtrar por tecnologia")

# Aplicando filtros
df_filtrado = df.copy()

if filtro_titulo:
    df_filtrado = df_filtrado[df_filtrado["titulo"].str.lower().str.contains(filtro_titulo.lower(), na=False)]

if filtro_tecnologia:
    df_filtrado = df_filtrado[df_filtrado["descricao"].str.lower().str.contains(filtro_tecnologia.lower(), na=False)]

# ---------------- TECNOLOGIAS ----------------
techs = ["python", "sql", "react", "aws", "excel"]

for tech in techs:
    df_filtrado[tech] = df_filtrado["descricao"].str.lower().str.contains(tech, na=False)

resultado = df_filtrado[techs].sum().sort_values(ascending=False)

# ---------------- MÉTRICAS ----------------
col1, col2 = st.columns(2)

col1.metric("Total de vagas", len(df_filtrado))
col2.metric("Tecnologias analisadas", len(techs))


# ---------------- GRÁFICO ----------------
st.subheader("Tecnologias mais demandadas")
st.bar_chart(resultado)

# ---------------- TABELA ----------------
st.subheader("Vagas coletadas")
st.dataframe(df_filtrado[["titulo", "empresa", "localizacao"]])
