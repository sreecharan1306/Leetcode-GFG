class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bs(nums,ele,l,h):
            while l<=h:
                m=(l+h)//2
                if nums[m]>=ele:
                    h=m-1
                else:
                    l=m+1
            return l
        nums.sort()
        n=len(nums)
        ans = 0
        for i, e in enumerate(nums):
            x = bs(nums, upper - e+1,i+1,n-1
            )
            y = bs(nums, lower - e,i+1,n-1)
            ans += (x - y)
        return ans











