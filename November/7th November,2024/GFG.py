#User function Template for python3
class Solution:
    # Function to determine if array arr can be split into three equal sum sets.
    def findSplit(self, arr):
        #cod here
        p=sum(arr)
        if p%3!=0:
            return [-1,-1]
        x=p//3
        n=len(arr)
        prefix=[0]*n
        prefix[0]=arr[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+arr[i]
        if x not in prefix or 2*x not in prefix:
            return [-1,-1]
        return [prefix.index(x),prefix.index(2*x)]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if result == [-1, -1]:
            print("false")
        else:
            print("true")
        print("~")

# } Driver Code Ends