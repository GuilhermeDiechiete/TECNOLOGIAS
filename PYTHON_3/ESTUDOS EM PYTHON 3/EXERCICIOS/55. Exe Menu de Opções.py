n1 = int(input('Primeiro Numero:'))
n2 = int(input('Segundo Numero:'))

opção = 0
while opção != 5:

    print('''
    OPÇÕES
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opção = int(input('Qual sua opção:'))

    if opção == 1:
        print('O numero {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('O numero {} x {} é igual a {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe novos valores')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    else:
        print('Opção invalidade')

print('Fim do Programa')

