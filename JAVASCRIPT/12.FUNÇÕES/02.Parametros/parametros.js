
function função(num1, num2){
    const soma = num1 + num2
    console.log(soma)
}

// quando chamamos a função, podemos enviar um valor para o parametro da função
função(2, 5)


//podemos deixar um valor prefixado no parametro, para nao ocorrer erro NaN caso um dos valores para o parametro nao seja enviado
function função2(num1=0, num2=0){
    const soma = num1 + num2
    console.log(soma)
}
função2(2) // so com o primeiro valor