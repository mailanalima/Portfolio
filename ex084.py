pessoas, dados, peso, pessoamax, pessoamin = [], [], [], [], []
print('-' * 50)
print('CADASTRAMENTO')
print('-' * 50)
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    peso.append(dados[1])
    sn = str(input('Quer continuar? [S/N] ')).upper()
    if sn in 'N':
        break
    dados.clear()
for p in pessoas:
    if p[1] == max(peso):
        pessoamax.append(p[0])
    if p[1] == min(peso):
        pessoamin.append(p[0])
print('-' * 50)
print(f'Você cadastrou um total de {len(pessoas)} pessoas.')
print(f'O maior peso foi de {max(peso)}kg. Peso de {pessoamax}')
print(f'O menor peso foi de {min(peso)}kg. Peso de {pessoamin}')
