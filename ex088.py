from random import randint
lista = list()
sorteios = list()
cont = 0
jogos = int(input('Quantos jogos você quer sortear? '))
total = 1
while total <= jogos:
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    sorteios.append(lista[:])
    lista.clear()
    total = total + 1
print(f'Os números sorteados foram:')
for i, l in enumerate(sorteios):
    print(f'Jogo {i}: {l}')
