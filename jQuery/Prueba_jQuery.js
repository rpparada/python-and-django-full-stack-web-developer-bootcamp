var jugadas = []
for (var i = 0; i < 6; i++) {
  jugadas.push([0,0,0,0,0,0])
}

// 0 = nadie, 1= primero(azul), 2=segundo(rojo)
var turno = 1

// #C89B7B
var jugador1 = prompt("Jugador 1, Cual es tu nombre? Tu seras Azul:");
var jugador2 = prompt("Jugador 2, Cual es tu nombre? Tu seras Rojo:");

if (jugador1 === "") {
  jugador1 = "Anonimo Azul"
}

if (jugador2 === "") {
  jugador2 = "Anonimo Rojo"
}

$('h3').text(jugador1 + ": es tu turno, por favor elije una columna para marcar en azul.")

$('*[id*=col1]').click(function () {
  var pos = jugarTablero(0)
  if (pos > -1){
    if (turno == 1) {
      $('*[id*=col1]').eq(pos).css('background','red')
    } else {
      $('*[id*=col1]').eq(pos).css('background','blue')
    }
  }
})

$('*[id*=col2]').click(function () {
  var pos = jugarTablero(1)
  if (pos > -1){
    if (turno == 1) {
      $('*[id*=col2]').eq(pos).css('background','red')
    } else {
      $('*[id*=col2]').eq(pos).css('background','blue')
    }
  }
})

$('*[id*=col3]').click(function () {
  var pos = jugarTablero(2)
  if (pos > -1){
    if (turno == 1) {
      $('*[id*=col3]').eq(pos).css('background','red')
    } else {
      $('*[id*=col3]').eq(pos).css('background','blue')
    }
  }
})

$('*[id*=col4]').click(function () {
  var pos = jugarTablero(3)
  if (pos > -1){
    if (turno == 1) {
      $('*[id*=col4]').eq(pos).css('background','red')
    } else {
      $('*[id*=col4]').eq(pos).css('background','blue')
    }
  }
})

$('*[id*=col5]').click(function () {
  var pos = jugarTablero(4)
  if (pos > -1){
    if (turno == 1) {
      $('*[id*=col5]').eq(pos).css('background','red')
    } else {
      $('*[id*=col5]').eq(pos).css('background','blue')
    }
  }
})

$('*[id*=col6]').click(function () {
  var pos = jugarTablero(5)
  if (pos > -1){
    if (turno == 1) {
      $('*[id*=col6]').eq(pos).css('background','red')
    } else {
      $('*[id*=col6]').eq(pos).css('background','blue')
    }
  }
})

function jugarTablero(columna) {
  for (var casilla in jugadas[columna]) {
    if (jugadas[columna][casilla] === 0) {
      jugadas[columna][casilla] = turno
      verificaGanador(casilla)
      if (turno == 1) {
        turno = 2
        $('h3').text(jugador2 + ": es tu turno, por favor elije una columna para marcar en azul.")
      } else if (turno == 2) {
        turno = 1
        $('h3').text(jugador1 + ": es tu turno, por favor elije una columna para marcar en rojo.")
      }
      return casilla
      break
    }
  }
  return -1
}

function verificaGanador(posUltJugada) {
  var suma1 = 0
  var suma2 = 0
  for (var i = 0; i < 6; i++) {
    if (jugadas[i][posUltJugada] == 1) {
      suma1 += 1
    } else if (jugadas[i][posUltJugada] == 2) {
      suma2 += 1
    }
  }

  if (suma1 == 4) {
    prompt(jugador1 + " es el ganador");
  } else if (suma2 == 4) {
    prompt(jugador2 +" es el ganador");
  }

}
