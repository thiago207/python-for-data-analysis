import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def carregar_dados(tickers):
    # Baixa dados
    dados = yf.download(
        tickers,
        start='2015-01-01',
        end='2025-01-01',
        group_by='ticker'
    )

    # Se tiver MultiIndex, extrair apenas "Close"
    if isinstance(dados.columns, pd.MultiIndex):
        precos = dados.xs('Close', axis=1, level=1)
    else:
        precos = dados[['Close']]

    # Renomear colunas para o nome do ticker
    precos.columns = tickers
    return precos.dropna()

# Lista de tickers
tickers = ["ITUB4.SA", "BBAS3.SA", "VALE3.SA", "ABEV3.SA", "PETR4.SA", "GGBR4.SA"]

# Interface
st.title("📈 App de preço de Ações")
st.write("O gráfico apresenta a evolução do preço das ações brasileiras ao longo dos anos.")

# Carregar dados
dados = carregar_dados(tickers)

# Seleção
tickers_selecionados = st.sidebar.multiselect(
    'Selecione as ações',
    options=tickers,
    default=tickers
)

data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider('Selecione o periodo', min_value=data_inicial, max_value=data_final, value=(data_inicial, data_final))

dados = dados.loc[intervalo_data[0]: intervalo_data[1]]

# Gráfico filtrado
if tickers_selecionados:
    st.line_chart(dados[tickers_selecionados])
else:
    st.warning("Selecione pelo menos uma ação.")


