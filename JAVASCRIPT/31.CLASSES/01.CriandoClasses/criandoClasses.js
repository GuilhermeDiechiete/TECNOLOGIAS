class Pessoa {
    constructor(nome, sobrenome) {
        this.nome = nome
        this.sobrenome = sobrenome
    }
    falar(){
        console.log(`${this.nome} está falando`)
    }
}

const p1 = new Pessoa('Guilherme', 'Diechiete')
const p2 = new Pessoa('Neusa', 'Diechiete')
const p3 = new Pessoa('Dhaniela', 'Souza')
console.log(p1, p2, p3)

p1.falar()