import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# ---------------------- AUTENTICAÇÃO ----------------------

# Definindo as credenciais
config = {
    "credentials": {
        "usernames": {
            "admin": {
                "name": "Administrador",
                "password": stauth.Hasher(["teste123"]).generate()[0]
            }
        }
    },
    "cookie": {
        "expiry_days": 1,
        "key": "cookie_key",
        "name": "cookie_name"
    },
    "preauthorized": {
        "emails": []
    }
}

# Inicializando o autenticador
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"]
)

# Login
nome, autenticado, nome_usuario = authenticator.login("Login", location="main")

if not autenticado:
    st.warning("Por favor, faça login para acessar o app.")
    st.stop()

# ---------------------- APP PRINCIPAL ----------------------

st.title("Assistente de Eventos")

@st.cache_data
def carregar_dados():
    url_diversos = "https://github.com/lpalanti/assistentedeeventos/raw/refs/heads/main/diversos.csv"
    url_freelancers = "https://github.com/lpalanti/assistentedeeventos/raw/refs/heads/main/freelancers.csv"
    url_hotelaria = "https://github.com/lpalanti/assistentedeeventos/raw/refs/heads/main/hotelaria.csv"

    diversos = pd.read_csv(url_diversos)
    freelancers = pd.read_csv(url_freelancers)
    hotelaria = pd.read_csv(url_hotelaria)
    return diversos, freelancers, hotelaria

diversos, freelancers, hotelaria = carregar_dados()

aba = st.sidebar.selectbox("Selecione a aba", ["Diversos", "Freelancers", "Hotelaria"])

if aba == "Diversos":
    st.subheader("Base Diversos")
    st.dataframe(diversos)

elif aba == "Freelancers":
    st.subheader("Base Freelancers")
    st.dataframe(freelancers)

elif aba == "Hotelaria":
    st.subheader("Base Hotelaria")
    st.dataframe(hotelaria)
