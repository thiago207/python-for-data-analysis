## Exercício

#Você é um analista de dados em uma empresa e conduziu uma pesquisa de satisfação do cliente durante uma semana. Você perguntou as clientes para classificar seu nível de satisfação com o serviço ao cliente em uma escala de 0 a 10. Você coletou respostas de 30 clientes por dia durante 7 dias, resultando em um total de 210 respostas.

#No entanto, os dados que você recebeu estão em um array 1D de 210 elementos. Reorganize os dados de forma a ter as respostas por dia e faça uma análise descritiva básica, calculando a média geral de satisfação e a média diária.

import numpy as np

# considere os seguintes dados aleatórios como início
rng = np.random.default_rng(seed=42)
respostas = rng.integers(low=0, high=10, size=210, endpoint=True)
#print(respostas)



respostas_reshape = np.reshape(respostas, (7,30))
#print(respostas_reshape)

media_geral = np.mean(respostas)
#print(media_geral)
satisfacao_diaria = respostas_reshape.mean(axis=1)
#print(satisfacao_diaria)
for i in range(7):
    print(f'DIA {i+1} SATISFAÇAO: {satisfacao_diaria[i]:.2f}')
print('MEDIA GERAL:', media_geral)