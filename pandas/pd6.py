import pandas as pd




vendas_df = pd.read_csv(r'pandas\Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'pandas\Contoso - Cadastro Produtos.csv', sep=';', encoding='latin1')
lojas_df = pd.read_csv(f'pandas\Contoso - Lojas.csv', sep=';', encoding='latin1')
clientes_df = pd.read_csv(f'pandas\Contoso - Clientes.csv', sep=';', encoding='latin1')

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja','Nome da Loja']]

vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')

vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail Cliente'})
print(vendas_df)

#id_loja = vendas_df['ID Loja'] == 86
#devolvida = vendas_df['Quantidade Devolvida'] != 0
#loja_austin = vendas_df[id_loja & devolvida]
#print(loja_austin)

vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y')
vendas_df['Ano da Venda'] = vendas_df['Data da Venda'].dt.year
vendas_df['Mes da Venda'] = vendas_df['Data da Venda'].dt.month
vendas_df['Dia da Venda'] = vendas_df['Data da Venda'].dt.day
print(vendas_df.info())
print()
print(vendas_df)