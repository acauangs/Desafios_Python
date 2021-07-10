#programa onde é criada apenas 1 lista, com 2 listas internas que separam pares de impares, vai receber uma entrada de 7 digitos inteiros

lista = [[], []]

for c in range(0,7):
    
    num = int(input(f'Digite o valor número {c+1}: ' ))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'\nOs valores pares: {lista[0]}')
print(f'\nOs valores imparés: {lista[1]}')
