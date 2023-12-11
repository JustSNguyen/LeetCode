/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArr = [];
    N = arr.length
    for (let i = 0; i < N; ++i) {
        const newValue = fn(arr[i], i);
        newArr.push(newValue);
    }
    return newArr;
};