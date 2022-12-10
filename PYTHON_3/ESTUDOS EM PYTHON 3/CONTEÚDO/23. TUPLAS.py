#TUPLAS -> São variaveis compostas
#tuplas são imutaveis

lanche = ('Hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche) #mostra todos
print(lanche[3])#mostra item que estiver entre []
print(lanche[1:3])#define o inicio e fim

print('------------------')

for cont in range(0,len(lanche)):
    print(lanche[cont])

print('-------------------')

loja = ('Parafuso', 'Pneu', 'Martelo', 'Pá')
for produto in loja:
    print(f'A loja vende {produto}')

print(sorted(lanche)) # coloca em ordem

print(loja.count('Pneu')) #mostra quantas vezes apareceu na lista

print(loja.index('Martelo')) #mostra a posição que o item esta

del(loja) #deleta a tupla toda


