// selecionei a area dos paragrafos
const paragrafos = document.querySelector('.paragrafos')
// selecionei os paragrafos dentro da area paragrafos
const ps = paragrafos.querySelectorAll('p')

//puxei todas as configurações de estilo do body
const estiloBody = getComputedStyle(document.body)
// selecionei a confg de background
const backgroundBody = estiloBody.backgroundColor

for (let p of ps){
    p.style.backgroundColor = backgroundBody
}
