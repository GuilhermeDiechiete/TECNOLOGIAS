from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('Os numeros sorteados foram: ', end=' ')

for n in numeros:
    print(f'{n}', end=' ')
print(f'\n Maior valor:{max(numeros)}')
print(f'\n Menos valor: {min(numeros)}')