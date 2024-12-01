class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        p,q=0,0
        a=float("inf")
        for i in matrix:
            for j in i:
                a=min(a,abs(j))
                p+=abs(j)
                if j<0:
                    q+=1
        return p-2*a if q&1 else p
