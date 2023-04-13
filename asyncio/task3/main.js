const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let k = 0;
const numbers = [];

rl.on('line', line => {
    let num = Number(line);
    let startN = 1;
    numbers.push(num);
    while (num > startN) {
        if (num / 3 === parseInt(num / 3)) num /= 3;
        else if (num / 2 === parseInt(num / 2)) num /= 2;
        else num -= 1;
        
        numbers.push(num);
        k += 1;
    }

    console.log(k);
    if (num <= 0) numbers = [1];
    console.log(numbers.reverse().join(' '));

    rl.close();
});