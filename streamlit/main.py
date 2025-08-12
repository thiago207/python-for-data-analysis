import streamlit as st
import pandas as pd
import yfinance  as yf


@st.cache_data
def carregar_dados(empresas):
    dados_acao = yf.Tickers(empresas)
    precos_acao = dados_acao.history(start='2015-01-01', end='2025-01-01')
    precos_acao = precos_acao["Close"]
    return precos_acao

dados  = carregar_dados("ITUB4.SA BBAS3.SA VALE3.SA ABEV3.SA PETR4.SA GGBR4.SA")


st.write(dados)
st.line_chart(dados)
# = tamanho do titulo
st.write("""
# App de preço de Ações  
O gráfico apresenta a evolução do preço das ações brasileiras ao longo dos anos
""")

lista_acoes = st.multiselect("Escolha as ações para exibir no gráfico", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename
grafico = st.line_chart(dados)
