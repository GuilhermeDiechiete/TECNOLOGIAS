num = (int(input('Primeiro Numero:')),
        int(input('Segundo Numero:')),
        int(input('Terceiro Numero:')),
        int(input('Quarto Numero:')))
print(f'Voce digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3)}')
else:
    print('O valor 3 não foi digitado')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')