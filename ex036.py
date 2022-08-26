c = int(input('Qual o valor da casa a ser financiada? R$'))
s = int(input('Qual sua renda mensal? R$'))
a = int(input('Em quantos anos você quer pagar? '))
p = c / (a * 12)
if p <= (s * 30 / 100):
    print(f'O valor da parcela do seu financiamento será de R${p:.2f}, e foi aprovado.')
else:
    print(f'Infelizmente seu financiamento não foi aprovado pois a parcela de R${p:.2f} ultrapassa 30% do seu salário.')
