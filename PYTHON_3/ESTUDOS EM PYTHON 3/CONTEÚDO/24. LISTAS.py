#LISTAS
#São variaveis compostas e SÃO MUTAVEIS
#usamos [] para listas

loja = ['Martelo', 'Prego', 'Broca', 'Parafuso', 'Fita']

#MUDAR O ITEM DA LISTA
loja[3] = 'Chave de Fenda'
print(f'{loja}')

#ADICIONA ITEM NO FINAL DA LISTA
loja.append('Fio de luz')
print(f'{loja}')

#ADICIONA ITEM EM QUALQUER POSIÇÃO
loja.insert(0,'Carregador')
print(f'{loja}')

#DELETAR ITEM, á 3 formas ----> loja.pop(3) <---- ----> loja.remove('item') <----- ou
del loja[3]
print(f'{loja}')

#DELETAR ITEM COM O IF
if 5 in loja:
    loja.remove(5)
print(f'{loja}')

