class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        vector<string>dist;
        unordered_map<string,int>mp;
        for(string i:arr){
            mp[i]++;
        }
        for(auto i:arr){
            if(mp[i]==1) dist.push_back(i);
            // cout<< i.first<<"\t"<<i.second<<endl;
        }
        if(dist.size()<k){
            return "";
        }
        else return dist[k-1];
    }
};