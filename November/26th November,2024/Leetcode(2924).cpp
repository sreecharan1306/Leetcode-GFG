class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<int>c(n,0);
        int ans=0;
        int ch=0;
        for(auto i:edges) c[i[1]]++;
        for(int i=0;i<n;i++) {
            if(c[i]==0){
                ans=i;
                ch+=1;
            }
        }
        return ch==1?ans:-1;

    }
};