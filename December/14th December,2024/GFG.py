#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        l,h=0,len(arr)-1
        while l<=h:
            m=(l+h)//2
            if arr[m]==key:
                return m
            elif arr[l]<=arr[m]:
                if arr[l]<=k<=arr[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if arr[m]<=k<=arr[h]:
                    l=m+1
                else:
                    h=m-1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends