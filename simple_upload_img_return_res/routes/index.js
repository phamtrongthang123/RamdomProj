var express = require('express');
var router = express.Router();
var multer  = require('multer');


var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, __dirname + '/uploads')      //you tell where to upload the files,
  },
  filename: function (req, file, cb) {
    cb(null, file.fieldname + '-' + Date.now() + '.png')
  }
})

var upload = multer({storage: storage,
    onFileUploadStart: function (file) {
      console.log(file.originalname + ' is starting ...')
    },
});

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Simple Demo' });
});

router.post('/profile', upload.single('myimage'), function (req, res, next) {
  // req.file is the `avatar` file
  console.log(req.file);
  return false;
})


module.exports = router;
