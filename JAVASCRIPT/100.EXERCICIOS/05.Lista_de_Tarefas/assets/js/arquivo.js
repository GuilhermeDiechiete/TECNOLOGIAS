const inputNovaTarefa = document.querySelector('.inputNovaTarefa')
const buttonAddTarefa = document.querySelector('.buttonAddTarefa')
const ListaTarefas = document.querySelector('.tarefas')

//FUNÇÃO PARA CRIAR LI
function criaLi(){
    const li = document.createElement('li')
    return li
}

//FUNÇÃO PARA CRIAR TAREFA
function criaTarefa(textoInput){
    const li = criaLi()
    li.innerText = textoInput
    ListaTarefas.appendChild(li)
    limpaInput()
    botaoApagar(li)
    salvarTarefa()
}
function salvarTarefa(){
    const liTarefas = ListaTarefas.querySelectorAll('li')
    const listaDeTarefas = []

    for (let tarefa of liTarefas) {
        const tarefaTexto = tarefa.innerText
        tarefaTexto = tarefaTexto.replace('Apagar', '')
        listaDeTarefas.push(tarefaTexto)
    }
    const tarefaJSON = JSON.stringify(listaDeTarefas)
    localStorage.setItem('tarefas', tarefaJSON)
}

// FUNÇÃO PARA LIMPAR O INPUT
function limpaInput(){
    inputNovaTarefa.value = ''
    inputNovaTarefa.focus()
}

//FUNÇÃO DO BOTÃO
buttonAddTarefa.addEventListener('click', function() {
    if (!inputNovaTarefa.value) return
    criaTarefa(inputNovaTarefa.value)
})

// FUNÇÃO APAGAR LI
function botaoApagar(li){
    li.innerText += ' '
    const botaoApagar = document.createElement('button')
    botaoApagar.innerText = 'Apagar'
    botaoApagar.setAttribute('class', 'apagar')
    li.appendChild(botaoApagar)
}

document.addEventListener('click', function(e){
    const el = e.target
    if (el.classList.contains('apagar')){
        el.parentElement.remove()
        salvarTarefa()
    }
})

function addTarefasSalvas() {
    const tarefas = localStorage.getItem('tarefas')
    const listaDeTarefas = JSON.parse(tarefas)

    for (let tarefa of listaDeTarefas){
        criaTarefa(tarefa)
    }
}
addTarefasSalvas()
