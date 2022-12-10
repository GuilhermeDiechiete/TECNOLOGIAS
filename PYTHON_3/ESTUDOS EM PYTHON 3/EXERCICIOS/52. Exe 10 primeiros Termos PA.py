termo = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
dec = termo + (10-1) * razao
for c in range(termo, dec + razao, razao):
    print('{}'.format(c), end=' - ')
print('ACABOU')