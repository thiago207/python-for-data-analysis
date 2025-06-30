import pandas as pd



vendas_df = pd.read_csv(r'pandas\Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'pandas\Contoso - Cadastro Produtos.csv', sep=';', encoding='latin1')
lojas_df = pd.read_csv(f'pandas\Contoso - Lojas.csv', sep=';', encoding='latin1')
clientes_df = pd.read_csv(f'pandas\Contoso - Clientes.csv', sep=';', encoding='latin1')


# clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9','Unnamed: 10'], axis=1) RETIRA AS COLUNAS


clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja','Nome da Loja']]


vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail Cliente'})
#print(produtos_df)
#print(lojas_df)
#print(clientes_df)

print(vendas_df.info())


