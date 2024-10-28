class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s=set(nums)
        nums.sort()
        ans=0
        flg=True
        for i in nums:
            k=1
            while pow(i,2) in s:
                k+=1
                i=i*i
                flg=False
            ans=max(ans,k)
        return ans if not flg else -1