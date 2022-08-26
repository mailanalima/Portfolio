valores = [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        valores[x].append(int(input(f'Digite um valor para a posição ({x},{y}): ')))
print('-' * 50)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{valores[x][y]}]', end='')
    print()
