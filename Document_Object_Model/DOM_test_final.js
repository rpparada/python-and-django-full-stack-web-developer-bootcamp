var casillas = []

casillas.push(document.querySelector('#uno'))
casillas.push(document.querySelector('#dos'))
casillas.push(document.querySelector('#tres'))
casillas.push(document.querySelector('#cuatro'))
casillas.push(document.querySelector('#cinco'))
casillas.push(document.querySelector('#seis'))
casillas.push(document.querySelector('#siete'))
casillas.push(document.querySelector('#ocho'))
casillas.push(document.querySelector('#nueve'))

var botonReinicio = document.querySelector('button')

botonReinicio.addEventListener("click",function(){
  for (var casilla in casillas) {
    casillas[casilla].textContent = "";
  }
})

casillas[0].addEventListener("click",function(){cambiaValor(0)});
casillas[1].addEventListener("click",function(){cambiaValor(1)})
casillas[2].addEventListener("click",function(){cambiaValor(2)})
casillas[3].addEventListener("click",function(){cambiaValor(3)})
casillas[4].addEventListener("click",function(){cambiaValor(4)})
casillas[5].addEventListener("click",function(){cambiaValor(5)})
casillas[6].addEventListener("click",function(){cambiaValor(6)})
casillas[7].addEventListener("click",function(){cambiaValor(7)})
casillas[8].addEventListener("click",function(){cambiaValor(8)})

function cambiaValor(casilla){
  console.log(casilla);
  if (casillas[casilla].textContent == "") {
    casillas[casilla].textContent = "O"
  } else if (casillas[casilla].textContent == "O") {
    casillas[casilla].textContent = "X"
  } else if (casillas[casilla].textContent == "X"){
    casillas[casilla].textContent = ""
  }
}
