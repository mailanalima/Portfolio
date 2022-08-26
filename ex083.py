x = list(str(input('Digite uma expressão entre parênteses: ')))
cont = x.count('(') + x.count(')')
if cont % 2 == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')
