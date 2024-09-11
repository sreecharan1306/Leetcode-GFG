/**
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minBitFlips = function (start, goal) {
    let ans = 0;
    while (start != 0 || goal != 0) {
        if ((start % 2 ^ goal % 2) == 1) ans++;
        start >>= 1;
        goal >>= 1;
    }
    return ans;
};