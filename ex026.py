frase = str(input('Escreva uma frase: ')).lower().strip().replace('á','a').replace('à','a').replace('ã','a').replace('â','a')
c = frase.count('a')
p = frase.find('a') + 1
u = frase.rfind('a') + 1
print(f'Informações sobre a letra A:')
print(f'Aparece {c} vezes.')
print(f'Aparece pela primeira vez na posição {p}.')
print(f'Apareceu pela última vez na posição {u}.')
