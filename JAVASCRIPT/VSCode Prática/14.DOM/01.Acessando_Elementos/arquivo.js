//ACESSANDO POR TAG
var body = document.getElementsByTagName('body')[0]
body.style.background = 'green'

//ACESSANDO POR ID
var titulo = document.getElementById('titulo')
titulo.style.color = 'blue'

//ACESSANDO POR CLASSE
var subtitulo = document.getElementsByClassName('subtitulo')[0]
subtitulo.style.color = 'orange'

//ACESSANDO POR SELETOR - usa a sintaxe do CSS. id(#) class(.)
var h3 = document.querySelector('h3')
h3.style.color = 'red'