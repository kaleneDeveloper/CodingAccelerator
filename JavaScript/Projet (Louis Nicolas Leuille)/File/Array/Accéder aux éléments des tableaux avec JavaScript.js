// let monTableau = new Array('un', 'deux', 'trois');
// let monTableau = Array('un', 'deux', 'trois');
let monTableau = ['un', 'deux', 'trois', 'quatre'];

// console.log(monTableau[0])
console.log(monTableau[monTableau.length - 1]);

// let monTableau2D = new Array(
//     Array('Mark', 'Jeff', 'Bill'),
//     Array('Zuckerberg', 'Bezos', 'Gates')  
// );

let monTableau2D = [
    ['Mark', 'Jeff', 'Bill'],
    ['Zuckerberg', 'Bezos', 'Gates']
];

console.log(monTableau2D[1][2]);

let monTableauAssociatif = {
    'prenom' : 'Mark',
    'nom'    : 'Zuckerberg',
    'poste'  : 'PDG de Facebook'
};

console.log(monTableauAssociatif['poste']);