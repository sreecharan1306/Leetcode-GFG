class Solution {
public:
    static bool cmp(pair<char, int>& a,pair<char, int>& b) {
        return a.second > b.second;
    }
    int minimumPushes(string word) {
        int ans = 0;
        int p=1;
        map<char, int> freq;

        for (char s : word) {
            freq[s]++;
        }
        vector<pair<char,int>> vec;
        for(auto i:freq) vec.push_back(make_pair(i.first,i.second));
        sort(vec.begin(),vec.end(),cmp);
        // for(auto i:vec){
        //     cout<<i.first<<"\t"<<i.second<<endl;
        // }
        for(int i=0;i<vec.size();i++){
            if(i>0 && (i%8)==0){
                p+=1;
            }
            ans+=p*vec[i].second;
            // cout<<ans<<endl;
        }
        return ans;
    }
};