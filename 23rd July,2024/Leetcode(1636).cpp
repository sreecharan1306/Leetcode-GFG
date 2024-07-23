class Solution {
public:
    static bool cmp(pair<int,int> A,pair<int,int>B){
        if(A.second==B.second){
            return A.first>B.first;
        }
        return A.second<B.second;
    }
    vector<int> frequencySort(vector<int>& nums) {
        map<int,int>mp;
        for(int i:nums){
            mp[i]++;
        }
        vector<pair<int,int>>freq(mp.begin(),mp.end());
        sort(freq.begin(),freq.end(),cmp);
        vector<int>sol;
        for(auto i:freq){
            sol.insert(sol.end(),i.second,i.first);
        }
        return sol;
    }
};