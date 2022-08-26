extenso = 'Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
n = int(input('Escolha um número entre 0 e 20: '))
while n not in range(0,21):
    n = int(input('Tente novamente. Escolha um número entre 0 e 20: '))
print(f'Você escolheu o número {extenso[n]}')
