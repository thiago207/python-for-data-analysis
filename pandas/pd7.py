import pandas as pd

novos_produtos_df = pd.read_csv(r'pandas\Contoso - Cadastro Produtos.csv', sep=';', encoding='latin1')
#print(novos_produtos_df.head(5))
novos_produtos_df.set_index('Nome do Produto', inplace=True)
#print(novos_produtos_df.loc['Contoso Education Essentials Bundle M300 White', 'Preco Unitario'])
#print(novos_produtos_df.iloc[99, 5])
print(novos_produtos_df)

novos_produtos_df.loc['Contoso Wireless Laser Mouse E50 Grey', 'Preco Unitario'] = 23
print(novos_produtos_df.head(5))