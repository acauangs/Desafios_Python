#Crie um programa que simule um caixa eletronico, no inicio pergunte qual o valor do saque, o programa informará qual a quantidade e valor de cudulas que será disponibilizada.

print('=======\033[;33mBANCO VC\033[m========')

nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = nota1 = 0


saque = int(input('Qual o valor do saque?'))

if saque > 100:
    nota100 = saque // 100
    saque = saque % 100

if saque > 50:
    nota50 = saque // 50
    saque = saque % 50

if saque > 20:
    nota20 = saque // 20
    saque = saque % 20

if saque > 10:
    nota10 = saque // 10
    saque = saque % 10

if saque > 5:
    nota5 = saque // 5
    saque = saque % 5

if saque > 2:
    nota2 = saque // 2
    saque = saque % 2

if saque > 1:
    nota1 = saque // 1
    saque = saque % 1



print('Total de',nota100,'de cédulas de R$ 100')
print('Total de',nota50,'de cédulas de R$ 50')
print('Total de',nota20,'de cédulas de R$ 20')
print('Total de',nota10,'de cédulas de R$ 10')
print('Total de',nota5,'de cédulas de R$ 5')
print('Total de',nota2,'de cédulas de R$ 2')
print('Total de',nota1,'de cédulas de R$ 1')
