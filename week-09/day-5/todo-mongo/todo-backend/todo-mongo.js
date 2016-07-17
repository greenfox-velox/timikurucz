'use strict';

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(bodyParser.json());
app.use(express.static('../todo'));

var mongodb = require('mongodb');
var MongoClient = mongodb.MongoClient;
var ObjectID = require('mongodb').ObjectID;

// Connection URL. This is where your mongodb server is running.
var url = 'mongodb://localhost:27017/todos';

// Use connect method to connect to the Server
MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    console.log('Connection established to', url);

    var collection = db.collection('todos');

    app.get('/todos', function (req, res) {
      var p = {};
      if (req.query.filter === 'checked') {
        p = { 'completed':0 };
      }
      collection.find(p,{'_id':1, 'text':1, 'completed':1, 'destroyed':1}).toArray(function (err, result) {
        if (err) {
          console.log(err);
          return;
        }
        res.send(result);
      });
    });

    app.get('/todos/:id', function (req, res) {
       collection.find({'_id': ObjectID(req.params.id)}, {'text': 1, '_id': 1}).toArray(function (err, result) {
         if (err) {
           console.log(err);
           return;
         }
         res.send(result);
       });
     });

app.post ('/todos', urlencodedParser, function (req, res) {
  var  newTodo = {
    'text' : req.body.text,
    'completed' : 0,
    'destroyed' : 0,
  }
  collection.insert(newTodo, function (err, result) {
    if (err) {
      console.log(err);
      return;
    }
    res.send(newTodo);
  });
});

app.put('/todos/:id', urlencodedParser, function (req, res) {
  collection.update({'_id': ObjectID(req.params.id)}, {$set:{'completed': 1}}, function (err, result) {
    if (err) {
      console.log(err);
      return;
    }
    res.send({'_id': ObjectID(req.params.id), 'completed':1});
  });
});

app.delete('/todos/:id', urlencodedParser, function (req, res) {
  collection.update({'_id': ObjectID(req.params.id)}, {$set:{'destroyed': 1}}, function (err, result) {
    if (err) {
      console.log(err);
      return;
    }
    res.send({'_id': ObjectID(req.params.id), 'destroyed':1});
  });
});

     app.listen(3000);
  }
});
