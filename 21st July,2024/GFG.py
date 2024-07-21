
class Solution:
    def findMaxProduct(self, arr):
        sol=1
        neg=[]
        mn=float('-inf')
        z=arr.count(0)
        n=len(arr)
        mod=10**9+7
        if n==z:
            return 0
        
        for i in arr:
            if i!=0:
                sol*=i
            if i<0 and mn<i:
                mn=i
                
            # sol*=i
            # sol%=mod
        # if sol>0:
        #     return sol
        # if (len(neg)+z)==n:
        #     return 0
        if sol<0:
            sol=sol//mn
            # return sol
        sol%=mod
        return sol
        # if sol<=0:
        #     return 0
        # else:
        #     return sol
    
