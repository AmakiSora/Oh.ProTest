const express = require('express')
const app = express()
const port = 8000

app.get('/helloworld', (req, res) => {
    res.send('HelloWorld')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})