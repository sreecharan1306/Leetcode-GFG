#User function Template for python3

class Solution:
    def roundToNearest (self, str) : 
        #Complete the function
        n=len(str)
        l=int(str[n-1])
        str=list(str)
        if l<=5:
            str[n-1]='0'
        else:
            if n==1:
                return '10'
            str[n-1]='0'
            i=n-2
            while i>=0 and str[i]=='9':
                str[i]='0'
                i-=1
            if i==-1:
                return "1"+"".join(str)
            else:
                str[i]=chr(ord(str[i])+1)
                return "".join(str)
        return "".join(str)
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends