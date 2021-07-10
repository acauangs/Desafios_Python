#programa recebe uma lista em forma de equação e baseado na quantidade de parenteses diz se é valida ou nao

equação = str(input('Digite uma operação matematica entre parentesses: '))
pilha = []

for i in equação:
    if i == '(':
        pilha.append('(')
        
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\n\033[1;32mEquação valida!\033[m')
else: 
     print('\n\033[1;31mEquação invalida\033[m')