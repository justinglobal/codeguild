var namesToAges = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
};

var agesOnly = [];
// makes array of only ages
for (var key in namesToAges) {
  var value = namesToAges[key];
  agesOnly.push(value);
};
console.log(agesOnly);

// makes Object of age:count for key:value
var agesToCount = { };
for(var i = 0; i < agesOnly.length; i += 1) {
    if(!agesToCount[agesOnly[i]])
        agesToCount[agesOnly[i]] = 0;
    agesToCount[agesOnly[i]] += 1;
};
console.log(agesToCount);
// var agesToCount = { 20:3, 22:2, 25:4 };

// makes Array of only counts
var onlyCounts = Object.keys(agesToCount).map(function ( key ) {
  return agesToCount[key];
});
// gets lowest value of only Counts
var minOccur = Math.min.apply( null, onlyCounts );

// for (var key in agesToCount) {
//     if agesToCount[key] === minOccur;

// var finalAge = agesToCount[minOccur];

//notice: this gives the value of the highest age, not the key
console.log(minOccur);

// see:
// http://codereview.stackexchange.com/questions/51053/get-the-key-of-the-highest-value-in-javascript-object
// http://stackoverflow.com/questions/27376295/getting-key-with-the-highest-value-from-object



// var obj = {a: 1, b: 2, c: 2},
// keys = Object.keys(obj),
// largest = Math.max.apply(null, keys.map(x => obj[x]))
// result = keys.reduce((result, key) => { if (obj[key] === largest){
//    result.push(key);
//   } return result; }, []);


// for (var key in namesToAges) {
//   var value = namesToAges[key];
//   if(!agesToCount[namesToAges[value]])
//     agesToCount[namesToAges[value]] = 0;
//   agesToCount[namesToAges[value]] += 1;
// };
// console.log(agesToCount);

// for loop goes over thing i am counting
// var agesToCount = {};
//
// for (var i = 0; i < namesToAges[value].length; i +=1) {
//   if(!agesToCount[namesToAges[i]])
//     agesToCount[namesToAges[i]] = 0;
//   agesToCount[namesToAges[i]] += 1;
// };

// console.log(a.length);
