import numpy as np

# Vendas diárias para 2 semanas
vendas = np.array([200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

# Reorganizar os dados em uma matriz de 2x7
vendas_reshaped = np.reshape(vendas, (-1,7))
#print(vendas_reshaped)


rng = np.random.default_rng(seed=42)
vendas = rng.integers(low=20, high=200, size=30, endpoint=True)
vendas_reshaped = np.reshape(vendas, (-1,6))
print(vendas_reshaped)
print(f'O total de vendas por semana: {vendas_reshaped.sum(axis=1)}')
print(f'A media de vendas por semana: {vendas_reshaped.mean(axis=1)}')
print(f'A media de vendas por dia da semana: {vendas_reshaped.mean(axis=0)}')
