from random import randint
computador = randint(0,5)
print('Vou pensar em um número de 0 a 5...')
jogador = int(input('Tente adivinhar qual foi esse número: '))
if jogador == computador:
    print('PARABÉNS, VOCÊ ACERTOU!!!')
else:
    print(f'Eu pensei no número {computador}, você errou.')
