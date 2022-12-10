
nomes = ('Zero','Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete','Oito','Nove', 'Dez')

while True:
    num = (int(input('Digite um numero de 0 a 20: ')))
    if 0 <= num <= 20:
        break
print((nomes[num]))
