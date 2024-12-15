/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumBeauty = function (nums, k) {
    nums.sort((a, b) => a - b);
    console.log(nums)
    let n = nums.length;
    let ans = 1, i = 0;
    for (let j = 0; j < n; j++) {
        if ((nums[j] - nums[i]) <= 2 * k) {
            ans = Math.max(ans, j - i + 1);
        }
        else {
            while ((nums[j] - nums[i]) > 2 * k) {
                i++;
            }
        }
    }
    return ans;
};