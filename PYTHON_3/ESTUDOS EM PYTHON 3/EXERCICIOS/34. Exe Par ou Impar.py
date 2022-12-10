numero = int(input('Digite um Numero:'))

resultado = numero % 2

if resultado == 0:
    print('O numero {} é PAR!'.format(resultado))
else:
    print('O numero {} é IMPAR!'.format(resultado))