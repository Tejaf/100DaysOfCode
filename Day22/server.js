var express = require('express');
var bodyParser = require('body-parser');
var nodemailer = require('nodemailer');

var app = express();

const PORT = process.env.PORT || 8001;
app.use(function(req, res, next) {
    console.log(`${req.method} for ${req.url} `)
    next()
});

app.use(express.static(__dirname + '/public'))

app.use(bodyParser.urlencoded( { extended: true }));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/send', function(req, res) {
    console.log(req.query)
    var smtpTransport = nodemailer.createTransport({
        service: "gmail",
        host: "smtp.gmail.com",
        auth: {
            user: "tmafonja1@gmail.com",
            pass: ""
        }
    });

    var mailOptions = {
        to: req.query.to,
        subject: req.query.subject,
        text: req.query.text
    }
    console.log(mailOptions);

    smtpTransport.sendMail(mailOptions, function(error, response) {
        if (error) {
            console.log(error);
            res.end("an error occured while sending this mail");
        } else {
            console.log( `Message send: ${response.message}`);
            res.end("sent")
        }
    })
});

app.listen(PORT, function() {
    console.log(`Express server listening on Port ${PORT}`);
})