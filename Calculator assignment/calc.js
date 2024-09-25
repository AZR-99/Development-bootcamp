function getNumbers() {
    var number1 = document.getElementById('firstnumber').value;
    var number2 = document.getElementById('secondnumber').value;
    return { number1: number1, number2: number2 };
}

function displayResult(result) {
    document.getElementById('result').value = result;
}

function add() {
    var numbers = getNumbers();
    var result = Number(numbers.number1) + Number(numbers.number2);
    displayResult(result);
}

function subtract() {
    var numbers = getNumbers();
    var result = Number(numbers.number1) - Number(numbers.number2);
    displayResult(result);
}

function multiply() {
    var numbers = getNumbers();
    var result = Number(numbers.number1) * Number(numbers.number2);
    displayResult(result);
}

