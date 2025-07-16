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


vendas_df.to_csv(r'C:\Users\Pichau\Documents\estudos\modulos-python\Novo Vendas 2017.csv', sep=';', encoding='latin1')