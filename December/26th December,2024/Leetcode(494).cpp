class Solution {
public:
    int help(vector<int> nums, int n, int ind, int target, int sum,
             vector<unordered_map<int, int>>& dp) {
        if (ind == n) {
            return sum == target ? 1 : 0;
        }
        if (dp[ind].count(sum))
            return dp[ind][sum];
        int add = help(nums, n, ind + 1, target, sum + nums[ind], dp);
        int sub = help(nums, n, ind + 1, target, sum - nums[ind], dp);
        return dp[ind][sum] = add + sub;
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        // int s = accumulate(nums.begin(), nums.end(), 0);
        // int s1 = (s + target) / 2;
        int n = nums.size();
        vector<unordered_map<int, int>> dp(n);
        int ans = help(nums, nums.size(), 0, target, 0, dp);
        return ans;
    }
};