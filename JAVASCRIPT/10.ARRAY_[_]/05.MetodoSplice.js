//SPLICE ->     nomes.splice(indice do começo, quantos elementos deseja remover, elementos para adicionar)

//        0       1        2        3           4
const nomes = ['Maria', 'João', 'Eduardo', 'Guilherme']

// pop ( remover o ultimo elemento)
nomes.splice(-1,1)
console.log(nomes)


const nomes2 = ['Maria', 'João', 'Eduardo', 'Guilherme']

// remover um elemento do array
nomes2.splice(2,1) // comecei a modificar no indice 3, removi um elemento
console.log(nomes2)

// adicionar elementos 
nomes.splice(3,0,'Neusa', 'Antonio')
console.log(nomes)

//push
nomes2.splice(nomes.length, 0, 'Luiz')
console.log(nomes2)