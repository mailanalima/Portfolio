n = int(input('Digite um número entre 0 e 9999: '))
n1 = str(int(100000+n))
print(f'Analisando o número {n}:')
print(f'unidade: {n1[5]}')
print(f'dezena: {n1[4]}')
print(f'centena: {n1[3]}')
print(f'milhar: {n1[2]}')

#opção2
#n = int(input('Digite um número: '))
#u = n // 1 % 10
#d = n // 10 % 10
#c = n // 100 % 10
#m = n // 1000 % 10
#print(f'unidade: {u}')
#print(f'dezena: {d}')
#print(f'centena: {c}')
#print(f'milhar: {m}')
