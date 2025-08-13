import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def carregar_dados(tickers):
    # Baixa os dados de todos os tickers de uma vez
    dados = yf.download(tickers, start='2015-01-01', end='2025-01-01', group_by='ticker')
    
    # Extrai apenas os preços de fechamento
    precos = pd.DataFrame()
    for ticker in tickers:
        if ticker in dados:
            precos[ticker] = dados[ticker]['Close']
    return precos.dropna()

# Lista de tickers (como lista Python)
tickers = ["ITUB4.SA", "BBAS3.SA", "VALE3.SA", "ABEV3.SA", "PETR4.SA", "GGBR4.SA"]

# Carrega os dados
dados = carregar_dados(tickers)

# Interface do app
st.write("""
# App de preço de Ações  
O gráfico apresenta a evolução do preço das ações brasileiras ao longo dos anos
""")

# Mostra os dados
st.write(dados)

# Exibe o gráfico
st.line_chart(dados)
lista_acoes = st.multiselect("Escolha as ações para exibir no gráfico", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica:'Close'})
grafico = st.line_chart(dados)
