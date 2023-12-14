/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    this.cur = n;
    return function() {
        const returnValue = this.cur;
        this.cur += 1
        return returnValue;
    };
};

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */