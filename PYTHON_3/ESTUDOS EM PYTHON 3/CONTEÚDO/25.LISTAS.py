#CRIAR LISTAS VAZIAS
loja = list()

for produtos in range(0,5):
    loja.append(str(input('Nome Produto:')))

if loja == 0:
    print(acabou)





for posição, itens in enumerate(loja):
    print(f'{posição}- {itens}')