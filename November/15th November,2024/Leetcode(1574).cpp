class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int i=1;
        int n=arr.size();
        while(i<n && arr[i]>=arr[i-1]){
            i++;
        }
        if(i==n) return 0;
        int j=n-1;
        while(j>0 && arr[j]>=arr[j-1]){
            j--;
        }
        int ans=INT_MAX;
        ans=min(ans,j);
        ans=min(ans,n-i);
        int p=0;
        while(j<n && p<i){
            if(arr[p]<=arr[j]){
                ans=min(ans,j-(p+1));
                cout<<ans<<"  ";
                p++;
            }
            else{
                j++;
            }
        }
        return ans;
    }
};