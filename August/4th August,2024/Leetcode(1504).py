class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans=[]

        for i in range(n):
            for j in range(i,n):
                ans.append(sum(nums[i:j+1]))
        ans.sort()
        # print(ans)
        mod=pow(10,9)+7
        return sum(ans[left-1:right])%mod

