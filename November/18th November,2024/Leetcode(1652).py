class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        if k==0:
            return [0]*n
        temp=code+code
        ans=[0]*n
        if k>0:
            for i in range(n):
                p=0
                for j in range(i+1,i+k+1):
                    p+=temp[j]
                ans[i]=p
            return ans
        for i in range(n):
            p=0
            for j in range(n+i-1,n+i+k-1,-1):
                p+=temp[j]
            ans[i]=p
        return ans
        