from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar.')
elif idade == 18:
    print('Está no ano do seu alistamento.')
else:
    print(f'Você deveria ter se alistado à {idade - 18} ano(s) atrás.')
