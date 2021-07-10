def voto(nasc):
    from datetime import date, datetime
    ano = datetime.now().year
    idade = ano - nasc
   
    if idade < 16:
        return f'Com {idade}: Não Vota'
    elif (idade > 65) or (16 <= idade < 18):
        return f'Com {idade}: Voto Opcional'
    else: 
        return f'Com {idade}: Voto é Obrigatorio'
   


print('=-' * 30)

n = int(input('Digite a sua data de nascimento: '))
print(voto(n))

 