velocidade = int(input('Qual a velocidade do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Muito bem, você está dentro do limite da velocidade.')
else:
    print(f'Você excedeu o limite de 80Km/h. Aguarde a multa no valor de R${multa} no seu endereço.')
