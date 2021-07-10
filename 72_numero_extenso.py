from typing import NoReturn


#CRIE UMA TUPLA QUE DEVOLVE UM NÚMERO DIGITADO ESCRITO POR EXTENSO, ENTRE 0 E 20:

num = int(input('Digite um número entre 0 e 20: '))

while num not in range(0,21):
    num = int(input('Numero invalido, Digite um número entre 0 e 20:'))


extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'ouze', 'doze', 'treze',
           'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

print('\nVocê digitou o número\33[1;31m', extenso[num],'\33[m')