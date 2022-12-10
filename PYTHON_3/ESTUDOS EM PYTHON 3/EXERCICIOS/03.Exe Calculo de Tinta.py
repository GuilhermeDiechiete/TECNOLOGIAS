 # calculo de litros de tinta

altura = float(input('Altura:'))
largura = float(input('Largura:'))

soma = altura * largura

tinta = soma / 4

print('A area total da parede é {:.2f} , então você ira precisar de {:.2f} litros de tinta '.format(soma , tinta))