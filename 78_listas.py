#Programa que recebe uma lista de 5 digitos por input, e retorna o maior e menor valor e suas respectivas posições

lista = []

for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c+1}: ')))

print('\nA lista digitada foi', lista)
print('\nO menor número da lista digitada foi: \033[031m', min(lista),'\033[mNa posição', lista.index(min(lista))+1)
print('\nO maior número da lista digitada foi: \033[032m', max(lista),'\033[mNa posição', lista.index(max(lista))+1)
