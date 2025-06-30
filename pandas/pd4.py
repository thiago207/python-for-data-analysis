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

frequencia_clientes = vendas_df['E-mail Cliente'].value_counts()

#frequencia_clientes[:5].plot(figsize=(15, 5))
#plt.show()

vendas_total_lojas = vendas_df.groupby('Nome da Loja').sum(numeric_only=True)
vendas_total_lojas = vendas_total_lojas[['Quantidade Vendida']]
print(vendas_total_lojas.sort_values('Quantidade Vendida', ascending=False)[:5])

maior_valor = vendas_total_lojas[['Quantidade Vendida']].max(numeric_only=True)
indice_maior_valor = vendas_total_lojas[['Quantidade Vendida']].idxmax()
print(maior_valor)