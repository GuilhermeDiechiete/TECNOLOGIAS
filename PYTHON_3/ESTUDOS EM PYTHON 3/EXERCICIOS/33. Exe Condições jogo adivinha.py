from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador escolher de 0 a 5
print('Vou pensar em um numero de 0 a 5, vamos ver quem vence!')

jogador = int(input('Em que numero pensou?'))
print('Pensando!')
sleep(3)
if computador == jogador:
    print('Você Acertou, Parabéns!')

else:
    print('Você Perdeu, HAHA, eu pensei no numero {}'.format(computador))
