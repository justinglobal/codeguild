"use strict";

// need a return value for functions (think of them as sub-programs)

var totalIncome = 160000;
var totalTax = 0;

var computeBracket1 = function(totalIncome) {
  if (totalIncome > 3351) {
    totalTax = 167.5;
  } else {
   totalTax = .05 * totalIncome;
  }
};
var computeBracket2 = function(totalIncome) {
  if (totalIncome > 8401) {
    totalTax += 353.5;
  } else if (totalIncome > 3350) {
    totalTax += .07 * (totalIncome - 3350);
  }
};
var computeBracket3 = function(totalIncome) {
  if (totalIncome > 125000) {
    totalTax += 10494;
  } else if (totalIncome > 8400) {
    totalTax += .09 * (totalIncome - 8400);
  }
};
var computeBracket4 = function(totalIncome) {
  if (totalIncome > 125000) {
    totalTax += .099 * (totalIncome - 125000);
  }
};
computeBracket1(totalIncome);
computeBracket2(totalIncome);
computeBracket3(totalIncome);
computeBracket4(totalIncome);

console.log(totalIncome);
console.log(totalTax);
