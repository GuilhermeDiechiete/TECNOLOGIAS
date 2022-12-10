#FATIAMENTO

nome ='Guilherme Diechiete'

#mostra somente a letra escolhida
print('Vai mostrar apenas a letra selecionada {} ->'.format(nome[3]))

#para selecionar varios caracteres, digitamos a posição do primeiro, depois digitamos o ultimo, sempre adicionando mais uma casa.
print('Vai mostrar do 0 ate o 10 {} ->'.format(nome[0:10]))

#colocamos a posição inicial e a posição final, depois colocamos a quantidade de casas que desejamos pular
print('Vai mostrar do 0 ate 10, pulando de dois em dois {}'.format(nome[0:10:2]))

#vai mostrar do inicio ate a casa 5
print('Vai mostrar do inicio ate o casa 5 {}'.format(nome[:5]))

#vai começar na casa selecionada ate o final
print('Vai mostrar da casa selecionada ate o final {}'.format(nome[15:]))

print('vai comecar na casa 2 e vai ate o final, pulando de 3 em 3 {}'. format(nome[2::3]))
