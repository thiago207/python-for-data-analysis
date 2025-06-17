# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz


from datetime import datetime
from pytz import timezone

data_str = '2007-07-20 07:32:02'
data_formato = '%Y-%m-%d %H:%M:%S'
data_str1 = datetime.strptime(data_str, data_formato)
#print(data_str1)
data = datetime(2007, 7, 20, 19, 53, 22, tzinfo=timezone('Asia/Tokyo'))
#print(data)

#print(datetime.now(timezone('America/Sao_Paulo')))

data = datetime.now()
print(data.timestamp())
print(data.fromtimestamp(1750196568.99928))