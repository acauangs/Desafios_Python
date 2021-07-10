#Programa que receba números para uma lista, valores repetidos não devem ser aceitos, devolva a lista em ordem crescente

lista = []

while True:
    num = int(input('Digite um valor para ser adicionado na lista: '))
    if num not in lista:
        lista.append(num)
    else: 
        print('Valor duplicado!')

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar[S,N]').strip()[0].upper()
       
    if continuar == 'N':
        break


print(sorted(lista))
    
    