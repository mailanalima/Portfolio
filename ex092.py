from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
an = int(input('Ano de Nascimento: '))
dados['Idade'] = date.today().year - an
dados['CTPS'] = int(input('Carteira de Trabalho ("0" caso não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Qual seu salário? '))
    dados['Aposentadoria'] = (dados['Contratação'] - an) + 35
print('-' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}.')
