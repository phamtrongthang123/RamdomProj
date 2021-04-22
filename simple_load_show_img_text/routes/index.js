var express = require('express');
var router = express.Router();
const fs = require('fs');

/* GET home page. 
choose the image file, click load => get id 
with id is index from image_list
*/
router.get('/', function(req, res, next) {
  image_list = req.image_list;
  // console.log(image_list);
  res.render('index', { title: 'Simple Demo', image_list, image_list_js: JSON.stringify(image_list)  });
});

/*
Get corresponding image file and text file with same id
*/
router.get('/:id', function(req, res, next) {
  const args_data = req.params;
  const id = args_data.id;
  image_list = req.image_list;
  text_list = req.text_list;
  // console.log(image_list);
  image_file = image_list[id];
  text_file = image_file.split('.')[0]
  if (text_list[id].includes(text_file)) {
    text_file = text_list[id];
  }
  else {
    for (var i = 0; i < text_list.length; i++) {
      if (text_list[i].includes(text_file)) {
        text_file = text_list[i];
        break;
      }
    }
  }
  var text_data = "";
  fs.readFile(text_file, 'utf8',(e, data) => {
    if (e) throw e;
    text_data=data;
    res.render('index_id', { title: 'Simple Demo', image_list, image_file, text_data, image_list_js: JSON.stringify(image_list) });
  });
});



module.exports = router;
