aluno = {}
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
aluno['Nome'] = nome
aluno['Média'] = media
if media >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
