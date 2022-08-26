from datetime import date

def voto(a):
    idade = date.today().year - a
    if 65 > idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade >= 65 or idade == 16 or idade == 17:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: NÃO VOTA.')


ano = int(input('Ano de Nascimento: '))
voto(ano)
