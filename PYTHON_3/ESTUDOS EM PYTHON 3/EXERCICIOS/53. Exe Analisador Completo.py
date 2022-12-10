# Quando queremos acumular os valores usamos VARIAVEL = 0
# Quando queremos contar a quantidade de algo usamos VARIAVEL = +1

somaidade = 0
mediaidade = 0
maiorhomem = 0
maisvelho = ''
mulher20 = 0

for pessoas in range(1,4):
    print('{} Pessoa'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M - F]')).strip()

    somaidade += idade
    if pessoas == 1 and sexo in 'Mm':
        maiorhomem = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
        mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorhomem, maisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))