//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:
    // nums: given vector
    // return the Product vector P that hold product except self at each index
    vector<long long int> productExceptSelf(vector<long long int>& nums) {

        // code here
        int cz=0;
        vector<long long int>sol;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0) cz+=1;
        }
        long long int s=1;
        for(long long int i:nums){
            if(i!=0)
            s=s*i;
            // pref.push_back(s);
        }
        if(cz==1){
            for(int i=0;i<nums.size();i++){
                if(nums[i]!=0){
                    sol.push_back(0);
                }
                else{
                    sol.push_back(s);
                }
            }
            return sol;
        }
        else if(cz>=2){
            vector<long long int> ans(nums.size(),0);
            return ans;
        }
        // vector<long long int>pref;
       
        // vector<long long int>sol;
        for(int i=0;i<nums.size();i++){
            sol.push_back(s/nums[i]);
        }
        return sol;
        
    }
};


//{ Driver Code Starts.
int main() {
    int t; // number of test cases
    cin >> t;
    while (t--) {
        int n; // size of the array
        cin >> n;
        vector<long long int> arr(n), vec(n);

        for (int i = 0; i < n; i++) // input the array
        {
            cin >> arr[i];
        }
        Solution obj;
        vec = obj.productExceptSelf(arr); // function call

        for (int i = 0; i < n; i++) // print the output
        {
            cout << vec[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends