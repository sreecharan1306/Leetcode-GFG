class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        p=[i for i in range(1,n+1)]
        ans=0
        sum=0
        s=set(banned)
        for i in range(1,n+1):
            if i not in s:
                if sum+i<=maxSum:
                    sum+=i
                    ans+=1
        return ans