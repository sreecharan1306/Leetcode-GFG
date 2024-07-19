//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
//  User function template for C++
// #include<ext/pb_ds/assoc_container.hpp>
// #include<ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// #define ordered_set tree<int,null_type,less,rb_tree_tag,tree_order_statistics_node_update>
class Solution {
  public:
  int binarySearch(vector<int>&sol,int key){
      int index=-1,low=0,high=sol.size()-1,mid;
      while(low<=high){
          mid=(low+high)/2;
          if(sol[mid]==key){
              index=mid;
              high=mid-1;
          }
          else if(sol[mid]>key) high=mid-1;
          else low=mid+1;
      }
      return index;
  }
    vector<int> constructLowerArray(vector<int> &arr) {
        // code here
        int n=arr.size();
        vector<int>sol;
        for(int i:arr) sol.push_back(i);
        sort(sol.begin(),sol.end());
        vector<int>ans(n);
        for(int i=0;i<n;i++){
            int index=binarySearch(sol,arr[i]);
            ans[i]=index;
            sol.erase(sol.begin()+index);
        }
        return ans;
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;

    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        int n = arr.size();
        Solution ob;
        vector<int> a = ob.constructLowerArray(arr);
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends