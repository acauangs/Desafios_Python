#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CONTADOR(), QUE RECEBE TRÊS PARAMETROS E REALIZA A CONTAGEM EM SEQUENCIA USANDO O PASSO DO TERCEIRO PARAMETRO. 
from time import sleep

def contador(i, f, p):
    print('-=' * 30)
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    print(f'Sua contagem de {i} até {f} de {p} em {p}:')
    
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.2)
            cont += p
        print('FIM!')
               
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.2)
            cont -= p
        print('FIM!')
            
        
contador(1, 10, 1) 
contador(10, 0 ,2) 
print('=-' * 30, '\n' 'Contagem personalizada!!' )

inicio = int(input('início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: ')) 

contador(inicio, fim, passo)
