import numpy as np

# Vendas diárias para 2 semanas
vendas = np.array([200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

# Reorganizar os dados em uma matriz de 2x7
vendas_reshaped = np.reshape(vendas, (2, 7))
print(vendas_reshaped.shape)
print(vendas_reshaped)

print(vendas_reshaped.sum(axis=0))
print(vendas_reshaped.sum(axis=1))