// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT
function add(name){
  roster.push(name)
}
// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT
function remove(name){
  if (roster.indexOf(name) > -1) {
    roster.splice(roster.indexOf(name),1);
  }
}
// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display(){
  roster.forEach(function(elemento){
    console.log(elemento)});
}
// Start by asking if they want to use the web app
var mensaje = prompt("Quieres utilizar esta aplicacion web? (usa 'y' para usar):");
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if (mensaje == 'y'){
  while (mensaje != 'salir') {
    mensaje = prompt("Quieres sumar, quitar, desplegar o salir");
    if (mensaje == "sumar"){
      var alumno = prompt("A quien quieres sumar?");
      add(alumno);
    } else if (mensaje == "quitar"){
      var alumno = prompt("A quien quieres quitar?");
      remove(alumno);
    } else if (mensaje == "desplegar") {
      display();
    } else if (mensaje == "salir") {
      break;
    }
  }
}
