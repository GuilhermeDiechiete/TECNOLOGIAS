// new Object

const pessoa = new Object()

pessoa.nome = 'Guilherme'
pessoa.sobrenome = 'Diechiete'
pessoa.idade = 23
pessoa.falarNome = function(){
    console.log(`${this.nome} está falando seu nome` )
}

console.log(pessoa)
pessoa.falarNome()