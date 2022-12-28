const numeros = [ 1, 2, 3, 4, 5, 6, 7, 8]

for (let numero of numeros){

    if (numero === 2){
        continue // vai continuar o codigo (ele pula)
    }
    console.log(numero)
}

const num = [ 1, 2, 3, 4, 5, 6, 7, 8]
for (let n of num){
    if (n === 5){
        
        break // encerra o codigo 
    }
    console.log(n)
}