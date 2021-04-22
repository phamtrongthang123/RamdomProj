var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
// Setup livereload
const livereload = require("livereload");


var liveReloadServer = livereload.createServer();
liveReloadServer.watch(path.join(__dirname, "public"));
var connectLivereload = require("connect-livereload");

var app = express();


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hbs');


app.use(connectLivereload());
liveReloadServer.server.once("connection", () => {
    setTimeout(() => {
        liveReloadServer.refresh("/");
    }, 50);
});

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
// static path
// root
app.use(express.static(path.join(__dirname, 'public')));
// images
app.use('/imgs',express.static(path.join(__dirname, 'images_text/images')))
app.use('/texts',express.static(path.join(__dirname, 'images_text/texts')))

// get file list
const imgs_folder = './images_text/images/';
const texts_folder = './images_text/texts/';
const fs = require('fs');
const image_list = []
const text_list = []

fs.readdir(imgs_folder, (err, files) => {
  files.forEach(file => {
    // console.log(file);
    image_list.push(file);
  });
  // console.log(image_list)
});
fs.readdir(texts_folder, (err, files) => {
  files.forEach(file => {
    // console.log(file);
    text_list.push(texts_folder+file);
  });
  // console.log(text_list)
});


var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

app.use('/', function (req, res, next) {  
  req.image_list = image_list;
  req.text_list = text_list;
  next();
},indexRouter);
app.use('/users', usersRouter);



// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
