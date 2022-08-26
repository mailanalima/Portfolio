lista = []
cont = 0
while True:
    lista.append((int(input('Digite um número: ')))
    cont = cont + 1
    sn = str(input('Deseja continuar? [S/N] ')).upper()
    if sn == 'N':
        break
print('-' * 40)
print(f'Você digitou {cont} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')
if 5 in lista:
    print('O número 5 aparece na lista.')
else:
    print('O número 5 não aparece na lista.')
