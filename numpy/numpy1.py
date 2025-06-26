import numpy as np
import time
array = np.array([1, 2 ,3])
novo_array = array * 10

print(novo_array)


lista = list(range(1, 1000000))
listanp = np.array(range(1, 1000000))


inicio = time.time()
lista_soma = sum(lista)
fim = time.time()
print(f'TEMPO NESCESSARIO lista normal: { fim - inicio }')

inicio = time.time()
lista_soma = np.sum(listanp)
fim = time.time()
print(f'TEMPO NESCESSARIO array np: { fim - inicio }')

