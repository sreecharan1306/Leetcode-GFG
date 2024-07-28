//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:

    bool kPangram(string str, int k) {
        // code here
        int cnt=0;
        map<char,int>mp;
        for(char i:str){
            if(i!=32){
                cnt++;
                mp[i]++;
            }
        }
        return cnt>=26&& 26-mp.size()<=k;
        // for(int i=0;i<26;i++){
        //     if(!mp[char(97+i)]) return false;
        // }
        // return true;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        cin.ignore();
        string str;
        getline(cin, str);

        int k;
        cin >> k;

        Solution ob;
        bool a = ob.kPangram(str, k);
        if (a)
            cout << "true" << endl;
        else
            cout << "false" << endl;
    }
    return 0;
}
// } Driver Code Ends