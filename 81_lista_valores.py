#programa que recebe uma lista até o usuario decidir parar, e retorna a quantidade de valores na lista, a ordem decresente, e se a lista possui o numero 5;
lista = []

while True: 
    lista.append(int(input('Digite um valor: ')))
    
    continuar =' '
    while continuar not in 'SN':
            continuar = input('Deseja continuar[S/N]:').strip()[0].upper()
        
    if continuar == 'N':
        break

print('\nA lista digitada foi:', lista)

print('\nA lista possui', len(lista),'Valores')

lista.sort(reverse=True)
print('\nA ordem decresente da lista é:', lista)

if 5 in lista:
    print(f'\nTem o numero 5 na lista')
else:
    print('\nA lista não possui o número 5')


