class Solution {
public:
    int findTheLongestSubstring(string s) {
        int n=s.size();
        map<char,int>mp;
        mp['a']=1;
        mp['e']=2;
        mp['i']=4;
        mp['o']=8;
        mp['u']=16;
        map<int,int>seen;
        seen[0]=-1;
        int ml=0;
        int mask=0;
        for(int i=0;i<n;i++){
            mask=mask^mp[s[i]-'a'];
            if(mp[s[i]]) mask^=mp[s[i]];
            if(seen.find(mask)==seen.end()){
                seen[mask]=i;
            }
            else ml=max(ml,i-seen[mask]);
        }

        return ml;
    }
};