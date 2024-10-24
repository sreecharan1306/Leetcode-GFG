#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n=len(arr)
        for i in range(n-1):
            if arr[i]!=0 and arr[i+1]!=0 and arr[i]==arr[i+1]:
                arr[i]=arr[i]*2
                arr[i+1]=0
                i+=1
        p=arr.count(0)
        ans=[i for i in arr if i!=0]
        ans+=[0]*p
        
        return ans


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        t -= 1


# } Driver Code Ends