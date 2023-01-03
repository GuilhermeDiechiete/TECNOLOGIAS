// reduce -> para reduzir o array em apenas um elemento

const numeros = [ 5,10,25,66,88,45,52,66,7,8,2]

const total = numeros.reduce(function(acumulador, valor){ 
    acumulador += valor
    return acumulador
})

console.log(total)