#CONDIÇÃO SIMPLES -> so utiliza o (if)
#CONDIÇÃO COMPÓSTA -> usa o (if) e (else)
#CONDIÇÃO ANINHADA -> usa os (elif)

nome = str(input('Qual é o seu Nome:'))

if nome == 'Guilherme':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Neusa':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é normal.')
print('Tenha um Bom Dia {}'.format(nome))
