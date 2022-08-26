s = float(input('Qual valor do seu salário? R$ '))
if s<=1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print(f'O novo valor do seu salário será R${novo:.2f}.')
