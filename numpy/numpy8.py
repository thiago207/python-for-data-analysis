import numpy as np
## Exercício

#Você é um engenheiro de produção e tem os tempos de ciclo (em minutos) de uma linha de produção em um array NumPy. Seu trabalho é identificar quaisquer tempos de ciclo que estão -dois desvios padrão acima- (ou) --abaixo da média--. Use o seguinte array para sua análise: `tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])`. 

tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])
desvio_ciclo = np.std(tempos_ciclo * 2)
media_ciclo = np.mean(tempos_ciclo)
print(media_ciclo)
print(desvio_ciclo)



mascara = (tempos_ciclo > media_ciclo + desvio_ciclo) | (tempos_ciclo < media_ciclo - desvio_ciclo)
desvios = np.where(mascara)
print(f"Os tempos de ciclo que estão dois desvios padrão acima ou abaixo da média são: {tempos_ciclo[desvios]}")


#condicao_contraria = np.where((tempos_ciclo < media_ciclo + desvio_ciclo) & (tempos_ciclo > media_ciclo - desvio_ciclo)) #UMA FORMA DE FAZER MAIS DFICIL

condicao_contraria = np.where(~mascara) #RESOLUCAO USANDO NEGACAO DE UMA CONDICAO (UMA RETORNANDO BOOLEANDO)
print(f"Os tempos de ciclo que NAO estão dois desvios padrão acima ou abaixo da média são: {tempos_ciclo[condicao_contraria]}")