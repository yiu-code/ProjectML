const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.render("index")
});


//needed to export everything of this file to app.js 
module.exports = router;