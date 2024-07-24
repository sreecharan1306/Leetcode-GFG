class Solution {
public:
    int con(int i,map<int,int>mp){
        if(i==0) return mp.at(0);
        int temp=i;
        string sol="";
        while(temp!=0){
            int n=temp%10;
            sol+=to_string(mp.at(n));
            temp=temp/10;
        }
        reverse(sol.begin(),sol.end());
        return stoi(sol);

    }
    static bool cmp(pair<int,int> &A,pair<int,int> &B){
        // if(A.second==B.second){
        //     return A.first>B.first;
        // }
        return A.second<B.second;
    }
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        map<int,int>mp;
        for(int i=0;i<=9;i++){
            mp[i]=mapping[i];
        }
        vector<pair<int,int>> mpnums;
        for (int i : nums) {
            mpnums.push_back({i, con(i, mp)});
        }

        sort(mpnums.begin(), mpnums.end(), cmp);
        vector<int>ans;
        for(auto i:mpnums){
            ans.push_back(i.first);
        }
        return ans;
    }
};