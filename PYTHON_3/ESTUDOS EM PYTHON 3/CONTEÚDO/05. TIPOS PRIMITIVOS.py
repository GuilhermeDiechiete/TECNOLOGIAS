# TIPOS PRIMITIVOS
# O python tem varios tipos primitivos, mas os principais são:

#INT -> Numeros Inteiros ->  4, -7 , 15000, 0075
#FLOAT -> Numeros com ponto flutuantes -> 7.0 , 15.000 , 0.075
#BOOL -> Valor Boolean -> True | False -> Sempre iniciando com letras maiusculas
#STR-> String - 'Guilherme' , '7,5'



#Como descobrir o tipo!

n1 = input('Digite um numero:')
print(type(n1))
#se eu deixar assim o python vai ler como uma string

n2 = int(input('Digite um Numero:'))
print(type(n2))
#agora definindo o tipo int, ele vai ler como numero.
