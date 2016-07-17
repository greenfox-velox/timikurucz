'use strict';

var inputField = document.querySelector('.input-text');
var addButton = document.querySelector('.add-button');
var todoContainer = document.querySelector('.todo-container');
// var host = 'https://mysterious-dusk-8248.herokuapp.com';
var host = 'http://localhost:3000';

function createOneNewTodo(todo) {
  var newLi = document.createElement('li');
  var newDiv = document.createElement('div');
  newDiv.classList.add('text');
  newDiv.textContent = todo.text;
  newLi.setAttribute('id', todo.id);
  newLi.appendChild(newDiv);
  todoContainer.appendChild(newLi);
  var newDivForButtons = document.createElement('div');
  newLi.appendChild(newDivForButtons);
  createDelButton(newDivForButtons, todo);
  createcheckButton(newDivForButtons, todo);
  clearTextbox();
}

function createAllTodos(input) {
  input.forEach(function (todo) {
    if(todo.destroyed === 0){
      createOneNewTodo(todo);
    }
  });
}

function createRequest(requestType, endPoint, dataToSend, cb)  {
  var xhr = new XMLHttpRequest();
  xhr.open(requestType, host + endPoint);
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
  xhr.onload = function () {
    if (cb !== null) {
      var response = JSON.parse(xhr.response);
      cb(response);
    }
  };
  xhr.send(dataToSend);
}

function clearTextbox() {
  var textBox = document.querySelector('.input-text');
  textBox.value = '';
}

function getAllTodos(p) {
  clearContent();
  createRequest('GET', p, null, createAllTodos);
}

getAllTodos('/todos');

function addTodo(p) {
  createRequest('POST', '/todos', JSON.stringify({ text: p }), createOneNewTodo)
}

addButton.addEventListener('click', function(){
  addTodo(inputField.value)
});


function createDelButton(parent, todo) {
  var del = document.createElement('button');
  del.classList.add('del-button');
  parent.appendChild(del);
  del.addEventListener('click', function (event) {
    delTodo(event, event.target.parentNode.parentNode.id);
  });
}


function deleteLi(event) {
  var ul = document.querySelector('ul');
  var itemToDel = document.getElementById(event.target.parentNode.parentNode.id);
  ul.removeChild(itemToDel);
}

function delTodo(event, delId) {
  var endPoint = '/todos/' + delId;
  createRequest('DELETE', endPoint, null, null);
  deleteLi(event);
}

function createcheckButton(parent, todo) {
  var check = document.createElement('button');
  if (todo.completed) {
    check.classList.add('checked-button');
  } else {
    check.classList.add('unchecked-button');
  }
  parent.appendChild(check);
  check.addEventListener('click', function (event) {
    checkTodo(event, event.target.parentNode.parentNode.id);
  });
}

function changeUncheckToCheckImg(input) {
  input.classList.remove('unchecked-button');
  input.classList.add('checked-button');
}

function checkLi(event) {
  var buttons = document.querySelectorAll('.unchecked-button, .checked-button');
  console.log(buttons);
  for (var i = 0; i <= buttons.length - 1; i++) {
    if ((buttons[i]).parentNode.parentNode.id === event.target.parentNode.parentNode.id) {
      changeUncheckToCheckImg(buttons[i]);
    }
  }
}

function checkTodo(event, checkId) {
  var endPoint = '/todos/' + checkId;
  var item = document.getElementById(checkId);
  var text = item.children[0].textContent;
  var textToSend = JSON.stringify({ text: text, completed: true });
  createRequest('PUT', endPoint, textToSend, null);
  checkLi(event);
}


function clearContent(){
  todoContainer.innerHTML = '';
}
var checkBox = document.querySelector('.cbox');

function displayCompletedTodos() {
  getAllTodos('/todos?filter=checked');
}

checkBox.addEventListener('click', function(event){
  if (checkBox.checked){
    displayCompletedTodos();
  } else {
    getAllTodos('/todos');
  }
});
