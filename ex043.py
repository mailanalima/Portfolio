a = float(input('Qual sua altura? '))
p = float(input('Qual seu peso? '))
imc = p / a ** 2
if imc < 18.5:
    print(f'Seu imc deu {imc:.1f} então você está abaixo do peso.')
elif 18.5 < imc <= 25:
    print(f'Seu imc deu {imc:.1f} então você está com seu peso ideal.')
elif 25 < imc <= 30:
    print(f'Seu imc deu {imc:.1f} então você está sobrepeso.')
elif 30 < imc <= 40:
    print(f'Seu imc deu {imc:.1f} então você está obeso.')
else:
    print(f'Seu imc deu {imc:.1f} então você está com obesidade mórbida.')
