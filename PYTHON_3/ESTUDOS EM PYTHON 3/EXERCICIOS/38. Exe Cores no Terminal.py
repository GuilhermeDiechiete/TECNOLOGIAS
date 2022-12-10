nome = 'Guilherme'

#add direto no print
print('\033[0:34m Ola mundo\033[m')

#add no .format
print('Muito prazer em te conhecer {}{}{}!!!'.format('\033[0:34m', nome, '\033[m'))



# podemos criar variaveis com dicionário de cores
cor = {'Azul': '\033[0:34m',
       'Vermelho': '\033[0:31m'}

#coloca o nome do dicionario e nome da cor entre ['']
print('Ola meu amigo {}{}{}'.format(cor['Azul'], nome, cor['Azul']))
print('Ola meu amigo {}{}{}'.format(cor['Vermelho'], nome, cor['Vermelho']))
