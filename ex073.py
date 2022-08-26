times = ('Internacional', 'Atlético MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeiras',
        'Santos', 'Grêmio', 'Esporte Recife', 'Corinthians', 'Fortaleza', 'Ceará SC',
        'Atlético GO', 'Bahia', 'Coritiba', 'Bragantino', 'Botafogo', 'Vasco',
        'Atlético PR', 'Goiás')
print('------' * 20)
print(f'Lista de times: {times}')
print('------' * 20)
print(f'Os cinco primeiros são: {times[:5]}')
print('------' * 20)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('------' * 20)
print(f'Times em ordem alfabética {sorted(times)}')
print('------' * 20)
print(f'O Grêmio está na {times.index("Grêmio")+1}ª posição.')
print('------' * 20)
