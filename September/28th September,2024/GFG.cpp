//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int minimizeCost(int& k,vector<int>& arr) {
        // Code here
        int n=arr.size();
        int mi,jump;
        if(n==1) return arr[0];
        vector<int>dp(n+1);
        dp[0]=0;
        // if(n<=2) return dp[n];
        // dp[1]=abs(arr[1]-arr[0]);
        for(int i=1;i<n;i++){
            mi=INT_MAX;
            for(int j=1;j<=k;j++){
                if(i>=j){
                   jump=dp[i-j]+abs(arr[i]-arr[i-j]);
                   mi=min(mi,jump);
                }
            }
            dp[i]=mi;
        }
        return dp[n-1];
    }
};


//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        string ks;
        getline(cin, ks);
        int k = stoi(ks);
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        int res = obj.minimizeCost(k, arr);
        cout << res << endl;
        // string tl;
        // getline(cin, tl);
    }
    return 0;
}

// } Driver Code Ends