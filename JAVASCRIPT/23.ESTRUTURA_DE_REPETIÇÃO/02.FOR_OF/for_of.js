    //indices 012345678
const nome = 'Guilherme';
// FOR CLASSICO
for (let inicio = 0; inicio < nome.length; inicio++){
    console.log(nome[inicio])}


const sobrenome = 'Diechite';
// FOR IN -> quando usamos o IN vem o indice
for (let palavra in nome){
    console.log(nome[palavra])}


const nome1 = ['Dhaniela', 'Guilherme']
// FOR OF -> quando usamos o OF vem o valor
for (let valor of nome1){
    console.log(valor)
}

