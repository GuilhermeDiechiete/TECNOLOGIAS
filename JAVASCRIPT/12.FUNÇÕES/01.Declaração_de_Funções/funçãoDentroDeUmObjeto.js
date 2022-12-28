// MODO CLASSICO
const pessoa = {
    nome: 'Guilherme',
    sobrenome: 'Diechiete',
    falar: function(){
        console.log('Oi')
    }
}
pessoa.falar()

// MODO ABREVIADO -> podemos tirar a palavra function e os dois pontos
const pessoa2 = {
    nome: 'Guilherme',
    sobrenome: 'Diechiete',
    falar(){
        console.log('Oie')
    }
}
pessoa2.falar()