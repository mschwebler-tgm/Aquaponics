var express = require('express');
var router = express.Router();


server.listen(80);


/* GET home page. */
router.get('/', function(req, res, next) {
	res.render('authentication');
});
