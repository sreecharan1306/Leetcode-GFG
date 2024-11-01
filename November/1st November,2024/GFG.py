#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        p,q=[],[]
        n=len(arr)
        i,j=0,n-1
        while i<j:
            p.append(arr[i])
            p.append(arr[j])
            i+=1
            j-=1
        if i==j:
            p.append(arr[i])
        ans=0
        for i in range(1,len(arr)):
            ans+=(abs(p[i]-p[i-1]))
        ans+=(abs(p[0]-p[-1]))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends