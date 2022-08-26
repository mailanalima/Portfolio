jogador = {}
jogador['Nome'] = str(input('Nome do Jogador: '))
jogador['Partidas'] = int(input('Quantas partidas ele jogou? '))
gols = []
for c in range(1, jogador['Partidas']+1):
    gol = int(input(f'Quantos gols ele fez na {c}ª partida? '))
    gols.append(gol)
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('-' * 30)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('-' * 30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for c in range(1, jogador['Partidas']+1):
    print(f'Na {c}ª partida fez {gols[c-1]} gols.')
