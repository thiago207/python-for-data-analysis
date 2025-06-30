import pandas as pd


vendas_df = pd.read_csv(r'pandas\Contoso - Vendas - 2017.csv', sep=';')
print(vendas_df[['Numero da Venda', 'Data da Venda', 'ID Produto']])
print(vendas_df['Data da Venda'][0])