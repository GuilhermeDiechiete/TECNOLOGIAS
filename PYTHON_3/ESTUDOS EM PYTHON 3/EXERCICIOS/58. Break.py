#while true inicia um laço infinito
#break e o unico que corta o laço

while True:
    num = int(input('Quer ver a tabuada de qual numero:'))
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')
print('Programa de Tabuada Encerrada!')
