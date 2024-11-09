#User function Template for python3

class Solution:
    def minSum(self, arr):
        n=len(arr)
        a,b=[],[]
        arr.sort(reverse=True)
        for i in range(n):
            if i&1:
                a.append(arr[i])
            else:
                b.append(arr[i])
        car=0
        i,j=0,0
        ans=""
        t=0
        p=min(len(a),len(b))
        while i<p and j<p:
            t=a[i]+b[i]+car
            ans+=(str((t)%10))
            car=t//10
            i+=1
            j+=1
        if len(b)!=len(a):
            t=b[i]+car
            ans+=(str((t)%10))
            car=t//10
        if car!=0:
            ans+=str(car)
        return ans[::-1].lstrip('0')


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends