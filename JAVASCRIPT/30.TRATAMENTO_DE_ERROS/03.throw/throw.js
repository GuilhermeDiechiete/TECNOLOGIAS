function soma (x,y){
    if(
        typeof x !== 'number' || 
        typeof y !== 'number'
    ) {
        throw('Não sao numeros'); 
    }
    return x + y;
}

console.log(soma(2 + 2))
console.log(soma('2' + 2))