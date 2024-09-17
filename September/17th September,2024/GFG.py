#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        n=len(arr)
        s=arr[0]+k
        l=arr[-1]-k
        ans=arr[-1]-arr[0]
        if ans<0:
            return arr[-1]-arr[0]
            
        for i in range(n-1):
            mini=min(s,arr[i+1]-k)
            maxi=max(l,arr[i]+k)
            if mini>=0:
                ans=min(ans,maxi-mini)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends