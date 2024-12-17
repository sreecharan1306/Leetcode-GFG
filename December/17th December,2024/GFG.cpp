//{ Driver Code Starts
// Initial function template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int helper(int k,vector<int>stalls,int m){
        int n=stalls.size();
        int ini=stalls[0];
        int ls=1;
        for(int i=1;i<n;i++){
            if((stalls[i]-ini)>=m){
                ls+=1;
                ini=stalls[i];
            }
        }
        if(ls<k) return 0;
        return 1;
    }
    int aggressiveCows(vector<int> &stalls, int k) {

        // Write your code here
        int ans=-1;
        sort(stalls.begin(),stalls.end());
        int l=0,h=1e9;
        while(l<=h){
            int m=(l+h)/2;
            int temp=helper(k,stalls,m);
            if(temp){
                ans=m;
                l=m+1;
            }
            else{
                h=m-1;
            }
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int test_case;
    cin >> test_case;
    cin.ignore();
    while (test_case--) {

        int k;
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        string in;
        getline(cin, in);
        stringstream sss(in);
        int num;
        while (sss >> num) {
            k = num;
        }
        Solution ob;
        int ans = ob.aggressiveCows(arr, k);
        cout << ans << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends