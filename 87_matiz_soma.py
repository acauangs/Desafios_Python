#Programa que recebe uma matriz 3x3, e devolve a matriz junto com a soma dos números pares, a soma dos valores da terceira coluna e o maior valor da segunda linha.

matriz = [[0, 0, 2], [0, 0, 0], [0, 0, 0]]
soma_par = tresS = maior_valor = 0

# input da matriz
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' *30)
#print da matrix, e somar os elementos pares na variavel (soma_par)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print('\n')

print('=-' *30,'\n')

print('\nA soma dos valores pares é:\033[1;33m', soma_par,'\033[m\n' )

#Soma da terceira coluna
for c in range(0,3):
        tresS += matriz[c][2]
print('A soma dos valores da terceira coluna é:\033[1;33m', tresS,'\033[m\n')

#Maior valor da segunda fileira
for n in matriz[1]:
    if n < 0 and maior_valor == 0:
        maior_valor = n
    elif n > maior_valor:
        maior_valor = n
print('O maior valor da segunda linha é :\033[1;33m', maior_valor,'\033[m\n')