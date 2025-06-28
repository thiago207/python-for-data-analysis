## Exercício

#Você é um gerente de vendas e tem os dados de vendas de três produtos diferentes (Produto A, Produto B, Produto C) para os últimos 5 dias em um array 2D NumPy. Cada linha do array representa um produto e cada coluna representa um dia. Seu trabalho é calcular as vendas totais para cada produto e para cada dia.

#Use o seguinte array para sua análise:

import numpy as np

vendas = np.array([[50, 60, 70, 65, 80],
                   [85, 90, 78, 92, 88],
                   [72, 75, 68, 77, 76]])
total_venda_por_semana = np.sum(vendas, axis=1)

print(f"Vendas totais para o Produto A: {total_venda_por_semana[0]}")
print(f"Vendas totais para o Produto B: {total_venda_por_semana[1]}")
print(f"Vendas totais para o Produto C: {total_venda_por_semana[2]}")
print()
vendas_dia = np.sum(vendas, axis=0)
for i in range(5):
    print(f"Vendas totais para o Dia {i+1}: {vendas_dia[i]}") 