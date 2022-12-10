total18 = 0
totalM = 0
while True:
    print('CADASTRO DE PESSOAS')
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Sexo:M|F:')).strip().upper()

    while sexo not in 'MF':
        sexo = str(input('Sexo M|F:')).upper().strip()
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalM += 1
    resp = ' '
    while resp not in 'SN':
     resp = str(input('DEseja continuar? S|N:')).upper()
    if resp == 'N':
        break
print(('acabou!'))
print(f'Total de pessoas com mais de 18 anos é {total18}')
print(f'Total de Homens {totalM}')