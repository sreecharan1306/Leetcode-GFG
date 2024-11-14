from math import ceil
class Solution:
    def minimizedMaximum(self, n: int, nums: List[int]) -> int:
        def check(m,n,nums):
            for i in nums:
                n-=ceil(i/(m*1.0))
                if n<0:
                    return False
            return True

        
        l,h=1,max(nums)
        while l<h:
            m=(l+h)//2
            ans=-1
            # p=check(m,n,nums)
            if check(m,n,nums):
                ans=m
                h=m
            else:
                l=m+1
        return l

