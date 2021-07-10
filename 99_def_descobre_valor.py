#PROGRMA QUE RECEBE VARIOS VALORES EM UM FUNÇÃO CHAMADA MAIOR(), DEPOIS DA UM PRINTA OS NÚMERO RECEBIDOS, QUANTIDADE TOTAL DE NÚMEROS E O MAIOR VALOR!
def maior(* n):
    from time import sleep
    
    print('-=' * 30)
    print('Analisando valores...')
    cont = maior = 0
    for v in n:
        print(f'{v}', end=' ', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1 
    
    print(f'Quantidade de valores informados:\033[34m {cont}\033[m')
    print(f'Maior valor informado: \033[32m{maior}\033[m\n')

'''maior(4, 7, 0)         
maior(1, 2, 0)        TESTES
maior(4, 7, 0, 9, 10 , 0)
maior()'''