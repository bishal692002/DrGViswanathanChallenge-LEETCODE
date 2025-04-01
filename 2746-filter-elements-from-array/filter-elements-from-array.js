/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
   arr = arr.filter((i , index) => fn(i , index));
    return arr; 
};