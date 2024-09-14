#User function Template for python3


class Solution:
    def rearrange(self,arr):
        # code here
        pos=[i for i in arr if i>=0]
        neg=[j for j in arr if j<0]
        p=len(pos)
        n=len(neg)
        b=[]
        k,l=0,0
        # print(pos)
        # print(neg)
        while k<p and l<n:
            b.append(pos[k])
            k+=1
            b.append(neg[l])
            l+=1
        while k<p:
            b.append(pos[k])
            k+=1
        while l<n:
            b.append(neg[l])
            l+=1
        for i in range(len(arr)):  
            arr[i] = b[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends