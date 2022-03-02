function calcularValorHora() {
    const valorMes = document.querySelector('#ganho-mes')
    const horas = document.querySelector('#horas-dia')
    const horasMes = horas.value * 22
    resposta.innerHTML = 'R$ ' + parseFloat(valorMes.value/horasMes).toFixed(2)
}
