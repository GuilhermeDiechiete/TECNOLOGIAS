
nome = str(input('Nome Completo:')) .strip()

print('Seu nome em Maiusculo é {}'.format(nome.upper()))
print('Seu nome em Minusculo é {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separaosnomes = nome.split()

print('seu primeiro nome é {}'.format(separaosnomes[0]))