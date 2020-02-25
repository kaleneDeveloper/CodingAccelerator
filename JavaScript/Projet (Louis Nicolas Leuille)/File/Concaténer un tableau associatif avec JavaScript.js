let myArrayAssociative = {
    'prenom'    : 'Mark',
    'nom'       : 'Zuckerberg',
    'poste'     : 'PDG de Facebook'
};

function concat(array) {
    let string = "";

    for (const x in array) {
    
        string += (x + ' : ' + array[x] + '\n');
    
    }
    
    console.log(string);
}

concat(myArrayAssociative)