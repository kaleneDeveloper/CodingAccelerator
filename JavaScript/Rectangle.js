const fs = require('fs')

// const c1 = fs.readFileSync("./"+process.argv[2],"utf8").split('\n')
// const c2 = fs.readFileSync("./"+process.argv[3],"utf8").split('\n')

fs.readFile("./"+"c1.txt", 'utf8', function(err, contents) {
    console.log(contents);
});
fs.readFile("./"+"c2.txt", 'utf8', function(err, contents) {
    console.log(contents);
});

var contents = fs.readFileSync("./"+"c1.txt", 'utf8');
console.log(contents);

var contents = fs.readFileSync("./"+"c2.txt", 'utf8');
console.log(contents);

