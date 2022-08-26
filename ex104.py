def leiaint(texto):
    valor = input(texto)
    if valor.isdecimal():
        return int(valor)
    else:
        print('Valor Inválido. Digite um número inteiro.')
        return leiaint(texto)


#PROGRAMA PRINCIPAL
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
