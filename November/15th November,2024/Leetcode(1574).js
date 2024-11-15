/**
 * @param {number[]} arr
 * @return {number}
 */
var findLengthOfShortestSubarray = function (arr) {
    let i = 1;
    let n = arr.length;
    while (i < n && arr[i] >= arr[i - 1]) i++;
    if (i == n) return 0;
    let j = n - 1;
    while (j > 0 && arr[j] >= arr[j - 1]) j--;    
    let ans = 100000;
    ans = Math.min(ans, j);
    ans = Math.min(ans, n - i);
    let p = 0;
    while (j < n && p < i) {
        if (arr[p] <= arr[j]) {
            ans = Math.min(ans, j - (p + 1));
            p++;
        }
        else j++;
    }
    return ans;
};