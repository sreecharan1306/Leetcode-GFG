class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int ans=1;
        int m=*max_element(nums.begin(),nums.end());
        int i=0;
        int n=nums.size();
        while(i<n){
            if(nums[i]==m){
                int c=0;
                while(i<n && nums[i++]==m){
                    c+=1;
                }
                ans=max(ans,c);
            }
            i++;
        }
        return ans;
    }
};