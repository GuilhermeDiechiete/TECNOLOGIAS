familia = ('Antonio','Neusa', 'Luana', 'Guilherme', 'Joaquim', 'Dhaniela')

print(f'Os mais velhos são {(familia[0:2])}')
print(f'Os mais novos são {(familia[-2:])}')
print({familia.index('Guilherme')}) #mostra em que posição esta o item
print(f'A orgem alfabetica é {sorted(familia)}') # organiza por nome