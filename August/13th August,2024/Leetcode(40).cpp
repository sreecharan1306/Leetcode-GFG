class Solution {
public:
    vector<vector<int>>sol;

    void helper(vector<int>cand,int target,int ind,vector<int>temp,int sum){
        if(target==sum){
            if(find(sol.begin(),sol.end(),temp)==sol.end())
                sol.push_back(temp);
        }
        if(target<sum) return;
        for(int i=ind;i<cand.size();i++){
            if (i > ind && cand[i] == cand[i - 1]) continue;  // Skip duplicates
            if(cand[i]>target-sum) break;
            temp.push_back(cand[i]);
            helper(cand,target,i+1,temp,sum+cand[i]);
            temp.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<int>temp;
        helper(candidates,target,0,temp,0);
        // set<vector<int>> s;
        // for(auto i:sol){
        //     s.insert(i);
        // }
        // sol.clear();
        // for(auto i:s){
        //     sol.push_back(i);
        // }
        return sol;
    }
};