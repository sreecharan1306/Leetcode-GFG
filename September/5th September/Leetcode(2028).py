class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        tot=mean*(m+n)
        temp=tot-sum(rolls)
        ans=[]
        if 6*n<temp or temp<0 or temp<n:
            return []
        p=temp//n
        q=temp%n
        for i in range(q):
            ans.append(p+1)
        for i in range(n-q):
            ans.append(p)
        return ans
        