var nombre = prompt("Dame tu primer nombre :");
var apellido = prompt("Dame tu apellido :");
var edad = prompt("Dame tu edad :")
var estatura = prompt("Dame tu estatura :")
var mascota = prompt("Dame el nombre de tu mascota :")

if (nombre[0].toUpperCase() == apellido[0].toUpperCase()){
  console.log("Primera condicion cumplida");
  if (edad >= 20 && edad <= 30){
    console.log("Segunda condicion cumplida");
    if (estatura >= 170){
      console.log("Tercera condicion cumplida");
      if (mascota[mascota.length-1] == 'y'){
        console.log("Cuarta condicion cumplida");
      }
    }
  }
}
