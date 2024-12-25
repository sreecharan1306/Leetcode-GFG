// User function Template for C++
class Solution {
  public:
    void setMatrixZeroes(vector<vector<int>> &mat) {
        // code here
        int m = mat.size();  
        int n = mat[0].size();  
        vector<pair<int, int>> q;  
        for (int i = 0; i < m; i++) {  
            for (int j = 0; j < n; j++) {  
                if (mat[i][j] == 0) {  
                    q.push_back({i, j});  
                }  
            }  
        }  
    

        for (const auto& pair : q) {  
            int a = pair.first;  
            int b = pair.second;  
            for(int i = 0; i < m; i++) {  
                mat[i][b] = 0;  
            }  
            for (int i = 0; i < n; i++) {  
                mat[a][i] = 0;  
            }  
        }  
    
        // return mat; 
    }
};