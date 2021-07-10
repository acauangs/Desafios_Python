#PROGRAMA QUE CADASTRE VARIOS USUARIOS ATÉ CRITERIO DE PARADA, E GUARDE OS DADOS PARA POSSIVEIS ESTATISTICAS.

maior18 = homens = mulheres = 0

while True:
    nome = (input('Digite o nome do usuario a ser cadastrado: '))
    idade = int(input('Digite a idade: '))
    sexo =' '
   
    while sexo not in 'MF':
        sexo = str(input('Sexo [M,F]')).strip()[0].upper()
    
    if idade >= 18: 
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if (sexo == 'F') and (idade < 20):
        mulheres += 1
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('[S,N]')).strip()[0].upper()
    
    if continuar == 'N':
        break   
        

print ('Total de pessoas com 18 anos,ou mais ', maior18)
print ('Total de homens cadastrado', homens)
print ('Total de mulheres com menos de 20 anos',mulheres)

        



     



