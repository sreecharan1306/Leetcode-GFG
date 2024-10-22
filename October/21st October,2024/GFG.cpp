// User function template for C++
class Solution {
  public:
  long long int mod=1e9+7;
    int countgroup(vector<int>& arr) {
        // Complete the function
        int x=0;
        for(int i:arr) x^=i;
        if(x!=0) return 0;
        else return (((1ll<<arr.size())-2)/2)%mod;
    }
};