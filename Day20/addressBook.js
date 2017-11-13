// muse from ipaye's code of consonance 100_days_of_code

const fs = require('fs');

function main() {
    process.stdout.write(`\n
    ---------------------------------------------------------
    Welcome to the phonebook app.

    Enter Your Contact Information in this sequesnce
    FullName-PhoneNumber-Address

    Example
    Please enter your details: Afonja Tejumade - 080XXXXXXX - Gbagada
    ---------------------------------------------------------
    Please Enter your details: `);

    process.stdin.on('data', function(data) {
        let response = data.toString().trim();
        let status = addToPhoneBook(response);
        console.log('You Added => ', status);
        process.exit();
    })
}

function addToPhoneBook(details) {
    let info = details.split('-');
    let addressDetails = [];
    info.forEach(function(field) {
        let detail = field.trim();
        addressDetails.push(field);
    });

    let contactInfo = `
        Name: ${addressDetails[0]}
        phoneNumber: ${addressDetails[1]}
        Address: ${addressDetails[2]}
        `;

        fs.appendFileSync('phoneBook.txt', contactInfo, 'utf-8', function(err) {
            if (err) console.log('Oops! something went wrong, can\'t add details');
            console.log('Your contact information was successfully added to file');
        })
        return contactInfo;
}

main();