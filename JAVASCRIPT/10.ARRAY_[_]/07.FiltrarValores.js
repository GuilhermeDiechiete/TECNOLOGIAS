// filter, map, reduce

// retornar os numeros maiores que 10
const numeros = [5,10,40,56,58,5,23,6,42,8,7,2,1,11,56]


// função de callback para usar filtros

/* COMPLETA 
function callbackFilter(valor, indice, array){
    if (valor > 10){
        return true
    } else {
        return false
    }
}
*/

/*
function callbackFilter(valor, indice, array){
    return valor > 10
}
*/

/*
function callbackFilter(valor, ){
    return valor > 10}
*/

/*
function callbackFilter(valor){
    return valor > 10}
*/

/*
const numerosFiltrados = numeros.filter(callbackFilter)

PODEMOS JOGAR A FUNÇÃO DIRETO NA VARIAVEL

const numerosFiltrados = numeros.filter(function callbackFilter(valor){
    return valor > 10})

*/

/* PODEMOS TRANSFORMAR EM ARRAY FUNCTION

const numerosFiltrados = numeros.filter((valor) => {
    return valor > 10})

    */

    // FUNÇÃO PARA FILTROS
const numerosFiltrados = numeros.filter(valor => valor > 10)

console.log(numerosFiltrados)
