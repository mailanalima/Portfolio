def escreva(frase):
    tam = len(frase) + 4
    print('-' * tam)
    print(f"  {frase}")
    print('-' * tam)


mensagem = str(input('Mensagem: '))
escreva(mensagem)
