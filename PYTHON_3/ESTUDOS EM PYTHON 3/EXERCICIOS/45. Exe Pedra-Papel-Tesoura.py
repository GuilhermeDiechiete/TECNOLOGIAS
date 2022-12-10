from random import randint

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('{:^20}'.format('JOKENPÔ'))
print('''
[0] PEDRA
[1] PAPEL
[2]TESOURA''')
jogador = int(input('Qual sua jogada:'))

print('-'*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-'*11)
