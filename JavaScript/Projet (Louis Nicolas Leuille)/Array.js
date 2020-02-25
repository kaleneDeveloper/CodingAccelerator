let myArray = ['un', 'deux', 'trois', 'quatre'];
myArray.push("cinq")
myArray.unshift("zero")
console.log(myArray);


let myArrayAssociative = {
        'Prenom' : 'Kalene',
        'Nom'    : 'A PIOU',
        'Post'   : 'Dev'
    };
    myArrayAssociative['Nationality'] = 'French';
    // console.log(myArrayAssociative);
    
    // let myArray = ['un', 'deux', 'trois', 'quatre'];
    // myArray.splice(2,2);
    // console.log(myArray);
    
    let myArray = ['un', 'deux', 'trois', 'quatre'];
    console.log(myArray.join(', '));
    
let myArray2D = [
    ['Kalene', 'Apiou', 'Alexis'],
    ['tsyus', 'jane','roter']
];
myArray2D.splice(2, 0, ['test','test2'])
myArray2D.push(['test','test2'])
console.log(myArray2D);

