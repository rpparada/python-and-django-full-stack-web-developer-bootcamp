/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!

///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop
// While Loop
var aux1 = 0
while (aux1<5) {
  console.log("Hello While");
  aux1++;
}
// For Loop
for (var aux2 = 0; aux2 < 5; aux2++) {
  console.log("Hello For");
}

/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
aux3 = 0
while (aux3 < 26) {
  if (aux3%2 != 0) {
    console.log("Odd number: "+aux3);
  }
  aux3++
}

// METHOD TWO
// For Loop
for (var aux4 = 0; aux4 < 26; aux4++) {
  if (aux4%2 != 0) {
    console.log("Odd number: "+aux4);
  }
}
