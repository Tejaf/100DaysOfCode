function fitAnswerToScreen (answer) {
    var ansText = answer.innerHTML;
    const answerFontSize = 60;
    if (ansText.length > 10 && ansText.length <= 30) {
        var newFont = String((answerFontSize * 10) / ansText.length + 'px');
        answer.style.fontSize = newFont ;
    } else  if (ansText.length > 30) {
        answer.style.fontSize = '23px' ;
    } else  {
        answer.style.fontSize = answerFontSize;
    }
}


var keys = document.querySelectorAll('#calculator button');
var answer = document.getElementById('answer');
var operators = ['+', '-', 'x', '÷', '%'];
var decimalAdded = false;
var evalClicked = false;



for(var i = 0; i < keys.length; i++) {
    keys[i].onclick = function(e) {

        // Get the input and button values
        var input = document.querySelector('#answer');
        var inputVal = input.innerHTML;
        var btnVal = this.innerHTML;

        fitAnswerToScreen(input);

        if (operators.indexOf(btnVal) === -1 && btnVal !== 'AC' && inputVal === '0') {
            console.log('hi');
            input.innerHTML = btnVal;

        } else if(btnVal === 'AC') {
            input.innerHTML = '0';
            decimalAdded = false;
        }

        else if(btnVal === '=') {
            var equation = inputVal;
            let lastChar = equation[equation.length - 1];

            equation = equation.replace(/x/g, '*').replace(/÷/g, '/');

            if(operators.indexOf(lastChar) > -1 || lastChar === '.')
                equation = equation.replace(/.$/, '');

            if(equation) {
                input.innerHTML = eval(equation);
                evalClicked = true;
            }

            decimalAdded = false;
        }

        // indexOf works only in IE9+
        else if(operators.indexOf(btnVal) > -1) {
            // Operator is clicked
            // Get the last character from the equation
            let lastChar = inputVal[inputVal.length - 1];

            // Only add operator if input is not empty and there is no operator at the last
            if(inputVal !== '' && operators.indexOf(lastChar) === -1)
                input.innerHTML += btnVal;

            // Allow minus if the string is empty
            else if(inputVal === '' && btnVal === '-')
                input.innerHTML += btnVal;

            // Replace the last operator (if exists) with the newly pressed operator
            if(operators.indexOf(lastChar) > -1 && inputVal.length > 1) {
                input.innerHTML = inputVal.replace(/.$/, btnVal);
            }
            decimalAdded =false;
            evalClicked = false;
        }

        else if(btnVal === '.') {
            if(!decimalAdded) {
                input.innerHTML += btnVal;
                decimalAdded = true;
            }
        }

        else {
            if (btnVal && evalClicked && operators.indexOf(btnVal) === -1 && btnVal !== 'AC') {
                input.innerHTML = btnVal;
                decimalAdded = false;
                evalClicked = false;

            } else if (operators.indexOf(btnVal) > -1) {
                input.innerHTML += btnVal;decimalAdded = false;
                evalClicked = false;

            } else {
                input.innerHTML += btnVal;
            }

        }

        // prevent page jumps
        e.preventDefault();
    }
}