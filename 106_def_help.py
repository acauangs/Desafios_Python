
def Pyhelp():
    from time import sleep
    c = 0
    while True:
        
            print('\033[41m')
            print('-=' * 30)
            print('Bem vindo ao Pyhelp')
            print('-=' * 30)
            print('\033[m')
            
            h = input('--> Função da Biblioteca: ')
            if h.upper() == ' SAIR':
                break
            
            print(f'Acessando o manual do comando {h} ...', flush=True)
            sleep(.30)
            #print(f'\033[46m{help(h)}\033[m')
            print('\033[46m' * 30)
            help(h)
            print('\033[m' )
 
Pyhelp()