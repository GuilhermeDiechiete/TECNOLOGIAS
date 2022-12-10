# valor original, vezes o desconto depois dividido por 100

valor = float(input('Valor em dinheiro:'))
desc = float(input('% de Desconto:'))

calculo = valor * desc / 100

valorfinal = valor - calculo

print('O valor de R${:.2f} com o desconto de {}%, ira ficar no valor de R${:.2f}'.format(valor, desc, valorfinal))
