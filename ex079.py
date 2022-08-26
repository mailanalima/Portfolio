valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não vou adicionar.')
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break
print('-' * 40)
valores.sort()
print(f'Você digitou os valores: {valores}')
