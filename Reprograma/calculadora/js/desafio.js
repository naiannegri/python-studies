
function calcular(){
    let valorHora = document.querySelector('#valor-hora')
    let horasProjeto = document.querySelector('#horas-projeto')
    resposta.innerHTML = 'R$ ' + parseFloat(valorHora.value * horasProjeto.value).toFixed(2)
}