// podemos adicionar um array em outra variavel para fazer uma copia
const sobrenomes = ['Diechiete', 'Pereira', 'Silva', 'Souza']
const novoSobrenomes = [...sobrenomes]

novoSobrenomes.pop()
console.log(sobrenomes)
console.log(novoSobrenomes)