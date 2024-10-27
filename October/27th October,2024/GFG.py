from collections import Counter
class Solution:
    def findTriplet(self, arr):
        p=Counter(arr)
        n=len(arr)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if p[arr[i]+arr[j]] and arr[i]+arr[j]!=0:
                    return True
        
        return False
                    





#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends