let listOfCountry = ['France', 'Belgian', 'Japan', 'Morocco'];

for (const x of listOfCountry) { 
    console.log(x);
};

listOfCountry.forEach(function(country) {
    console.log(country);
});

listOfCountry.forEach(country => console.log(country));
