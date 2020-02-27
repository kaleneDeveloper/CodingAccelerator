let carA = {
    builder: 'Tesla',
    modele: 'Cybertruck'
};
let carB = {
    builder: 'Renault',
    modele: 'Espace'
};

// car.add(carA);
let car = new WeakSet([carA, carB]);
console.log(car);



let voitureA = {
    constructeur: 'Tesla',
    modele: 'Cybertruck'
  }
  let voitureB = {
    constructeur: 'Renault',
    modele: 'Espace'
  }
  
  let voitures = new WeakSet([voitureA, voitureB]);
  console.log(voitures);