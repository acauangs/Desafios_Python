from random import sample

sorteados = []

escolha = int(input('Quantos jogos você quer sortear: '))

while escolha > 0:
    jogos = sample(range(0, 61), 6)
    sorteados.append(jogos[:])
    jogos.clear()
    escolha -= 1

print('-='* 5,'Sorteando',(len(sorteados)),'Jogos', '-='* 5)

for e, j in enumerate(sorteados):
    print(f'Jogo {e+1}: {j}')

print('-='* 5,'Boa Sorte!', '-='* 5,'\n')