#Programa para verificar a média de gols de um jogador, recebendo gols para cada jogo

time = []
jogador = {}
jogos_gols = []

while  True: #Entrada de cadastro de um nome jogador
    jogador.clear()
    jogos_gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'     Quantas partidas o {jogador["nome"]} jogou? '))

    for j in range (0, partidas): # quantidade de partidas jogadas
        jogos_gols.append(int(input(f'      Quantos gols na partida {j+1}: ')))

    jogador['gols'] = jogos_gols[:]
    jogador['total'] = sum(jogos_gols)
    jogador['media'] = (sum(jogos_gols) / len(jogos_gols))
    time.append(jogador.copy())
   
    while True: #criterio de parada de cadastro
        resp = str(input('Deseja continuar [s/n]? ')).strip()[0].upper()
        if resp in 'SN':
            break
        print('Por favor digte Sim ou Não [s] [n]')
    if resp == 'N':
        break

print('-='* 30,'\n')
print(f'cod- ', end='')
for i in jogador.keys(): # mostra o cabeçario 'nome' 'gols' 'total'
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time): #mostra os valores dentro de time[{'  x ''  x'}]
    print(f'{k:>4} ', end='')     
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-='* 30,'\n')
while True: #Permite mostrar os dados do jogador ou encerrar o programa
    busca = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if busca == 999:
        break
    elif busca >= len(time):
        print((f'\nNúmero invalido! Não há jogador com o código {busca}!'))
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:\n')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1}, Marcou {g}')
    print('-='* 30)
print('<<VOLTE SEMPRE>>')