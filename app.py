import streamlit as st
import pandas as pd

# URL do seu arquivo .csv no GitHub (use o link "raw")
URL_FREELANCERS = 'https://raw.githubusercontent.com/SEU_USUARIO/NOME_REPO/main/freelancers.csv'
URL_DIVERSOS = 'https://raw.githubusercontent.com/SEU_USUARIO/NOME_REPO/main/diversos.csv'
URL_HOTELARIA = 'https://raw.githubusercontent.com/SEU_USUARIO/NOME_REPO/main/hotelaria.csv'

@st.cache_data
def carregar_dados():
    freelancers = pd.read_csv(URL_FREELANCERS)
    diversos = pd.read_csv(URL_DIVERSOS)
    hotelaria = pd.read_csv(URL_HOTELARIA)
    return freelancers, diversos, hotelaria

freelancers, diversos, hotelaria = carregar_dados()

st.title("Busca de Fornecedores e Hotéis")

aba = st.selectbox("Escolha uma categoria:", ["Freelancers", "Diversos", "Hotelaria"])

if aba == "Freelancers":
    df = freelancers
elif aba == "Diversos":
    df = diversos
else:
    df = hotelaria

busca = st.text_input("Buscar por nome, cidade ou estado:")
if busca:
    df_filtrado = df[df.apply(lambda row: busca.lower() in str(row).lower(), axis=1)]
else:
    df_filtrado = df

st.dataframe(df_filtrado)

