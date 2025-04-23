import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

# --- AUTENTICAÇÃO ---
usuarios = {
    "usernames": {
        "admin": {
            "name": "Administrador",
            "password": "$2b$12$prnWjZ0bOhaXjNm6sPZReu5aD3Xj0P0dVYbYPO3LZL99kMfDEvD4a"
        },
        "joao": {
            "name": "João da Inovents",
            "password": "$2b$12$XyNRWgTOBFY2ZONHIfHR4Of7tZ0Uzw0b1FVPi7iGQMF0v7Q8nV74C"
        }
    }
}

authenticator = stauth.Authenticate(
    usuarios,
    "meu_app_login",  # Nome do cookie
    "chave_secreta_super_segura",  # Chave secreta
    cookie_expiry_days=1
)

nome, autenticado, nome_usuario = authenticator.login("Login", "main")

if not autenticado:
    st.warning("Por favor, faça login para acessar o app.")
    st.stop()

authenticator.logout("Logout", "sidebar")
st.sidebar.success(f"Logado como: {nome}")

# --- URLS DOS ARQUIVOS CSV NO GITHUB ---
URL_DIVERSOS = "https://raw.githubusercontent.com/lpalanti/assistentedeeventos/main/diversos.csv"
URL_FREELANCERS = "https://raw.githubusercontent.com/lpalanti/assistentedeeventos/main/freelancers.csv"
URL_HOTELARIA = "https://raw.githubusercontent.com/lpalanti/assistentedeeventos/main/hotelaria.csv"

# --- FUNÇÃO PARA CARREGAR DADOS ---
@st.cache_data
def carregar_dados():
    diversos = pd.read_csv(URL_DIVERSOS)
    freelancers = pd.read_csv(URL_FREELANCERS)
    hotelaria = pd.read_csv(URL_HOTELARIA)
    return diversos, freelancers, hotelaria

diversos, freelancers, hotelaria = carregar_dados()

# --- EXEMPLO DE VISUALIZAÇÃO DOS DADOS ---
st.title("Assistente de Eventos")
st.subheader("Acesso aos dados")

aba = st.selectbox("Escolha a aba:", ["Diversos", "Freelancers", "Hotelaria"])

if aba == "Diversos":
    st.dataframe(diversos)
elif aba == "Freelancers":
    st.dataframe(freelancers)
elif aba == "Hotelaria":
    st.dataframe(hotelaria)
