def sorteio():
    from random import randint
    from time import sleep
    
    num = []
    print('Sortenado 5 valores da lista:', end=' ')
    for n in range (0, 5):
        s = (randint(0,10))
        print(s, end=' ', flush=True)
        sleep(0.3)
        num.append(s)
    return num

def somapar(lista):
    soma = 0
    for n in lista:
        if (n % 2 == 0):
            soma += n
    return soma

números = (sorteio()) 

print(f'\nSomando os valores pares de {números} temos o resultado de {somapar(números)}!\n')

