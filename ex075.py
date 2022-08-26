v = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print(f'Você digitou os valores {v}. ')
if 9 in v:
    print(f'O valor 9 apareceu {v.count(9)} vezes.')
else:
    print(f'O valor 9 não foi encontrado.')
if 3 in v:
    print(f'O valor 3 apareceu na {v.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não foi encontrado.')
print('Os valores pares digitados foram', end=' ')
for n in v:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('nenhum!')
        break
