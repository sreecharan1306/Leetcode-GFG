//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    vector<vector<int>>ans;
    bool isSafe(int row,int col,vector<vector<int>>&temp,int n){
        int r=row;
        int c=col;
        while(r>=0 && c>=0){
            if(temp[r--][c--]!=0) return false;
        }
        c=col;
        r=row;
        while(c>=0){
            if(temp[row][c--]!=0) return false;
        }
        c=col;
        r=row;
        while(c>=0 && r<n){
            if(temp[r++][c--]!=0) return false;
        }
        return true;
        
    }
    void solve(int col,vector<vector<int>>&temp,int n){
        if(col==n){
            vector<int>bs;
            for(int i=0;i<n;i++){
                int sum=0;
                for(int j=0;j<n;j++){
                    sum+=temp[j][i];
                }
                bs.push_back(sum);
            }
            ans.push_back(bs);
            return;
        }
        for(int row=0;row<n;row++){
            if(isSafe(row,col,temp,n)){
                temp[row][col]=row+1;
                solve(col+1,temp,n);
                temp[row][col]=0;
            }
        }
    }
    vector<vector<int>> nQueen(int n) {
        // code here
        vector<int>d(n,0);
        vector<vector<int>>temp(n,d);
        
        
        solve(0,temp,n);
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        
        Solution ob;
        vector<vector<int>> ans = ob.nQueen(n);
        if(ans.size() == 0)
            cout<<-1<<"\n";
        else {
            for(int i = 0;i < ans.size();i++){
                cout<<"[";
                for(int u: ans[i])
                    cout<<u<<" ";
                cout<<"] ";
            }
            cout<<endl;
        }
    }
    return 0;
}
// } Driver Code Ends