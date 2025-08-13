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
    options=tickers
)

# Gráfico filtrado
if tickers_selecionados:
    st.line_chart(dados[tickers_selecionados])
else:
    st.warning("Selecione pelo menos uma ação.")


data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider('Selecione o periodo', min_value=data_inicial, max_value=data_final, value=(data_inicial, data_final))

dados = dados.loc[intervalo_data[0]: intervalo_data[1]]


texto_performance = ''

if len(tickers_selecionados) == 0:
    tickers_selecionados = list(dados.columns)

carteira = [1000 for acao in tickers_selecionados]
total_inicial_carteira = sum(carteira)

for ativo in tickers_selecionados:
    performance_ativo = dados[ativo].iloc[-1] / dados[ativo].iloc[0] - 1
    performance_ativo = float(performance_ativo)

    if performance_ativo > 0:
        #  :cor[texto]
        texto_performance = texto_performance + f'  \n{ativo}: :green[{performance_ativo:.1%}]'
    elif performance_ativo < 0:
        texto_performance = texto_performance + f'  \n{ativo}: :red[{performance_ativo:.1%}]'
    else:
        texto_performance = texto_performance + f'  \n{ativo}: {performance_ativo:.1%}'


total_final_carteira = sum(carteira)
performance_carteira = total_final_carteira / total_inicial_carteira - 1

if performance_carteira > 0:
    texto_performance_carteira = f"Performance da carteira com todos os ativos: :green[{performance_carteira:.1%}]"
elif performance_carteira < 0:
    texto_performance_carteira = f"Performance da carteira com todos os ativos: :red[{performance_carteira:.1%}]"
else:
    texto_performance_carteira = f"Performance da carteira com todos os ativos: {performance_carteira:.1%}"


st.write(f"""
### Performance dos Ativos
Essa foi a perfomance de cada ativo no período selecionado:

{texto_performance}

{texto_performance_carteira}
""")

