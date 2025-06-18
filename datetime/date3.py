# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime
fmt='%d/%m/%Y'
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt))


agora = datetime.now()

# Formatações comuns
print(agora.strftime("%d/%m/%Y"))           # 17/06/2025
print(agora.strftime("%d-%m-%Y"))           # 17-06-2025
print(agora.strftime("%Y-%m-%d"))           # 2025-06-17
print(agora.strftime("%d de %B de %Y"))     # 17 de June de 2025
print(agora.strftime("%A, %d/%m/%Y"))       # Tuesday, 17/06/2025
print(agora.strftime("%d/%m/%Y %H:%M:%S"))  # 17/06/2025 14:30:45