class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        # temp=nums+nums
        i,l,co,m=0,0,0,0
        o=nums.count(1)
        while i<n*2:
            if nums[i%n]:
                co+=1
            if i-l+1>o:
                co-=nums[l%n]
                l+=1
            m=max(m,co)
            if m==o:
                return 0
            i+=1
            # print(p,end="->")
            # print(m)
        return o-m