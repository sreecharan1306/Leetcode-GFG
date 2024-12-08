class Solution(object):
    def minimumSize(self, nums, k):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        l, r=1, max(nums)
        while l<r:
            m=(l+r)>>1
            cnt=sum((x-1)//m for x in nums)
            if cnt<=k: r=m
            else: l=m+1
        return r