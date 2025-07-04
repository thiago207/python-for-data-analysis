import pandas as pd

tabela = pd.read_excel(r'pandas\Produtos.xlsx')





tabela.loc[tabela['Tipo'] == 'Serviço' , 'Multiplicador Imposto'] = 1.5

tabela['Preço Base Reais'] = tabela['Multiplicador Imposto'] * tabela['Preço Base Reais'] 

print(tabela)

#tabela.to_excel('Produtos2.xlsx', index=False)