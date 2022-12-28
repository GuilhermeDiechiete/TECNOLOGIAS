// ARRAY
// Cada valor de um array tem um indice, começando do 0

//                   0           1        2        3        4
const familia = ['Guilherme', 'Luana','Antonio','Neusa','Joaquim']


//ACESSANDO TODO O ARRAY
console.log(familia)

//ACESSANDO OS ELEMENTOS DO ARRAY
console.log(familia[0])
console.log(familia[3])
console.log(familia[2])


//EDITAR UM ELEMENTO DO ARRAY
familia[4] = 'Joca'
console.log(familia)

//DESCOBRIR O COMPRIMENTO DO ARRAY
const tamanhoArray = familia.length
console.log(tamanhoArray)


//    ADICIONAR ELEMENTO

//ADICIONAR ELEMENTO ( precisa saber o indice)
familia[5] = 'Dhaniela'
familia[6] = 'Juliano'
console.log(familia)

//ADICIONAR ELEMENTO NO FINAL DO ARRAY
familia.push('Neide')
console.log(familia)

//ADICIONAR ELEMENTO NO INICIO DO ARRAY
familia.unshift('Thirteu')
console.log(familia)

//   REMOVER ELEMENTOS

//REMOVER ELEMENTO NO FINAL DO ARRAY
familia.pop()
console.log(familia)

// podemos salvar os elementos removidos
const removido = familia.pop()
console.log(removido)

//REMOVER ELEMENTO DO INICIO DO ARRAY
familia.shift()
console.log(familia)

//DELETAR ELEMENTO SEM ALTERAR OS INDICES
delete familia[1]
console.log(familia) // o elemento fica undefined

//FATIAR O ARRAY
console.log(familia.slice(0,4))//(inicio , fim)
console.log(familia.slice(2, -1))//(inicio, menos tanto do final)

//TYPEOF
console.log(typeof familia)// é um objeto
console.log(familia instanceof Array)//saber se a origem dele é um array