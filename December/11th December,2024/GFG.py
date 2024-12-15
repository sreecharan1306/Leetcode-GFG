class Solution:
    def mergeArrays(self, a, b): 
        # code here
        right=len(a)-1
        start=0
        while right>=0 and start<len(b):
            if(a[right]>b[start]):
                a[right],b[start]=b[start],a[right]
                right-=1
            start+=1
        a.sort()
        b.sort()
        
                


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends