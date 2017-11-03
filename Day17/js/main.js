let input = document.getElementById("input");
let inputUnit = document.getElementById(("unit"));
let convertBtn = document.getElementById(("convert"));
let result = document.getElementById(("result"));

function celsiusToFahrenheit(c) {
    let f = (c * 9.0/5 ) + 32;
    return f.toFixed(2)
}

function fahrenheitToCelsius(f) {
    let c = (f - 32) * 5.0/9;
    return c.toFixed(2)
}

convertBtn.addEventListener('click', function () {

    let inputValue = input.value;
    let inputUnitValue = inputUnit.options[inputUnit.selectedIndex].value;

    if (parseFloat(inputValue) === 0 || parseFloat(inputValue)) {
        if(inputValue) {
            if (inputUnitValue === '°C') {
                let answer = celsiusToFahrenheit(inputValue);
                result.innerHTML = String(answer) + "<span class='unit'>°F</span>";
            } else if (inputUnitValue === '°F') {
                let answer = fahrenheitToCelsius(inputValue);
                result.innerHTML = String(answer) + "<span class='unit'> °C </span>";
            }
        }

    } else {
        result.innerHTML = "<span>Hey! you can only convert numbers e.g 12</span>"
    }

    event.preventDefault();
});