valores = list()
for x in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {x+1}: ')))
print(f'Os valores digitados foram: {valores}')
print(f'O maior número digitado é: {max(valores)} na posição {valores.index(max(valores))+1}')
print(f'O menor número digitado é: {min(valores)} na posição {valores.index(min(valores))+1}')
