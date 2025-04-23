import streamlit as st
import pandas as pd

# URLs dos arquivos CSV hospedados no GitHub
URL_DIVERSOS = "https://github.com/lpalanti/assistentedeeventos/raw/refs/heads/main/diversos.csv"
URL_FREELANCERS = "https://github.com/lpalanti/assistentedeeventos/raw/refs/heads/main/freelancers.csv"
URL_HOTELARIA = "https://github.com/lpalanti/assistentedeeventos/raw/refs/heads/main/hotelaria.csv"

@st.cache_data
def carregar_dados():
    diversos = pd.read_csv(URL_DIVERSOS)
    freelancers = pd.read_csv(URL_FREELANCERS)
    hotelaria = pd.read_csv(URL_HOTELARIA)
    return diversos, freelancers, hotelaria

# Carregando os dados
diversos, freelancers, hotelaria = carregar_dados()

st.title("🔎 Banco de Fornecedores")

# Menu lateral para escolher o tipo de busca
tipo_busca = st.sidebar.radio("Escolha o tipo de fornecedor:", ("Diversos", "Freelancers", "Hotelaria"))

# Campo de busca
busca = st.text_input("Digite o nome, cidade ou área de atuação:")

def filtrar(df, busca):
    if busca:
        return df[df.apply(lambda row: row.astype(str).str.contains(busca, case=False).any(), axis=1)]
    return df

# Exibir os resultados de acordo com a escolha
if tipo_busca == "Diversos":
    st.subheader("📦 Diversos")
    st.dataframe(filtrar(diversos, busca))
elif tipo_busca == "Freelancers":
    st.subheader("🧑‍💼 Freelancers")
    st.dataframe(filtrar(freelancers, busca))
else:
    st.subheader("🏨 Hotelaria")
    st.dataframe(filtrar(hotelaria, busca))
