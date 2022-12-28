// FORMA CORRETA E SIMPLES
const h1 = document.querySelector('.titulo')
const data = new Date()
const opções = {
    dateStyle: 'full',
    timeStyle: 'short'
}
h1.innerHTML = data.toLocaleDateString('pt-BR', {dateStyle: 'full'})

// COM SISTEMA SWITCH
/*
const bloco = document.querySelector('.bloco')
const h1 = document.querySelector('.titulo')

const data = new Date()

function getDiaSemana(diaSemana) {
    let diaSemanaT

    switch (diaSemana){
        case 0:
            diaSemanaT = 'Domingo'
            return diaSemanaT
        case 1:
            diaSemanaT = 'Segunda-Feira'
            return diaSemanaT
        case 2:
            diaSemanaT = 'Terça-Feira'
            return diaSemanaT
        case 3:
            diaSemanaT = 'Quarta-Feira'
            return diaSemanaT
        case 4:
            diaSemanaT = 'Quinta-Feira'
            return diaSemanaT
        case 5:
            diaSemanaT = 'Sexta-Feira'
            return diaSemanaT
        case 6:
            diaSemanaT = 'Sabado'
            return diaSemanaT
        default:
            diaSemanaT = ''
            return diaSemanaT
    }
}
function getNomeMes(numMes){
    let mes 
    switch (numMes){
        case 0: 
            mes = 'Janeiro'
            return mes
        case 1: 
            mes = 'Fevereiro'
            return mes
        case 2: 
            mes = 'Março'
            return mes
        case 3: 
            mes = 'Abril'
            return mes
        case 4: 
            mes = 'Maio'
            return mes
        case 5: 
            mes = 'Junho'
            return mes
        case 6: 
            mes = 'Julho'
            return mes
        case 7: 
            mes = 'Agosto'
            return mes
        case 8: 
            mes = 'Setembro'
            return mes
        case 9: 
            mes = 'Outubro'
            return mes
        case 10: 
            mes = 'Novembro'
            return mes
        case 11: 
            mes = 'Dezembro'
            return mes
    }
}
function zeroEmMinutos (num){
    return num >= 10 ? num : `0${num}`
}
function criaData(data){
    const diaDaSemana = getDiaSemana(data.getDay())//passei o parametro para ativar a função
    const numMes = data.getMonth()//varivel como o valor do mes
    const nomeMes = getNomeMes(numMes)//passei o parametro para ativar a função
    return `${diaDaSemana} , ${data.getDate()} de ${nomeMes} de ${data.getFullYear()} ${zeroEmMinutos(data.getHours())}:${zeroEmMinutos(data.getMinutes())}`
}

h1.innerHTML = criaData(data)

*/
