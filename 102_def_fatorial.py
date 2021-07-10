

def fatorial(num, show =False):
    """
    program com um funcao fatorial, que recebe um numero como parametro e retorna o fatorial
    Com um parametro opcional se ele receber True mostra a operacao
    """
    print('-=' * 30)
    fat = 1 
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print (f' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat

print(fatorial(5, show=True))
help(fatorial)