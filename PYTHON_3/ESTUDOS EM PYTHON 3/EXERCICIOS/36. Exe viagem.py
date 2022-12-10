km = float(input('Digite a Distância:'))

if km <=200:
    preço = km * 0.50
else:
    preço = km * 0.45

print(' o valor da corrida custara R${:.2f}'.format(preço))


