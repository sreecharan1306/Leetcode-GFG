class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        unordered_map<int,string>mp;
        for(int i=0;i<names.size();i++){
            mp[heights[i]]=names[i];
        }
        sort(heights.rbegin(),heights.rend());
        vector<string>sol;
        for(int i:heights){
            sol.push_back(mp[i]);
        }
        return sol;

    }
};