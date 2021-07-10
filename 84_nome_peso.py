#faça um programa que leia o nome e o peso de várias pessoas, no final mostre quantas pessoas foram cadastradas, as pessoas mais pesadas e as pessoas mais leves

pessoas = []
dados = []

while True: 
    
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    continuar = ' '
    
    while continuar not in 'SN':
        continuar = input('Você deseja cadastrar um novo usuario? [S/N]').strip()[0].upper()

    if continuar == 'N':
        print(['[Encerrando...]'])
        break

print('\nAo total você cadastrou:', len(pessoas),'pessoas')

for p in pessoas: 
    if p[1] >= 100:
        print(f'\nPessoa com mais de 100kgs: {p[0]} com {p[1]}')

print('-=-' * 30)

for p in pessoas:
    if p[1] <= 70:
        print(f'\nPessoas com menos de 70kgs: {p[0]} com {p[1]} \n')



