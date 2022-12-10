//VARIAVEIS COMPOSTAS ( ARRAY)
//Podem receber varios tipos de dados, number,string,boolean..
// cada valor tem um indice, começa no indice 0

let marca = [ 'Fiat', 'Ford', 'Chevrolet', 'Peugeot']
let modelo = ['Toro', 'Focus', 'Chevette', 208]
console.log(marca)


for (let pos=0; pos < marca.length; pos++){
    console.log(`${pos} - ${marca}`)

}

// FOR == para   IN == em
//para cada posição em marca {faça o bloco}
for(let pos in marca){
    console.log(`${pos} - ${marca}`)
}