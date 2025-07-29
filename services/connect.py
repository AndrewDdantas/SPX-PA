from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from .config import json_key
import gspread
import pandas as pd

Scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

backup_path = "dados_cache.csv"


# Função cacheada de carregamento
@st.cache_data(ttl=300)  # cache por 5 minutos
def carregar_dados():
    cred = ServiceAccountCredentials.from_json_keyfile_dict(
        json_key, scopes=Scopes)
    gc = gspread.authorize(cred)
    planilha = gc.open("PROGRAMAÇÃO FROTA - Belem - LPA-02")
    aba = planilha.worksheet("Programação")
    dados = aba.get_all_values()[2:]
    df = pd.DataFrame(dados[1:], columns=dados[0])
    df.to_csv(backup_path, index=False)
    return df
