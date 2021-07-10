#Programa que pergunte a distancia de uma viagem, e cobre 0.50 cents por km até 200km e .45 para viagens mais longas

distancia = int(input('Digite a distancia em km da sua viagem: '))

if distancia > 200:
    valor = (distancia * 0.45)
else:
    valor = (distancia * 0.50)

print(f'O valor cobrado pela sua viagem de {distancia}km, será de: {valor:.2f}R$')
