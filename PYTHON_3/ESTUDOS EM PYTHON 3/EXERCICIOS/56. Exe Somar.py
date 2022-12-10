num = 0
soma = 0
contador = 0
num = float(input('Numero:'))
while num != 999:
    contador += 1
    soma += num
    num = float(input('Numero:'))
print('Você digitou {} vezes e a soma dos numeros é {}'.format(contador, soma))
