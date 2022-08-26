n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Sua média foi {m:.1f} e está reprovado.')
elif 5 <= m < 7:
    print(f'Sua média foi de {m:.1f} e está de recuperação.')
elif m >= 7:
    print(f'Sua média foi de {m:.1f} e está aprovado.')
