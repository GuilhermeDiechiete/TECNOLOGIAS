// retorna um valor
// quando o return é usado, termina a função ( tipo um break)

function soma(a,b){
    const calculo = a + b
    return calculo
}
console.log(soma(2,5))


// RETORNAR UM OBJETO
function criaPessoa(nome, sobrenome){
    return { nome, sobrenome}
}
const p1 = criaPessoa('Guilherme', 'Diechiete')
console.log(p1)


//RETORNO DE FUNÇAO INTERNA

function falarFrase(comeco){
    function falaResto(resto){
        return comeco + '' + resto
    }
    return falaResto
}
const falar = falarFrase('Eu estou falando sobre')
console.log(falar(' Javascript'))
