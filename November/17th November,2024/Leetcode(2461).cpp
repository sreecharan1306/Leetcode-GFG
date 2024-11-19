class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int>mp;
        long long ans=0;
        int n=nums.size();
        int i=0;
        int j=0;
        long long s=0;
        while(j<n){
            mp[nums[j]]++;
            s+=nums[j];
            if((j-i+1)>k){
                mp[nums[i]]--;
                if(mp[nums[i]]==0)
                    mp.erase(nums[i]);
                s-=nums[i];
                i++;
            }
            if(mp.size()==k && (j-i+1)==k) ans=max(ans,s);
            j+=1;
        }
        return ans;
    }
};