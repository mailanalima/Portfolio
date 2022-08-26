n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
#VERIFICANDO QUEM É O MENOR VALOR
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(f'O menor valor foi {menor}.')
#VERIFICANDO QUEM É O MAIOR VALOR
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print(f'O maior valor foi {maior}.')
