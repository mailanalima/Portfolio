s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while s not in ['M','F']:
    s = str(input('Dados inválidos. Informe seu sexo: [M/F] ')).upper()
print('OK')
