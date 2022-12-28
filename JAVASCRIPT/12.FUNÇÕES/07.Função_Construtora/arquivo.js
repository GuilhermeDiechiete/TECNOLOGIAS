//FUNÇÃO CONSTRUTORA -> retorna objetos
//FUNÇÃO FABRICA -> retorna objetos
// inicia com letra Maiuscula

function Pessoa(nome, sobrenome){
    this.nome = nome
    this.sobrenome = sobrenome

    this.metodo = function(){
        console.log('Sou um metodo')
    }
}

// precisa do new e o nome sempre com letra maiuscula
const pessoa1 = new Pessoa('Guilherme', 'Diechiete')
const pessoa2 = new Pessoa('Dhaniela', 'Souza')
// a palavra new cria um objeto vazio e aponta o objeto para a variavel
pessoa1.metodo()

console.log(pessoa1, pessoa2)
console.log(typeof(pessoa1)) // object
console.log(typeof(pessoa2)) // object

