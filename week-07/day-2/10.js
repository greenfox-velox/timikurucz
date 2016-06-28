'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  gradeList: [],
  addGrade: function (grade) {
    this.gradeList.push(grade);
  },

  getAverage: function () {
    var summ = 0;
    this.gradeList.forEach(function (e) {
      summ += e;
    });
    var average = summ / this.gradeList.length;
    return average;
  }
};

student.addGrade(5);
student.addGrade(3);
student.addGrade(5);
console.log(student.gradeList);
console.log(student.getAverage());
