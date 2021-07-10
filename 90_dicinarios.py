#PROGRAMA QUE CRIA UM DICIONARIO QUE LEITA NOME E NOTA DE UM ALUNO, DEPOIS DEVOLVA O NOME E BASEADO NA NOTA SE ELE ESTA APROVADO OU NÃO
aluno = {}

aluno['nome']  = str(input('Nome: '))
aluno['media'] = float(input('Nota: '))

print(f"O nome do aluno é {aluno['nome']}") 
print(f"A média é {aluno['media']}")

if aluno['media'] >= 7:
    print('Situação é aprovado :)')
else:
    print('Situação igual a reprovado :(')
