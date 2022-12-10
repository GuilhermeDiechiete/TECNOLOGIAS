print('{:^40}'.format('LOJAS DIECHIETE'))
valor = float(input('Valor da compra:'))
print('''FORMA DE PAGAMENTO
    [1] à vista dinheiro
    [2] cartão a vista
    [3] 2x no cartão
    [4] 3x ou mais no cartão''')

opção = int(input('Qual sua Opção?'))

if opção == 1:
    print('Pagamento em dinheiro - Desconto de 10%: R${}'.format(valor - (valor * 10 / 100)))
elif opção == 2:
    print('Pagamento cartão a vista - Desconto de 10%: R${}'.format(valor - (valor * 10 / 100)))
    print('Insira o cartão!')
elif opção == 3:
    print('Pagamento 2x no cartão - Acrescimo de 2%: R${}'.format(valor * 1.2))
    print('Insira o cartão!')
elif opção == 4:
    vezes = int(input('Numero de Parcelas:'))
    print('Pagamento no cartão em {}x - Acrescimo de 4%: R${}'.format(vezes, valor * 1.4))
    print('Insira o cartão!')
else:
    print('Opção incorreta. Tente Novamente!')
