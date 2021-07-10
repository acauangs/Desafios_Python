#crie uma lista que o usuario possa digitar 5 valores, e cadastre-os em uma lista já na ordem correta (sem usar sort())

lista = []

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    
    if  i == 0 or num > lista[-1]:
        lista.append(num)
        print('Número adicionado ao final da lista...')
    
    else: 
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print (f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print('-= '* 30)
print('Os valores digitados foram:', lista)




