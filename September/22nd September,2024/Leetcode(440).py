class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        res=[]
        p=0
        def solve(curr,p):
            if curr>n:
                return 
            if p>k:
                return res[k]
            # if len(res)>k:
            #     return res[k]
            res.append(curr)
            for i in range(10):
                solve(curr*10+i,p)
        for i in range(1,10):
            solve(i,p)

        return res[k-1]