// function predictAge() {

//     let age = prompt("What is your age ? : ");
//     // age = parseInt(age);
//     age = Number(age);
//     alert("Soon you will have " + (age + 1) + " years !" );

// }

// predictAge();


// function abracadabra() {
//     let name = prompt("What is your name ? :"), lastName = prompt("Your last name ? :"), age = Number(prompt("And your age ? :"));
    
//     alert("Sapristi ! On ne m'avait pas prévenu que c'était vous, " 
//         + name 
//         + "! Euh... Je veux dire... Monsieur le grand magicien " 
//         + lastName 
//         + " ! Cela fait déjà " 
//         + age  
//         + " ans que vous faites rayonner notre contrée !");

// }

// abracadabra();

let weight = parseFloat(prompt("Please insert your weigth (in kg) :"));
let size = parseFloat(prompt("Please insert your size (in cm) :"));

function calculIMC(weight, size) {
    
    let IMC = weight/(size/100)**2;
    // let IMC = weight/Math.pow((size/100), 2);
    return "Your IMC is " + IMC + ".";

}

alert(calculIMC(weight, size));