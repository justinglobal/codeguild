"use strict";


var intsToSearch = [1, 0, 1, 2];
var sumToUse = [3]

var sumPairs = []

var find_sum_pairs = function(intsToSearch , sumToUse) {
  var funcPosition = 0
  while funcPosition <= (intsToSearch.lenght - 1)
    for intsToSearch.range[-1]; {
      if (intsToSearch[funcPosition] + intsToSearch[funcPosition + 1])
        === sumToUse
        return sumPairs.push(intsToSearch[funcPosition] , intsToSearch[funcPosition +1] )
        return funcPosition += 1
      else (intsToSearch[funcPosition] + (intsToSearch[funcPosition] + 1))
       !== sumToUse {
        return funcPosition += 1
      }
    }
};

console.log(find_sum_pairs(intsToSearch, sumToUse));

// var find_sum_pairs = function(intsToSearch , sumToUse) {
//   return intsToSearch[3] / sumToUse;
// };
