import pandas as pd



vendas_df = pd.read_csv(r'pandas\Contoso - Vendas - 2017.csv', sep=';')

print(vendas_df.info())

produtos_quantidade = vendas_df[['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']]
print(produtos_quantidade)