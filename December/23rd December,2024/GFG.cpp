

class Solution {
  public:
    bool search(vector<int> v, int k){
        int h = v.size() - 1;
        int l = 0;
        while(l <= h){
            int m = l + (h - l) / 2;
            if(k == v[m]) return true;
            else if(k > v[m]) l = m + 1;
            else h = m - 1;
        }
        return false;
    }
    bool searchRowMatrix(vector<vector<int>> &mat, int x) {
        for(vector<int>& v:mat){
            if(v[v.size() - 1] < x) continue;
            else  if(search(v, x)) return true;
        }
        return false;
    }
};