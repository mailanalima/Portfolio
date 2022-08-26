palavras = ('gato', 'cachorro', 'maquiagem', 'augusto')
for n in palavras:
    print(f'\nNa palavra {n} temos: ', end='')
    for l in n:
        if l.lower() in 'aeiou':
            print(l, end=' ')
