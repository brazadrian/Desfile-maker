const express = require('express');
const app = express();
const path = require('path');

const basePath = path.join(__dirname, "templates")

app.use(express.urlencoded({
    extend: true,
}))


app.use(express.json())


app.use(express.static('public'));

app.get('/', (req,res) => {
    res.sendFile(`${basePath}/principal.html`)
})

app.listen(3000, () => {console.log('Ta pegando')})