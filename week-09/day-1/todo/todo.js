'use strict';

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(bodyParser.json());

var todoId = 3;

var todosList = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }];


function getTodos() {
  return (todosList);
}

app.get('/todos', function(req, res) {
  res.send(getTodos());
})

function getOneTodo(itemId) {
  for (var i = 0; i < todosList.length; i ++){
    if (parseInt(todosList[i].id) === parseInt(itemId)) {
      return todosList[i];
    }
  }
}

//with filter:
// function getOneTodo(itemId){
//   return (todosList.filter(function(e) {
//     if (parseInt(e.id) === parseInt(itemId)) {
//       return e;
//     }
//   }));
// }

app.get('/todos/:id' , function(req, res) {
  res.send(getOneTodo(req.params.id));
})

function addTodo(input) {
  todoId ++;
  var newItem = {"completed": false, "id": todoId, "text": input};
  todosList.push(newItem);
  // console.log(newItem);
  return newItem;
}

app.post ('/todos', urlencodedParser, function(req, res) {
  // console.log(req.body.text);
  // console.log(req.body);
  res.send(addTodo(req.body.text));
})

function checkOneTodo(itemId, newText) {
  for (var i = 0; i < todosList.length; i ++){
    if (parseInt(todosList[i].id) === parseInt(itemId)) {
      todosList[i].completed = true;
      todosList[i].text = newText;
      return todosList[i];
    }
  }
}

//with filter:
// function checkOneTodo(itemId, newText) {
//   return (todosList.filter(function(e) {
//       if (parseInt(e.id) === parseInt(itemId)) {
//         e.completed = true;
//         e.text = newText;
//         return e;
//       }
//     }));
// }

app.put ('/todos/:id', urlencodedParser, function(req, res) {
  res.send(checkOneTodo(req.params.id, req.body.text));
})


function delOneTodo(itemId) {
  for (var i = 0; i < todosList.length; i ++){
    if (parseInt(todosList[i].id) === parseInt(itemId)) {
      todosList[i].destroyed = true;
      return todosList.splice(i, 1)[0];
    }
  }
}

//with filter:
// function delOneTodo(itemId) {
//   todosList.filter(function(e) {
//     if (parseInt(e.id) === parseInt(itemId)) {
//       e.destroyed = true;
//       todosList.splice(todosList.indexOf(e), 1);
//       return e;
//     }
//   });
// }


app.delete ('/todos/:id', urlencodedParser, function(req, res) {
  res.send(delOneTodo(req.params.id));
});

// app.delete('/todos/:id', urlencodedParser, function(req, res) {
//   if (err) {
//     res.status(404);
//   } else {
//     res.send(delOneTodo(req.params.id));
//   }
// });


app.listen(3000);
