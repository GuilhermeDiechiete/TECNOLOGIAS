resp = 'S'
soma = 0
quant = 0
media = 0
while resp in 'Ss':
    num = int(input('Digite um Numero:'))
    soma += num
    quant += 1
    resp = str(input('Quer continuar [S/N]:')).upper().strip()
media = soma / quant
print('Voce digitou {} numeros e a media foi {}'.format(quant, media))
