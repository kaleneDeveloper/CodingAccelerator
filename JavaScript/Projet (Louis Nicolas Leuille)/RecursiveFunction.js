function sum(number) {

    if(number > 0) {
        
        console.log(number);
        sum(number - 1);
    }
    else {
        console.log(number);
    }
}

sum(5);
// 
function sum(number) {

    if(number == 1) {
        return 1;
    }
    else {
        return number + sum(number - 1);
    }
    
}
console.log(sum(5));

