from random import randint
computador = randint(0,10)
print('Acabei de pensar em um número de 0 a 10...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador  == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais... Tente mais uma vez')
        elif jogador > computador:
            print('Um pouco menos... Tente mais uma vez')
print(f'ACERTOOU! Com {palpites} tentativas.')
