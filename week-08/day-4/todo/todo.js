'use strict';

var inputField = document.querySelector('.input-text');
var addButton = document.querySelector('.add-button');
var todoContainer = document.querySelector('.todo-container');
var host = 'https://mysterious-dusk-8248.herokuapp.com';

function createOneNewTodo(todo) {
  var newItem = document.createElement('li');
  newItem.textContent = todo.text;
  newItem.setAttribute('id', 'l' + todo.id);
  todoContainer.appendChild(newItem);
  createDelButton(newItem, todo);
  createcheckButton(newItem, todo);
}


function createAllTodos(input) {
  input.forEach(function(todo) {
    createOneNewTodo(todo);
  })
}

function getTodos() {
  var xhr = new XMLHttpRequest();
  var endPoint = '/todos'
  xhr.open('GET', host + endPoint);
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
  xhr.onload = function() {
    var response = JSON.parse(xhr.response);
    createAllTodos(response);
    };
  xhr.send();
}
getTodos();

function addTodo() {
  var xhr = new XMLHttpRequest();
  var endPoint = '/todos'
  xhr.open('POST', host + endPoint);
  xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
  var textToSend = JSON.stringify({ text: inputField.value });
  xhr.onload = function() {
    var response = JSON.parse(xhr.response);
    createOneNewTodo(response);
  };
  xhr.send(textToSend);
}

addButton.addEventListener('click', addTodo);


function createDelButton(parent, todo) {
  var del = document.createElement('button');
  del.classList.add('del-button');
  del.setAttribute('id', 'd' + todo.id);
  parent.appendChild(del);
  del.addEventListener('click', function(event){
    delTodo(event, del.id);
  });
}

function deleteLi(event){
  var ul = document.querySelector('ul');
  var proba = document.querySelector('#l' + event.target.id.slice(1,10));
  ul.removeChild(proba);
}

function delTodo(event, id) {
  var xhr = new XMLHttpRequest();
  var serverId = event.target.id.slice(1, 10);
  var endPoint = '/todos/' + serverId;
  xhr.open('DELETE', host + endPoint);
  xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
  xhr.onload = function() {
    deleteLi(event);
  };
  xhr.send();
}

function createcheckButton(parent, todo) {
  var check = document.createElement('button');
  if (todo.completed) {
    check.classList.add('checked-button');
  } else {
    check.classList.add('unchecked-button');
  }
  parent.appendChild(check);
  check.setAttribute('id', parent.id);
  check.addEventListener('click', function(event){
    checkTodo(event, check.id);
  });
}

function changeUncheckToCheckImg(input) {
  input.classList.remove('unchecked-button');
  input.classList.add('checked-button');
}


function checkLi(event){
  var buttons = document.querySelectorAll('.unchecked-button');
  for (var i = 0; i <= buttons.length - 1; i++) {
    if ((buttons[i]).id === event.target.id) {
      changeUncheckToCheckImg(buttons[i]);
    }
  }
}

function getText(id){
  var allLi = document.querySelectorAll('ul > li');
  console.log(allLi);
  for (var i = 0; i <= allLi.length - 1; i++) {
    if ((allLi[i]).id === event.target.id) {
      return (allLi[i]).textContent;
    }
  }
}

function checkTodo(event, id) {
  var xhr = new XMLHttpRequest();
  var serverId = event.target.id.slice(1,10);
  var endPoint = '/todos/' + serverId;
  console.log(endPoint);
  var blabla = document.querySelector('#l' + serverId);
  var textToSend = JSON.stringify({ text: getText(blabla), completed: true });
  xhr.open('PUT', host + endPoint);
  xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
  xhr.onload = function() {
    checkLi(event);
  };
  xhr.send(textToSend);
}
