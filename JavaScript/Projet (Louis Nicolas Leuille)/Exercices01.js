// First methode
// try {
//     do {

//         var choose = Number(prompt("What do you want to do ? : \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division"));

//         if(choose != "" && choose != null && choose != 1 && choose != 2 && choose != 3 && choose != 4) {
            
//             alert(choose + " is not defined \nChoose : \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division");

//         }

//     } while(choose != 1 && choose != 2 && choose != 3 && choose != 4)

//     switch(choose) {
//         case 1:
//             firstNumer  = parseFloat(prompt("Enter your first number:"));
//             secondNumber = parseFloat(prompt("Enter your second number:"));
//             resultat = firstNumber + secondNumber;
//             alert("Your resultat is " + firstNumber + "+" + secondNumber + " = " + resultat);
//             break;
//         case 2:
//             firstNumer  = parseFloat(prompt("Enter your first number:"));
//             secondNumber = parseFloat(prompt("Enter your second number:"));
//             resultat = firstNumber - secondNumber;
//             alert("Your resultat is " + firstNumber + "-" + secondNumber + " = " + resultat);
//             break;
//         case 3:
//             firstNumer  = parseFloat(prompt("Enter your first number:"));
//             secondNumber = parseFloat(prompt("Enter your second number:"));
//             resultat = firstNumber * secondNumber;
//             alert("Your resultat is " + firstNumber + "*" + secondNumber + " = " + resultat);
//             break;
//         case 4:
//             firstNumer  = parseFloat(prompt("Enter your first number:"));
//             secondNumber = parseFloat(prompt("Enter your second number:"));
//             resultat = firstNumber / secondNumber;
//             if (resultat == Infinity) {
//                 alert("Your resultat is " + firstNumber + "/" + secondNumber + " = 0");
//             }
//             else {
//             alert("Your resultat is " + firstNumber + "/" + secondNumber + " = " + resultat);
//             }
//             break;
//         default:
//             throw new Error(error);
//     }
// }
// catch(error) {
//     alert(choose + " is not defined \nChoose : \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division");
// }

//Second methode

do {

    var redoCalcul = true;

    try {
        function Addition(numberA, numberB) {
            return numberA + numberB;
        }
        function Multiplication(numberA, numberB) {
            return numberA * numberB;
        }
        function Substraction(numberA, numberB) {
            return numberA - numberB;
        }
        function Division(numberA, numberB) {
            return numberA / numberB;
        }
        do {
            var choose = Number(prompt("What do you want to do ? : \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division"));

            if(choose != "" && choose != null && choose != 1 && choose != 2 && choose != 3 && choose != 4) 
                alert(choose + " is not defined \nChoose : \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division");

        } while(choose != 1 && choose != 2 && choose != 3 && choose != 4)

        do {
            var firstNumber  = Number(prompt("Enter your first number:"));
            var secondNumber = "";
            while(secondNumber == 0) {
                var secondNumber = Number(prompt("Enter your second number:"));
                if(choose != 4) {break;}
                if(secondNumber == 0 && choose == 4) {
                    alert("You cannot divide by 0.");
                }
            }
        } while(isNaN(firstNumber) || isNaN(secondNumber))


        switch (choose) {
            case 1:
                var resultat = Addition(firstNumber, secondNumber)
                break;
            case 2:
                var resultat = Substraction(firstNumber, secondNumber)
                break;
            case 3:
                var resultat = Multiplication(firstNumber, secondNumber)
                break;
            case 4:
                var resultat = Division(firstNumber, secondNumber)
                break;
            default:
                throw new Error(error);
        }


    }
    catch(error) {
        alert(choose + " is not defined \nChoose : \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division");
    }

    if(choose == 1)  {
        alert("Your resultat is " + firstNumber + "+" + secondNumber + " = " + resultat);
    }
    else if(choose == 2) {
        alert("Your resultat is " + firstNumber + "-" + secondNumber + " = " + resultat);
    }
    else if(choose == 3) {
        alert("Your resultat is " + firstNumber + "*" + secondNumber + " = " + resultat);
    }
    else if(choose == 4) {
        if (resultat == Infinity) {
            alert("Your resultat is " + firstNumber + "/" + secondNumber + " = 0");
        }
        else {
        alert("Your resultat is " + firstNumber + "/" + secondNumber + " = " + resultat);
        }
    }

    if(confirm("Would you like to redo a calculation ?")) {
        var redoCalcul = true;
    }
    else {
        var redoCalcul = false;
    }

} while(redoCalcul == true)