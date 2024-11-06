class Solution {
public:
    int st(int x) {
        int c = 0;
        for (int i = 0; i < 9; i++) {
            if ((x >> i) & 1)
                c += 1;
        }
        return c;
    }
    bool canSortArray(vector<int>& nums) {
        map<int, int> mp;
        for (int i : nums)
            mp[i] = st(i);
        vector<pair<int,int>>v;
        int prev=nums[0];
        int bs=nums[0];
        for(int i=1;i<nums.size();i++){
            if(mp[nums[i]]==mp[nums[i-1]]){
                prev=max(prev,nums[i]);
                bs=min(bs,nums[i]);
            }
            else{
                v.push_back(make_pair(bs,prev));
                bs=nums[i];
                prev=nums[i];
            }
        }
        v.push_back(make_pair(bs,prev));
        for(int i=1;i<v.size();i++){
            // cout<<v[i].first<<"  "<<v[i].second<<endl;
            if(v[i].first<v[i-1].second) return false;
        }
        return true;


        
    }
};