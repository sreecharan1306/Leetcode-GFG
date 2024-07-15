//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    string smallestNumber(int s, int d) {
        // code here
        if(s>9*d) return "-1";
        string ans(d, '0');
        s--;
        for (int i = d - 1; i >= 0; i--) {
            if (s > 9) {
                ans[i] = '9';
                s -= 9;
            } else {
                ans[i] = '0' + s;
                s = 0;
            }
        }
        ans[0] = '0' + (ans[0] - '0' + 1);
        return ans;
        // string ans="";
        // int num=s;
        // for(int i=0;i<9;i++){
        //     if(num>0 && num<=9 && i==d){
        //         ans=num+a;
        //         num=0;
        //     }
        //     else if(i<d-1 && num==1){
        //         ans+='0';
        //     }
        //     else if(num>10){
        //         num-=9;
        //         ans+='9';
        //     }
        //     else{
        //         ans+=(num-1);
        //         num=1;
        //     }
        // }
        // if(num==0) return  ans;
        // return "-1";
    }
};

//{ Driver Code Starts.

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        int s, d;
        cin >> s >> d;
        Solution ob;
        cout << ob.smallestNumber(s, d) << "\n";
    }

    return 0;
}
// } Driver Code Ends