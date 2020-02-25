let basket = ['strawberry', 'banana', 'apple'];

for (const x in basket) {
    console.log(basket[x]);
}

for (const x in basket) {
    basket[x] = 'Green';
}

console.log(basket);