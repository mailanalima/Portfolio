soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'Você me informou {cont} números pares e a soma é {soma}.')
