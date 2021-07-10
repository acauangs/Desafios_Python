#PROGRAMA QUE RECEBA VÁRIAS NOTAS, E RETORNE UM DICIONARIO COM TOTAL DE NOTAS, MAIOR NOTA, MENOR, MÉDIA E SITUAÇÃO DO ALUNO COMO PARAMETRO OPICIONAL.

def notas(*num, sit=False):
    dados = {}
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['media'] = sum(num)/len(num)
    if sit:
        if dados['media'] < 7:
            dados['situação'] = 'Ruim'
        else:
            dados['situação'] = 'Boa'
    
    return dados



resp = notas(7, 10, 2, 6.5, sit=True)
print(resp)