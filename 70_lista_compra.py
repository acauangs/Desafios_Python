#PROGRAMA QUE RECEBE UMA LISTA DE COMPRA, E RETORNA O TOTAL GASTO, QUANTIDADE DE ITENS QUE CUSTAM MAIS DE MIL REAIS, E O NOME DO PRODUTO MAIS BARATO
# PROGRAMA SERÁ ENCERRADO POR ESCOLHA DO USUARIO. 

from typing import Counter

total_gasto = mais_de_mil = menor = cont = 0
mais_barato = ' '

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Preço:R$ '))
    total_gasto += preco
    
    if preco > 1000:
            mais_de_mil += 1
    cont +=1 

    if cont == 1 or preco < menor :
        menor = preco
        barato = produto

    continuar = ' '
    while continuar not in 'SN':
            continuar = str(input('Deseja continuar [S,N]')).strip()[0].upper()
    if continuar == 'N':
        break
    
print ('\nO total gasto foi: R$',total_gasto,'\n')
print ('quantidade de produtos que custam mais de mil reais:',mais_de_mil,'\n')
print ('Produto mais barato custa: R$',menor,'produto:',barato,'\n')