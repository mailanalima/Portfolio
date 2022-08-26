from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'1º Jogador': randint(1, 6),
           '2º Jogador': randint(1, 6),
           '3º Jogador': randint(1, 6),
           '4º Jogador': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in sorteio.items():
    print(f'{k} tirou {v}.')
    sleep(0.5)
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print('-' * 35)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.5)
