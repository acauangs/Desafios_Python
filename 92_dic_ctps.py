#DICIONARIO QUE RECEBE DADOS DE UMA PESSOA, E SE ELA POSSUI CARTEIRA DE TRABALHO RECEBE MAIS INFORMAÇÕES E DEPOIS MOSTRA TODOS OS DADOS RECEBIDOS
from datetime import datetime
a = datetime.now().year

pessoa = {}

pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Digite o ano de nascimento: '))
pessoa['idade'] = (a - nasc)

carteira = ' '

while carteira not in 'SN':
    carteira = str(input('Possui carteira de trabalho [S/N]')).strip()[0].upper()

while True:
    if carteira == 'N':
        for k, v in pessoa.items():
            print(f'{k} tem o valor: {v}')
        break
    
    else:
        pessoa['ctps'] = int(input('Carteira de trabalho: '))
        pessoa['contribuicao'] = int(input('Anos de contribuição: '))
        pessoa['salario'] = float(input('Valor do sálario: R$'))
        pessoa['falta para se aposentar'] = (50 - pessoa['contribuicao'])
        print('\n')

        for k, v in pessoa.items():
            print (f'{k} tem o valor: {v}')
        break