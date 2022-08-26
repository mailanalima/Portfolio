lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    sn = str(input('Quer continuar? [S/N] ')).upper()
    if sn in 'N':
        break
print('-' * 50)
print(f'A lista completa é: {lista}')
for n in range(0, len(lista)):
    if lista[n] % 2 == 0:
        pares.append(lista[n])
    else:
        impares.append(lista[n])
print(f'A lista de pares: {pares}')
print(f'A lista de ímpares: {impares}')
