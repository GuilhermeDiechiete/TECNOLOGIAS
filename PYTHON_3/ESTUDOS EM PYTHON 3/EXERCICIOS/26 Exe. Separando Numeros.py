
# MODO DE LISTA
#num = int(input('Digite os Numeros:'))
#n = str(num)
#print('Unidade: {}'.format([3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))

#MODO MATEMATICO

num = int(input('Digite os Numeros:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(' Unidade: {} Dezena: {} Centena: {} Milhar: {}'.format(u, d, c, m))

