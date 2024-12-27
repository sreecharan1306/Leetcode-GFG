#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
from collections import defaultdict
class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        mp=defaultdict(int)
        ans=0
        for i in arr:
            if mp[target-i]>0:
                ans+=mp[target-i]
            mp[i]+=1
        return ans

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends