'use strict';

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(bodyParser.json());
app.use(express.static('../todo'));

var mysql = require('mysql');
var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'asd',
  database: 'todoapp',
});
con.connect();
// jo, filter nelkul:
// app.get('/todos', function (req, res) {
//   con.query('SELECT * FROM todos', function (err, rows) {
//     if (err) {
//       console.log(err.toString());
//       return;
//     }
//     res.send(JSON.parse(JSON.stringify(rows)));
//   });
// });

app.get('/todos', function (req, res) {
  var queryString = '';
  if (req.query.filter === 'checked') {
    queryString = 'SELECT * FROM todos WHERE completed = 0';
  } else {
    queryString = 'SELECT * FROM todos';
  }
  con.query(queryString, function (err, rows) {
    if (err) {
      console.log(err.toString());
      return;
    }
    res.send(JSON.parse(JSON.stringify(rows)));
  });
});

//
//
//   if (req.query.filter === 'checked') {
//     con.query('SELECT * FROM todos WHERE completed = 1', function (err, rows) {
//       if (err) {
//         console.log(err.toString());
//         return;
//       }
//       res.send(JSON.parse(JSON.stringify(rows)));
//     });
//   } else {
//   con.query('SELECT * FROM todos', function (err, rows) {
//     if (err) {
//       console.log(err.toString());
//       return;
//     }
//     res.send(JSON.parse(JSON.stringify(rows)));
//   });
//   }
// });


app.get('/todos/:id', function (req, res) {
  con.query('SELECT * FROM todos WHERE id = ?', req.params.id, function (err, rows) {
    if (err) {
      console.log(err.toString());
      return;
    }
    res.send(JSON.parse(JSON.stringify(rows)));
  });
});


app.post ('/todos', urlencodedParser, function (req, res) {
  con.query("INSERT INTO todos (text) VALUES ('"+req.body.text+"')", function (err, rows) {
    if (err) {
      console.log(err.toString());
      return;
    }
    res.send({ id: rows.insertId, text: req.body.text });
  });
});


app.put('/todos/:id', urlencodedParser, function (req, res) {
  con.query('UPDATE todos SET completed = 1 WHERE id = ?', req.params.id, function (err, rows) {
    if (err) {
      console.log(err.toString());
      return;
    }
    res.send({ id: rows.insertId, completed: true });
    // res.send({ id: req.param.id, completed: true });
  });
});


app.delete('/todos/:id', urlencodedParser, function (req, res) {
  con.query('DELETE FROM todos WHERE id = ?', req.params.id, function (err, rows) {
    if (err) {
      console.log(err.toString());
      return;
    }
    res.send({ id: req.param.id, destroyed: true });
  });
});

////FILTEEEER:
// app.get('/filter', function(req, res) {
//   con.query('SELECT * FROM todos WHERE completed = 1', function(err, rows) {
//     if (err) {
//       console.log(err.toString());
//       return;
//     }
//     console.log(rows);
//     res.send(JSON.parse(JSON.stringify(rows)));
//   });
// });



app.listen(3000);
