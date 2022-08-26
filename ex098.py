from time import sleep

def contador(a, b, c):
    print('--' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2)
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= c
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora sua vez de personalizar a contagem:')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
