function addition(...numbers)  {
    let result = 0;
    numbers.forEach(number => {
        result += number;
       
    });
    console.log(result);
}

addition(2, 23, 4, 23, 23, 23 , 23);
