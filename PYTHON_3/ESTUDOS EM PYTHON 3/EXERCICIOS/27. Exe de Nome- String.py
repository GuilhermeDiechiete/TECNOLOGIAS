# Ver se a cidade digitada é igual a Santiago

cid = str(input('Qual sua cidade: ')).strip() #strip desconcidera os espaços
print(cid[:9].upper() == 'SANTIAGO') #jogamos tudo para maiusculo
