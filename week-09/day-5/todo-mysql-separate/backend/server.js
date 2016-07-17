'use strict';

var express = require('express');
var app = express();

var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

app.use(bodyParser.json());
app.use(express.static('../todo'));

var dbQueries = require('./dbqueries');


app.get('/todos', function (req, res) {
  dbQueries.getAllTodos(req, function(rows){
    res.send(rows);
  });
});


app.get('/todos/:id', function (req, res) {
  dbQueries.getOneTodoItem(req, function(rows){
    res.send(rows);
  });
});

app.post('/todos', urlencodedParser, function(req, res) {
  dbQueries.addNewTodo(req, function(rows){
    res.send(rows);
  });
});

app.put('/todos/:id', urlencodedParser, function(req, res) {
  dbQueries.updateOneTodo(req, function(rows){
    res.send(rows);
  });
});

app.delete('/todos/:id', urlencodedParser, function (req, res) {
  dbQueries.deleteOneTodo(req, function(rows){
    res.send(rows);
  });
});

app.listen(3000);
