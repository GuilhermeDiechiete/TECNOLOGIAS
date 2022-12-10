imovel = float(input('Valor do Imovél: R$'))
salario = float(input('Seu Salário: R$'))
anos = int(input('Quantos anos de Financiamento:'))

#valor do imovel dividido pelos meses -> vai mostrar o valor da parcela
parcela = imovel / (anos * 12)

#salario vezes 30 dividido por 100 -> vai mostrar o valor maximo que pode ser a prestação
maximo = salario * 30 / 100

#se a parcela for maior que o maximo dos 30%
if parcela > maximo:
    print('Financiamento Negado!')
else:
    print('Financiamento Aprovado!')