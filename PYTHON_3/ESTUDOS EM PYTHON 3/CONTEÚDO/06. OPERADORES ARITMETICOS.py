# OPERADORES ARITMETICOS SÃO:

# + Adição
# - Subtração
# * Multiplicação
# / Divisão

# ** Potência
# // Divisão Inteira
# % Resto da Divisão


# ORDEM DE PRECEDÊNCIA

# ()
# **
# * / // %
# + -

n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))

#só trocar o operador
ad = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
divint = n1 // n2
resto = n1 % n2


print('O calculo de {} e {} é igual a {}'.format(n1, n2, ad))
print('O calculo de {} e {} é igual a {}'.format(n1, n2, sub))
print('O calculo de {} e {} é igual a {}'.format(n1, n2, mult))
print('O calculo de {} e {} é igual a {}'.format(n1, n2, div))
print('O calculo de {} e {} é igual a {}'.format(n1, n2, pot))
print('O calculo de {} e {} é igual a {}'.format(n1, n2, divint))
print('O calculo de {} e {} é igual a {}'.format(n1, n2, resto))



