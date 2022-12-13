

//selecionando a tag PAI que irá ficar o elemento criado
var header = document.querySelector('header')

//criando o elemento h1
var novotitulo = document.createElement('h1')

//criando o texto do elemento h1
var textotitulo = document.createTextNode('Inserindo elementos no HTML pelo JS')

//adicionando o texto ao elemento
novotitulo.appendChild(textotitulo)

//adicionando o elemento na tag PAI do HTML
header.appendChild(novotitulo)