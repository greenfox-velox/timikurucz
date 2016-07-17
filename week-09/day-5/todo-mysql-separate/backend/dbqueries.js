'use strict';

var mysql = require('mysql');
var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'asd',
  database: 'todoapp',
});


con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

function handleError (err) {
  if(err) {
    console.log(err.toString());
    return;
  }
}

function getAllTodos (req, cb) {
  var queryString = 'SELECT * FROM todos';
  if (req.query.filter === 'incompleted') {
    queryString += ' WHERE completed = 0';
  }
  con.query(queryString, function (err, rows) {
    handleError(err);
    cb(rows);
  });
}

function getOneTodoItem(req, cb) {
  con.query('SELECT * FROM todos WHERE id = ?', req.params.id, function (err, rows) {
    handleError(err);
    cb(rows[0]);
  });
}

function addNewTodo(req, cb) {
  con.query("INSERT INTO todos (text) VALUES ('"+req.body.text+"')", function (err, rows) {
    handleError(err);
    cb({ id: rows.insertId, text: req.body.text });
  });
}

function updateOneTodo(req, cb) {
  con.query('UPDATE todos SET completed = 1 WHERE id = ?', req.params.id, function (err, rows) {
    handleError(err);
    cb({ id: rows.insertId, completed: true });
  });
}

function deleteOneTodo(req, cb) {
  con.query('DELETE FROM todos WHERE id = ?', req.params.id, function (err, rows) {
    handleError(err);
    cb({ id: req.param.id, destroyed: true });
  });
}


module.exports = {
  getAllTodos: getAllTodos,
  getOneTodoItem: getOneTodoItem,
  addNewTodo: addNewTodo,
  updateOneTodo: updateOneTodo,
  deleteOneTodo: deleteOneTodo
}
