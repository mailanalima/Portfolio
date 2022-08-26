jogadores = []
jogador = {}
while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).title()
    jogador['Partidas'] = int(input('Quantas partidas ele jogou? '))
    gols = []
    for c in range(1, jogador['Partidas']+1):
        gol = int(input(f'Quantos gols ele fez na {c}ª partida? '))
        gols.append(gol)
    jogador['Gols'] = gols
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    sn = str(input('Quer continuar? [S/N] ')).upper()
    if sn in 'N':
        break
print('-' * 50)
print('Cod. ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
