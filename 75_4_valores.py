#DESENVOLVA UM PROGRAMA QUE LEI 4 VALORES DO TECLADO, E GUARDE EM UMA TUPLA. DEPOIS RETORNE QUANTAS VEZES FORAM DIGITADO
# O NUMERO 9,A POSIÇÃO DO NUM 3, QUAIS FORAM OS PARES.

numeros = [int(input('Digite quatro valores:')), int(input('Digite quatro valores:')), int(input('Digite quatro valores:')),
           int(input('Digite quatro valores:'))]


print('Você digitou os valores: ', numeros)

print('O número 9 apareceu: ', numeros.count(9), 'x')

if 3 in numeros:
    print('O número 3 apareceu na posição: ',numeros.index(3)+1)

else:
    print('Não foi digitado o número 3')

print('Os números pares : ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
