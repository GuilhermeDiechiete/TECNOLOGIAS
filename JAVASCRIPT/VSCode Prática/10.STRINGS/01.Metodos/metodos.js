// length - mostra o comprimento da string
var nome = 'Guilherme'
var sobrenome = 'Diechiete'
console.log(nome.length)

// indexOf - busca o caracter por indice
console.log(nome[2])

//indexOf - podemos localizar palavras
console.log(sobrenome.indexOf('hie'))

// slice - remover palavras ou letras
var hiet = sobrenome.slice(4, 8)
console.log(hiet)

//replace
var troca = sobrenome.replace('Diechiete', 'Silva')
console.log(troca)

// toLowerCase - joga tudo pra minusculo
var nomecompleto = 'Guilherme Diechiete da Silva'
console.log(nomecompleto.toLocaleLowerCase())

//toUpperCase - joga tudo para maiusculo
console.log(nomecompleto.toUpperCase())

// trim - remove os espaços 
var nome1 = '       Guilherme      '
var nomeTrim = nome1.trim()
console.log(nome1)
console.log(nomeTrim)

// split - transforma em array
console.log(nomecompleto.split(" "))