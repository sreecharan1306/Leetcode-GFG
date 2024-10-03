class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s=sum(nums)
        prefix=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            prefix.append(nums[i]+prefix[i-1])
        # print(prefix)
        r=s%p
        if r==0:
            return 0
        res=n
        d=dict()
        d[0]=-1
        cur=0
        for i,num in enumerate(nums):
            cur=(cur+num)%p
            temp=(cur-s)%p
            if d.get(temp) is not None:
                res=min(res,i-d.get(temp))
            d[cur]=i
        if res==n:
            return -1
        return res
