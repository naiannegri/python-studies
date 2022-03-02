
//var inputAno = document.querySelector(#ano);

//var paragrafoResposta = document.querySelector('#respostaAno') 

//function cliquei() {
 //   paragrafoResposta.innerHTML = document.querySelector(#respostaAno)
//}



//let anoNascimento = window.prompt('Informe o ano de nascimento ')
//console.log('Você tem ' + (2022 - anoNascimento) + ' anos')

//DOM - Document Object Mode - HTML


//querySelectorAll = seleciona todas os ids

function cliquei () {
    let ano = document.querySelector('#ano')
    let resposta  = document.querySelector('#respostaAno')
    let respostaAtual = resposta.innerHTML
    resposta.innerHTML = "Resposta: ";

    resposta.innerHTML = respostaAtual + ano.value
} 
