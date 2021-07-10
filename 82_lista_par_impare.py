#CRIE UMA ENTRADA DE DADOS QUE RECEBA UMA LISTA, E DEPOIS SEPARE EM OUTRAS DUAS LISTA NUMEROS PARES DOS IMPARES E RETORNE AS LISTA EM UM PRINT.

lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite uma valor para sua lista: '))
    lista.append(num)

    continuar = ' '
    
    while continuar not in 'NS':
        continuar = input('Deseja continuar[S/N]?').strip()[0].upper()
    
    if continuar == 'N':
        print('\033[1;31m[Encerrando...]\033[m')
        break

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print('\nA lista digitada foi: ', lista)
print('\nLista com números pares: ', lista_par)
print('\nLista com números ímpares: ', lista_impar,'\n')


