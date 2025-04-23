import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# URLs dos arquivos CSV hospedados no GitHub
URL_DIVERSOS = "https://raw.githubusercontent.com/lpalanti/assistentedeeventos/main/diversos.csv"
URL_HOTELARIA = "https://raw.githubusercontent.com/lpalanti/assistentedeeventos/main/hotelaria.csv"
URL_FREELANCERS = "https://raw.githubusercontent.com/lpalanti/assistentedeeventos/main/freelancers.csv"

# Função para carregar os dados e remover as 4 primeiras linhas
@st.cache_data
def carregar_dados():
    diversos = pd.read_csv(URL_DIVERSOS, skiprows=4)
    hotelaria = pd.read_csv(URL_HOTELARIA, skiprows=4)
    freelancers = pd.read_csv(URL_FREELANCERS, skiprows=4)
    return diversos, hotelaria, freelancers

# Configuração do login
config = {
    "credentials": {
        "usernames": {
            "usuario": {
                "name": "Usuário",
                "password": stauth.Hasher(["teste123"]).generate()[0]
            }
        }
    },
    "cookie": {
        "name": "auth_cookie",
        "key": "random_key",
        "expiry_days": 1
    },
    "preauthorized": {}
}

authenticator = stauth.Authenticate(
    config["credentials"], config["cookie"]["name"], config["cookie"]["key"], config["cookie"]["expiry_days"]
)

nome, autenticado, nome_usuario = authenticator.login("Login", location="main")

if autenticado:
    st.sidebar.success(f"Bem-vindo, {nome}!")
    aba = st.sidebar.radio("Escolha uma categoria:", ["Diversos", "Hotelaria", "Freelancers"])
    
    diversos, hotelaria, freelancers = carregar_dados()

    if aba == "Diversos":
        st.header("Tabela: Diversos")
        busca = st.text_input("Buscar", key="busca_diversos").lower()
        if busca:
            filtrado = diversos[diversos.apply(lambda row: row.astype(str).str.lower().str.contains(busca).any(), axis=1)]
        else:
            filtrado = diversos
        st.dataframe(filtrado)

    elif aba == "Hotelaria":
        st.header("Tabela: Hotelaria")
        busca = st.text_input("Buscar", key="busca_hotelaria").lower()
        if busca:
            filtrado = hotelaria[hotelaria.apply(lambda row: row.astype(str).str.lower().str.contains(busca).any(), axis=1)]
        else:
            filtrado = hotelaria
        st.dataframe(filtrado)

    elif aba == "Freelancers":
        st.header("Tabela: Freelancers")
        busca = st.text_input("Buscar", key="busca_freelancers").lower()
        if busca:
            filtrado = freelancers[freelancers.apply(lambda row: row.astype(str).str.lower().str.contains(busca).any(), axis=1)]
        else:
            filtrado = freelancers
        st.dataframe(filtrado)

    authenticator.logout("Sair", location="sidebar")
else:
    st.warning("Por favor, faça login para acessar o conteúdo.")

