class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        p=pow(2,maximumBit)
        answer=[0]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]^nums[i]
        for i in range(n-1,-1,-1):
            answer[n-i-1]=prefix[i]^(p-1)
        return answer