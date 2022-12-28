/*
FIRST-CLASS OBJECTS ( Objetos de primeira classe)

FUNCTION EXPRESSION
    -> podemos adicionar uma função em uma variavel, fazendo a função ser um dado 
*/
const função = function(){
    console.log('Sou um Dado')}

função()


/* com isso podemos executar uma função dentro de outra função como parametro*/

function executarOutraFunção(recebeFunção){
    console.log('Vou executar sua função')
    função()
}
executarOutraFunção()