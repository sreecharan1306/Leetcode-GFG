//{ Driver Code Starts
// Initial function template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int help(vector<int>arr,int m){
        int n=arr.size();
        int st=1;
        long long pages=0;
        for(int i=0;i<n;i++){
            if(pages+arr[i]<=m){
                pages+=arr[i];
            }
            else{
                st++;
                pages=arr[i];
            }
        }
        return st;
    }
    int findPages(vector<int> &arr, int k) {
        // code here
        int n=arr.size();
        if(k>n) return -1;
        int l=*max_element(arr.begin(),arr.end());
        int h=accumulate(arr.begin(),arr.end(),0);
        if(k==1) return h;
        if(k==n) return l;
        while(l<=h){
            int m=(l+h)/2;
            int st=help(arr,m);
            if(st>k){
                l=m+1;
            }
            else h=m-1;
        }
        return l;
    }
};

//{ Driver Code Starts.

int main() {
    int test_case;
    cin >> test_case;
    cin.ignore();
    while (test_case--) {

        int d;
        vector<int> arr, brr, crr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        getline(cin, input);
        ss.clear();
        ss.str(input);
        while (ss >> number) {
            crr.push_back(number);
        }
        d = crr[0];
        int n = arr.size();
        Solution ob;
        int ans = ob.findPages(arr, d);
        cout << ans << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends