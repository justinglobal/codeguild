//sum_pairs.js

var findSumPairs = function(pairs, pairSum){
    var finalResult = [];
    for (var pos1 = 0; pos1 < pairs.length; pos1 += 1) { //while i < pairs.length
        var pos2 = pos1 + 1;
        for (pos1; pos2 <= pairs.length; pos2 += 1){
            if (pairs[pos1] + pairs[pos2] === pairSum){
                finalResult.push([pairs[pos1], pairs[pos2]])
            };
        };
    };
    return finalResult;
};

console.dir(findSumPairs([-1, 0, 1, 2], 3)); // 6 unique combos
console.dir(findSumPairs([-1, 0, 1, 2], 1)); // 6 unique combos
console.dir(findSumPairs([2, -1, 2], 1)); // 5 unique combos
console.dir(findSumPairs([-1, 1, 2, 2], 3)); // 6 unique combos
