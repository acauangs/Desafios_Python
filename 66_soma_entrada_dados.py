#crie um programa que leia vários números inteiros, o programa só vai parar quando o usuario digitar '999'. No final mostre quantos  números foram digitados, e a soma deles.

num = quantidade_numeros = soma  = 0

while num != 999:
    try:
        num = int(input('Digite um valor (ou 999 para parar): '))
        if num == 999 and quantidade_numeros == 0:
            print('Nenhum número a ser somado')
        elif num == 999:
            break
        else:
            soma = soma + num
            quantidade_numeros += 1
    except:
        print ('Valor invalido, Digite apenas um número inteiro ou (999)!')
print('A soma dos',quantidade_numeros,'valores foi:', soma,'!')

    
      


