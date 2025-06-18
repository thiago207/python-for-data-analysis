# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

data_emprestimo = datetime(2020, 12, 20)
cinco_anos = relativedelta(years=5)
data_final = data_emprestimo + cinco_anos

lista_parcelas = []
data_parcela = data_emprestimo


while data_parcela < data_final:
    lista_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)



valor_parcelas = 1000000 / len(lista_parcelas) 

for v,c in enumerate(lista_parcelas):
    print(f'{c.strftime('%d/%m/%Y')} - {v+1} PARCELA R$: {valor_parcelas:,.2f}')

print()
print(
    f'Voce pegou 1.000.000 para pagar\n'
    f'em {cinco_anos.years} anos\n'
    f'Numero de parcelas: ({len(lista_parcelas)})\n'
    f'No valor de R$: {valor_parcelas:,.2f}\n'
    )

    

    
