#Programa para verificar a média de gols de um jogador, recebendo gols para cada jogo

jogador = {}
jogos_gols = []

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))


for j in range (0, partidas):
    jogos_gols.append(int(input(f'Quantos gols na partida {j+1}: ')))

jogador['gols'] = jogos_gols
jogador['total'] = sum(jogos_gols)
jogador['media'] = sum(jogos_gols) / len(jogos_gols)

print('-='*30,'\n')
print(f'Jogador {jogador["nome"]}, jogou {len(jogador["gols"])} partidas!')

for e, g in enumerate(jogos_gols):
    print(f'Na partida {e+1}, fez {g} gols.')

print(f'\nFoi um saldo de {jogador["total"]} gols, com média de {jogador["media"]} por partida.')
