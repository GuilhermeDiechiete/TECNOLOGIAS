#ESTRUTURA DE REPETIÇÃO for

# A estrutura for, vai repetir tudo que estiver dentro dela, variaveis, prints, de acordo com o numero de vezes ou com a condição

s = 0
for c in range(0,4):
    notas= float(input('Digite a nota:'))
    s += notas
print('Total de notas:{}'.format(s))
