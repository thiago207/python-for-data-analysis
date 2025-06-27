import numpy as np

dados = [127, 90, 201, 150, 210, 220, 115]
vendas = np.array(dados)
#print(np.mean(vendas))


precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])
max = np.max(precos)
min = np.min(precos)
variacao = max - min
#print(max, min, variacao)



quantidades = np.array([5, 3, 2])
precos = np.array([100, 200, 50])

# 5A, 3B, 2C 
# 100, 200, 50
total_vendas = np.dot(quantidades, precos)
print(total_vendas)



