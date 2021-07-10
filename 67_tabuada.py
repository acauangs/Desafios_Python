#Faça um programa que retorne a taubata de um número escolhido pelo o usuario, o programa sera encerrado com a entrada de qualquer numero negativo ou zero.

entrada = 1

while entrada > 0:
    entrada = int(input('Gostaria de ver a tabuada de qual valor: '))
    
    if entrada <= 0:
        print ('Programa Encerrado, Volte Sempre!')
        break 
    else:
        count = 1
    while count <= 10:
        print(f'{entrada} x {count} = {entrada * count}\n')
        count += 1


