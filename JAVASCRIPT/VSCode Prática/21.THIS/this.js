let pessoa = {
    nome: 'Guilherme',
    idade: 23,
    falar: function(){
        console.log('Ola, Tudo bem?')
    },

dizernome: function(){
    console.log('O meu nome é ' + this.nome)
}}

pessoa.dizernome()