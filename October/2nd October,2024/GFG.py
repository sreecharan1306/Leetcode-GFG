#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        # code here
        op=1
        n=len(arr)
        if n==1:
            return arr[0]
        x=(n-1)//4
        y=(n-1)%4
        if(y==0 or y==1 or y==3):
            return arr[x+1]
        return arr[x+2]
        # while len(arr)!=1:
        #     arr[:]=arr[len(arr)-1:]+arr[:len(arr)-1]
        #     arr.pop(len(arr)-op)
        #     op+=1
        # return arr[0]


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends