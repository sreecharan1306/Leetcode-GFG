//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    void sort012(vector<int>& arr) {
        // code here
        int cz=0,co=0,ct=0;
        for(i:arr){
            if(i==0){
                cz++;
            }
            else if(i==1){
                co++;
            }
            else{
                ct++;
            }
        }
        int ind=0;
        for(int i=0;i<cz;i++){
            arr[ind++]=0;
        }
        for(int i=0;i<co;i++){
            arr[ind++]=1;
        }
        for(int i=0;i<ct;i++){
            arr[ind++]=2;
        }
        
        
    }
};

//{ Driver Code Starts.
int main() {

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {

        vector<int> a;
        string input;
        int num;

        getline(cin, input);
        stringstream s2(input);
        while (s2 >> num) {
            a.push_back(num);
        }
        Solution ob;
        ob.sort012(a);

        int n = a.size();
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }

        cout << endl;
    }
    return 0;
}

// } Driver Code Ends