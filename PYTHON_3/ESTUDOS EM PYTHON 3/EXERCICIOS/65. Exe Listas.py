num = list()

for n in range(0,5):
    num.append(int(input('Digite um Valor:')))

print(f'Os numeros digitados foram {num}')
print(f'O maior valor foi: {max(num)} que esta na posição')
print(f'O menos valor foi:{min(num)}')