#PROGRAMA QUE CADASTRE VARIAS PESSOAS EM UMA LISTA E CADA PESSOA CADASTRADA EM UM DICIONARIO DENTRO DESSA LISTA, 
# E NO FINAL MOSTRE: QUANTAS PESSSOAS FORAM CADASTRADAS, A MEDIA DE IDADE DO GRUPO, LISTA COM TODAS AS MULHERES, LISTA COM TODAS PESSOAS ACIMA DA MÉDIA de idade

pessoas = []
dados = {}
mulheres = []

media_idade = 0

while True:
    dados['nome'] = str(input('Nome: '))
    sexo = ' '
    
    while sexo not in 'MF': #verificar se é sexo M ou F, e valida a entrada correta dos dados
        sexo = str(input('Sexo: ')).strip()[0].upper()
        if sexo == 'F':
            mulheres.append(dados['nome'])
    
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    
 
    media_idade += dados['idade']
    
    pessoas.append(dados.copy())
    dados.clear()
    
    continuar = ' ' #Metodo para determinar a parada por escolha do usuario 
    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar um novo usúario?[S/N]')).strip()[0].upper()
    if continuar == 'N':
        print('[Encerrando...]')
        break

media_idade = (media_idade / len(pessoas))

print('-=' * 30)
print(f'\n- O grupo tem {len(pessoas)} pessoas cadastradas')
print(f'- A média de idade é de {media_idade} anos.')
print(f'- As mulheres cadastradas foram: {mulheres[0:]}')
print('A lista de pessoas que estão acima da média são: ')
print('\n')

#pessoas acima da média de idade
for e, i in enumerate(pessoas):
    if pessoas[e]['idade'] >= media_idade:
        print(pessoas[e])