import numpy as np

# Salários dos funcionários
salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

# Calcular a média salarial
media_salarial = np.mean(salarios)

print(media_salarial)

#salarios acima da media

salarios_acima_media = np.where(salarios > media_salarial)
print(salarios_acima_media) #posicao
print(salarios[salarios_acima_media]) #passando como indice

#print(salarios[salarios > media_salarial]) CONDICOES SIMPLES PODE FAZER DIRETO
#print(salarios[salarios <= 4000])

print(np.where(salarios > media_salarial, '+ACIMA DA MEDIA', '-ABAIXO DA MEDIA'))


print(salarios)
#print(np.where(salarios > media_salarial, salarios, salarios * 1.1))


#indice = np.where((salarios >= 3000) & (salarios <= 4000))
#print(salarios[indice])

salarios_ajustados = np.where((salarios >= 3000) & (salarios <= 4000), salarios * 1.1, salarios)
print(salarios_ajustados)


print(np.where((salarios_ajustados < 3000) | (salarios_ajustados > 4500)))

print(np.where((salarios_ajustados < 3000) | (salarios_ajustados > 4500), salarios * 1.2, salarios_ajustados))