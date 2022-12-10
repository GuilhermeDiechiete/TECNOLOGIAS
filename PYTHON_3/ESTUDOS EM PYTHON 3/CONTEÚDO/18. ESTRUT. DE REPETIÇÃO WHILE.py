# usamos o while quando nao sabemos o final
#exe, nao sabemos quantas vezes o usuario vai errar a digitação do sexo
#então precisamos definir um resultado para proseguir

sexo = str(input('Sexo [M-F]: ')).strip().upper()[0]

#enquanto sexo for diferente de MF, vai continuar perguntando o sexo
while sexo not in 'MF':
    sexo = str(input('Sexo invalido:')).strip().upper()[0]
print('Sexo definido: {}'.format(sexo))
