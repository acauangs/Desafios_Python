
def leiaint(msg):
    while True:
        num = input((msg))
        if num.isnumeric():
            num = num
            print(f'Você digitou o valor {num}')
            break
        else:
            print('ERRO!, Digite um número inteiro valido')


n = leiaint("Digite um número inteiro: ")
