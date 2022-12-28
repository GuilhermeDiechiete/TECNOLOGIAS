// DIA SEMANA - DIA - MES - ANO - HORA - MINUTOS
const data = new Date()

function funçãoData(data){
    const dia_Semana = diaDaSemana(data.getDay())
    const dia = data.getDate()
    const mes = data.getMonth()
    const ano = data.getFullYear()
    const hora = data.getHours()
    const min = data.getMinutes()
    console.log(`${dia_Semana}, ${dia}/${mes}/${ano} | ${hora}:${min}`)
}
funçãoData(data)

function diaDaSemana(diaSemana){
    let retornoDiaSemana

    switch(diaSemana){
        case 0:
            retornoDiaSemana = 'Domingo'
            return retornoDiaSemana
        case 1:
            retornoDiaSemana = 'Segunda'
            return retornoDiaSemana
        case 2:
            retornoDiaSemana = 'Terça'
            return retornoDiaSemana
        case 3:
            retornoDiaSemana = 'Quarta'
            return retornoDiaSemana
        case 4:
            retornoDiaSemana = 'Quinta'
            return retornoDiaSemana
        case 5:
            retornoDiaSemana = 'Sexta'
            return retornoDiaSemana
        case 6:
            retornoDiaSemana = 'Sabado'
            return retornoDiaSemana
        default:
            retornoDiaSemana = ''
            return retornoDiaSemana
}}








