lar = float(input('Qual a largura da sua parede em metros? '))
alt = float(input('Qual a altura da sua parede em metros? '))
a = lar * alt
print(f'Sua parede tem a dimensão de {lar}x{alt} e sua área é de {a:.2f}m².')
print(f'Para pintar essa parede, você precisará de {a/2:.2f}l de tinta.')
