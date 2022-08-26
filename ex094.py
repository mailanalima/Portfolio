pessoas = []
cont = 0
idades = []
mulheres = []
while True:
    pessoa = {}
    cont += 1
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Gênero [M/F]: ')).upper()
    if pessoa['sexo'] in 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    idades.append(pessoa['idade'])
    pessoas.append(pessoa.copy())
    pessoa.clear()
    sn = str(input('Deseja continuar? [S/N] ')).upper()
    if sn in 'N':
        break
print('-' * 30)
print(f'Foram cadastradas {cont} pessoas.')
mediaidade = sum(idades) / cont
print(f'A média de idade das pessoas é de {mediaidade} anos.')
print(f'As mulheres da lista são: {mulheres}')
print('Pessoas que estão acima da idade média:')
for p in pessoas:
    if p['idade'] >= mediaidade:
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('ENCERRADO')
