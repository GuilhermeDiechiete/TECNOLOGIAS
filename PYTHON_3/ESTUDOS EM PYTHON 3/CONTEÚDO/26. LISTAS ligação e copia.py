#LIGAÇÃO
#se eu alterar a lista 2, a lista de 1 vai mudar tambem, elas estão ligadas
lista1 = [2,3,5,6,8,10]
lista2 = lista1
print(f'Lista 1:{lista1}')
print(f'Lista 2:{lista2}')

print('---------------------------')

#COPIA

lista3 = [2,4,6,7,4,3]
lista4 = lista3[:]

lista4[3] = 100
print(f'Lista 3:{lista3}')
print(f'Lista 4:{lista4}')