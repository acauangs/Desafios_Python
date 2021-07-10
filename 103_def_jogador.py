#PROGRAMA COM UM FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARAMETROS OPCIONAIS: NOME DE UM JOGADOS E QUANTOS GOLS FEZ NO CMAPEONATO;
#O PROGRAMA DEVERÁ SER CAPAZ DE IMPRIMIR ATÉ MESMO SE NADA FOR PASSADO
def ficha(j = 0, g = 0):
    if not j:
        j = '<desconhecido>'
    if not g:
        g = 0
    print('-=' * 30)
    print(f'O jogador {j} fez {g} gol(s) no campeonato.\n')

#programa principal 
jogador = str(input("Nome do jogador: "))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(jogador, gols)
