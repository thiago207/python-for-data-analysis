# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo


import calendar

#calendario = calendar.calendar(2025)
#calendario = calendar.month(2025, 6)
a,calendario = calendar.monthrange(2025, 7)

print(calendar.day_name[a])
print(calendar.day_name[calendar.weekday(2025, 7, 20)])
print(calendario)