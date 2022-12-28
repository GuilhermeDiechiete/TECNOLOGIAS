function Calculadora(){
this.display = document.querySelector('.display')

this.inicia = () => {
    this capturaCliques()
}


}

const calculadora = new Calculadora()

calculadora.inicia()