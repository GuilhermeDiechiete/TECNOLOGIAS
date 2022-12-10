import ntpath

nome = str(input('Digite seu nome:')).strip()

nomelist = nome.split() #vai jogar as palavras em uma lista


print('Seu primeiro nome é {}'.format(nomelist[0]))
print('Seu Ultimo nome é {}'.format(nomelist[len(nomelist)-1]))
