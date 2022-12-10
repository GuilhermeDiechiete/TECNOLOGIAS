frase = str(input('Digite uma Frase:')).upper().strip()

print('A letra A aparece {} vezes na Frase.'.format(frase.count('A')))

print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

#upper -> joga tudo para maiusculo
#strip -> tira os espaços

#count -> vai contar as letras
#find -> vai achar a letra, começando do inicio para o fim
#rfind -> vai achar a letra, começando do final para o Inicio

#O +1 é para subir uma posição do caracter