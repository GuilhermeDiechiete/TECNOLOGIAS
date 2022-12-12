//São açoes executadas assim que são chamadas ou em decorrencia de algum evento.
//Uma função pode receber parametros e retornar resultados



function calculo(n){
    if(n % 2 == 0){
        return 'Par'
    } else {
        return 'Ímpar'
    }

}
let numero = Number(prompt('Digite um numero'))
let res = calculo(numero)
alert(res)
