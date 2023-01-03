
// map altera os valores do array

const numeros = [ 5,10,55,65,10,20,32,85,41,52,88,20,8,4,1]

/*
função completa
const numerosX2 = numeros.map(function(valor, indice, array){
    return valor * 2
})
*/


// array function
const numerosX2 = numeros.map(valor => {
    return valor * 2})
    
console.log(numerosX2)