from datetime import date
atual = date.today().year
nasc = int(input('Qual ano do seu nascimento? '))
idade = atual - nasc
if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é a MIRIM.')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é a INFANTIL.')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é a JUNIOR.')
elif idade == 20:
    print(f'Você tem {idade} anos e sua categoria é a SÊNIOR.')
elif idade > 20:
    print(f'Você tem {idade} anos e sua categoria é a MASTER.')
