// OBJETO DATE
const data = new Date()//GUARDA A DATA E HORA 

console.log(data) // mostra a data
console.log(data.toString()) // data no formato gringo

console.log('Dia', data.getDate())
console.log('Mes', data.getMonth())
console.log('Ano', data.getFullYear())
console.log('Hora', data.getHours())
console.log('Min', data.getMinutes())
console.log('Seg', data.getSeconds())
console.log('ms', data.getMilliseconds())
console.log('Dia da Semana', data.getDay())
