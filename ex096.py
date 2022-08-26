def area(l, c):
    areatotal = l * c
    print(f'A área do terreno é de {areatotal}m².')


print('Calcule a área de um terreno:')
print('-' * 30)
lar = float(input('Qual a largura? '))
comp = float(input('Qual o comprimento? '))
area(lar, comp)
