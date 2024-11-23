#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        arr.sort()
        ans=arr[-1]-arr[0]
        for i in range(len(arr)-1):
            mini=min(arr[0]+k,arr[i+1]-k)
            maxi=max(arr[-1]-k,arr[i]+k)
            ans=min(ans,maxi-mini)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends