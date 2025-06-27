import numpy as np
# Guia de Introdução ao NumPy

#NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.



# Preços dos produtos
precos = np.array([20, 25, 30, 35, 40])

# Aumentar os preços em 10 % (ex.: ajuste de inflação)
novos_precos = precos * 1.10
print(novos_precos)




# Vendas do dia
vendas = np.array([200, 220, 250, 210, 300])

# Somar todas as vendas
total_vendas = np.sum(vendas)
print(total_vendas)




# Vendas diárias em uma semana
vendas = np.array([200, 220, 250, 210, 300, 280, 230])

# Calcular a média de vendas
media_vendas = np.mean(vendas)
print(media_vendas)




# Preços dos produtos
precos = np.array([20, 25, 30, 35, 40])

# Encontrar o produto mais caro e mais barato
produto_mais_caro = np.max(precos)
produto_mais_barato = np.min(precos)
print(produto_mais_caro, produto_mais_barato)


# Vendas diárias
vendas = np.array([200, 220, 250, 210, 300])

# Ordenar as vendas
vendas_ordenadas = np.sort(vendas)
print(vendas_ordenadas)



# Número de produtos vendidos
quantidades = np.array([10, 20, 30, 40])

# Preços dos produtos
precos = np.array([5, 10, 15, 20])

# Calcular o valor total de vendas?
print(quantidades * precos)
print(np.sum(quantidades * precos))
total_vendas = np.dot(quantidades, precos)
print(total_vendas)