# ALINHAMENTO DAS RESPOSTAS


nome = input('Qual é o seu nome?')

#normal
print('Olá, prazer em te conhecer {}!'.format(nome))

#20 espaços para o nome
print('Olá, prazer em te conhecer {:20}!'.format(nome))

# > Alinhado a Direita
print('Olá, prazer em te conhecer {:>20}!'.format(nome))

# < Alinhado a Esquerda
print('Olá, prazer em te conhecer {:<20}!'.format(nome))

# ^ Centralizado
print('Olá, prazer em te conhecer {:^20}!'.format(nome))

# Preenchimento dos espaços com algum simbolo
print('Olá, prazer em te conhecer {:=^20}!'.format(nome))
print('Olá, prazer em te conhecer {:.^20}!'.format(nome))



