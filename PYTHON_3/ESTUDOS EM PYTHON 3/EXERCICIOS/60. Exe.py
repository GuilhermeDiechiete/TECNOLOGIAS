total = 0
while True:
    produto = str(input('Nome do Produto:'))
    preço = float(input('Preço R$'))
    total += preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S|N:')).upper().strip()
    if resp == 'N':
        break
print(f'O toal de produtos foi R${total:.2f}')