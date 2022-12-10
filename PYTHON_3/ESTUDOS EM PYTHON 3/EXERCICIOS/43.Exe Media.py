p1 = float(input('Primeira Nota:'))
p2 = float(input('Segunda Nota:'))
media = (p1 + p2) / 2

if media >= 7:
    print('Com as notas {} e {} sua media é {}'.format(p1, p2, media))
    print('APROVADO')
elif media <= 5:
    print('Com notas {} e {} sua media é {}'.format(p1, p2, media))
    print('REPROVADO')
elif media > 4.1 and media < 6.9:
    print('Com as notas {} e {] sua media é {}'.format(p1, p2, media))
    print('RECUPERAÇÃO!')

