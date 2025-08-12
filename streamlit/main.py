import streamlit as st
import pandas as pd
import yfinance  as yf


@st.cache_data
def carregar_empresa(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacao_acao = dados_acao.history(start='2000-01-01', end='2024-07-01')
    cotacao_acao = cotacao_acao['Close']
    return cotacao_acao



dados = carregar_empresa("ITUB4.SA")


# = tamanho do titulo
st.write("""
# App de preço de Ações  
O gráfico apresenta a evolução do preço das ações brasileiras do Itau (ITUB4) ao longo dos anos
""")

st.line_chart(dados)


st.write(dados)