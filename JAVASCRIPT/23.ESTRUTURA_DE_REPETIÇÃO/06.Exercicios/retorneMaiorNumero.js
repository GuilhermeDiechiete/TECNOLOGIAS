// FORMA MAIS TRADICIONAL
function retorna(a, b){
    if (a > b){
        return a
    } else {
        return b
    }
}
console.log(retorna(2,5))

// FORMA ABREVIADA COM OPERADOR TERNARIO
function retorna2(a, b){
    // se a>b for true, retorna a, se for falso, retorna b
    return a > b ? a : b
}
console.log(retorna2(50,5))


// com ARROW FUNCTION
const retorna3 = (a, b) => a > b ? a : b
console.log(retorna3(100,30))

