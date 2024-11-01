#User function Template for python3
from collections import Counter
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
        arr.sort()
        ans=0
        p=Counter(arr)
        for i in arr:
            if p[i-k]:
                ans+=p[i-k]
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends