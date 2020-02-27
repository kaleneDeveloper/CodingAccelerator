// let myMap = new Map([
//     ['name', 'kalene;'],
//     ['lastName', 'A PIOU']
// ]);

// myMap.set('poste', 'PDG de facebook');
// myMap.delete('poste');

// console.log(myMap);

let utilisateurs = new Map();

utilisateurs.set('Mark Zuckerberg', {
    email: 'mark@facebook.com',
    poste: 'PDG',
});

utilisateurs.set('Bill Gates', {
    email: 'bill@gatesnotes.com',
    poste: 'Sauver le monde',
});

// utilisateurs.delete('Bill Gates');

console.log(utilisateurs);