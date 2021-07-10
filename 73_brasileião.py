
tabela = ('Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Atlético-MG', 'Bragantino', 'Fluminense', 'Bahia', 'chapecoense', 'Parmeiras', 'Céara SC', 'Santos', 'Internacional')

print('-=' * 15)
print ('\nTabela brasileirão 2021', tabela)

print('-=' * 15)
print('\nOs 5 primeiros são: ', tabela[0:5])

print('-=' * 15)
print('\nOs 4 ultimos são: ', tabela[-4:])

print('-=' * 15)
print('\nA ordem alfabetica é: ', sorted(tabela))

print('-=' * 15)
print('\nO chapecoense está na', tabela.index("chapecoense"),'Posição')
