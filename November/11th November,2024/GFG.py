#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        s=set()
        ans=0
        m=0
        for i in range(len(arr)):
            m=max(m,arr[i])
            if arr[i] in s:
                p=(m+1-arr[i])
                # arr[i]+=p
                ans+=p
                m+=1
                s.add(m)
            else:
                s.add(arr[i])
        # print(arr)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends