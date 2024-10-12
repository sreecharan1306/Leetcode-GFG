class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        mr=[0]*n
        t=n-1
        m=0
        for i in range(n):
            mr[t]=max(nums[n-1-i],m)
            m=mr[t]
            t-=1
        l=0
        for r in range(n):
            while nums[l]>mr[r]:
                l+=1
            ans=max(ans,r-l)
        return ans