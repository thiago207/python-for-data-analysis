import numpy as np
## Exercício

#Você é um analista de RH e tem os salários de todos os funcionários da sua empresa em um array NumPy. Seu trabalho é identificar quantos funcionários ganham acima da média. Use o seguinte array para sua análise: `salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])`.


salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])
media_salarial = np.mean(salarios)
salarios_acima_da_media = np.where(salarios > media_salarial) # FORMA DE SABER QUAIS SAO.

funcionarios_acima_media = (np.sum(salarios > media_salarial)) # OBJETIVO DO EXERCICIO. 
print(f'TOTAL DE FUNCIONNARIOS COM MEDIA SALARIA MAIOR QUE A MEDIA: {funcionarios_acima_media}')


