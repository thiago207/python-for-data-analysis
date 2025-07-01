import pandas as pd
import matplotlib.pyplot as plt



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

quantidade_vendida = vendas_df['Quantidade Vendida'].sum()
quantidade_devolvida = vendas_df['Quantidade Devolvida'].sum()

#print('{:.2%}'.format(quantidade_devolvida / quantidade_vendida))

vendas_lojacontoso = vendas_df[vendas_df['ID Loja'] == 306]
quantidade_vendida = vendas_lojacontoso['Quantidade Vendida'].sum()
quantidade_devolvida = vendas_lojacontoso['Quantidade Devolvida'].sum()
print('{:.2%}'.format(quantidade_devolvida / quantidade_vendida))


#loja_306 = vendas_df['ID Loja'] == 306
#vendas_lojacontoso = vendas_df[loja_306]
#print(vendas_lojacontoso)


loja_306 = vendas_df['ID Loja'] == 306  
devolucao_0 = vendas_df['Quantidade Devolvida'] == 0
#vendas_lojacontoso_0_devolucao = vendas_df[(vendas_df['ID Loja'] == 306)  & (vendas_df['Quantidade Devolvida'] == 0)]
vendas_lojacontoso_0_devolucao =  vendas_df[loja_306 & devolucao_0]
print(vendas_lojacontoso_0_devolucao)