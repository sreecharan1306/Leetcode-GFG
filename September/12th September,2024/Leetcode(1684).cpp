class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_map<char,int>mp;
        for(char s:allowed){
            mp[s]++;
        }
        int ans=0;
        for(string i:words){
            bool flag=true;
            for(char ch:i){
                if(mp[ch]==0) flag=false;
            }
            if(flag) ans+=1;
        }
        return ans;
    }
};