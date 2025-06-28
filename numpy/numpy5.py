import numpy as np

rng = np.random.default_rng()
array_aleatorio = rng.random(4) * 100 
#print(array_aleatorio)


rng = np.random.default_rng(seed=0)
dados_vendas = rng.integers(low=1, high=209.99, size=30)
print(dados_vendas)

vendas_maximas = np.max(dados_vendas)
dia_vendas_maximas = np.argmax(dados_vendas) + 1
print(f"O dia com as vendas mais altas foi o dia {dia_vendas_maximas} com {vendas_maximas} vendas.")

vendas_minimas = np.min(dados_vendas)
dia_vendas_minimas = np.argmin(dados_vendas) + 1
print(f"O dia com as vendas mais baixas foi o dia {dia_vendas_minimas} com {vendas_minimas} vendas.")


# Média de vendas durante o mês
media_vendas = np.mean(dados_vendas)
print(f"A média de vendas durante o mês foi de {media_vendas} vendas por dia.")