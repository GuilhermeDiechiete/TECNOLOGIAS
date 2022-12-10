n1 = int(input('Primeiro numero:'))
n2 = int(input('Segundo Numero:'))

if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2,n1))
else:
    print('{} e {} são iguais'.format(n1, n2))


