# valor vezes os 100% mais o Acrescimo

valor = float(input('Qual o valor atual de dinheiro:'))
acrescimo = float(input('Qual a porcentagem do acrescimo:'))
acres = (100 + acrescimo) * valor / 100

print('O valor atual é de R${:.2f} com o acrescimo de {}% vai ficar no valor de: R${:.2f}'.format(valor, acrescimo, acres))
