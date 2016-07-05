'use strict';

// Automated CarPark system
//
// All the dates in this examples should be stored as a number
// The milliseconds lasted from 1970-01-01
//
// Create a Car constructor
// it should take 3 parameters
//  - type: the cars type as a string (eg: 'volvo')
//  - color: the cars type as a string (eg: 'red')
//  - balance: the cars parking credis as a number (eg: 500)

function Car(type, color, balance) {
  this.type = type;
  this.color = color;
  this.balance = balance;
  this.lastEnterDate = 0;
  this.id = Car.ids;
  Car.ids ++;
}

// every car should have an id property (a number), that is
// unique for all the cars, starting form 0
Car.ids = 0;


// Methods:
// enter(enterDate) - it should store the date of entering
Car.prototype.enter = function (enterDate) {
  this.lastEnterDate = enterDate;
};

// getEnterDate() - it should return the date of the last entering
Car.prototype.getEnterDate = function () {
  return this.lastEnterDate;
};

// leave(price) - it should decrease the balance with the price of the parking (that is given in an argument)
Car.prototype.leave = function (price) {
  this.balance -= price;
  return this.balance;
};

// getStats() - it should give back a string like:
// "Type: volvo, Color: red, Balance: 500"
Car.prototype.getStats = function () {
  return ('Type: ' + this.type + ', Color: ' + this.color + ', Balance: ' + this.balance);
};

// Create a CarPark constructor. it should take 2 parameters
//  - income: the initial credits as a number (eg: 4000)
//  - startTime: the current date
function CarPark(income, startTime) {
  this.income = income;
  this.startTime = startTime;
  this.parkingFee = 40;
  this.carsList = [];
}

// The parking fee: 40 per hours (only every whole hour)

// Methods:
// carEnter(car) - It should add a car to the garage and add its stored startTime
CarPark.prototype.carEnter = function (car) {
  car.enter(this.startTime);
  this.carsList.push(car);
};

CarPark.prototype.calculateParkingFee = function (car) {
  var enterTime = car.getEnterDate();
  var currentTime = this.startTime;
  var hours = Math.floor((currentTime - enterTime) / 3600000);
  var fee = hours * this.parkingFee;
  return fee;
};

// carLeave(id) - It should remove the car with the given id and it should charge from its balance
CarPark.prototype.carLeave = function (givenId) {
  for (var i = 0; i < this.carsList.length; i++) {
    if (this.carsList[i].id === givenId) {
      var wholeParkingFee = this.calculateParkingFee(this.carsList[i]);
      console.log(wholeParkingFee);
      this.carsList[i].leave(wholeParkingFee);
      this.income += wholeParkingFee;
      this.carsList.splice(i, 1);
    }
  }
};

// elapseTime(hours) - It should increment the time with the hours
CarPark.prototype.elapseTime = function (hours) {
  this.startTime += hours * 3600000;
};

// Optional Methods:
// getStats()
//  - It should return a string like:
//    "Cars: 4, Time: 1234423453, Income: 1400"
CarPark.prototype.getStats = function () {
  return ('Cars: ' + this.carsList.length + ', Time: ' + Date.now() + ', Income: ' + this.income);
};

var car1 = new Car('volvo', 'black', 500);
var car2 = new Car('lada', 'white', 600);
var car3 = new Car('mustang', 'black', 2500);

var garage = new CarPark(100, Date.now());
garage.carEnter(car1);
garage.carEnter(car2);
garage.carEnter(car3);
console.log(car1.id);
console.log(car2.id);
console.log(car3.id);
console.log(car2.balance);
console.log(garage.income);
console.log(garage.carsList);

garage.elapseTime(5);

garage.carLeave(2);
console.log(car2.balance);
console.log(garage.income);
console.log(garage.carsList);

console.log(garage.getStats());

// Optional Methods:
//
// getParkingCarsSince(hours)
//  - It should return the number of cars that are parking since the given hours
