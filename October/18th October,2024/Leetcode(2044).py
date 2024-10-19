class Solution:
    def gensubsets(self,nums, n):
        total = 2**n
        subsets = []
        for i in range(total):
            subset = [nums[j] for j in range(n) if (i & (1 << j))]
            subsets.append(subset)
        return subsets

    def genor(self,arr):
        return reduce(lambda x, res: x | res, arr, 0)


    def countMaxOrSubsets(self, nums: List[int]) -> int: 
        maxor = reduce(lambda x, res: x | res, nums, 0)
        n = len(nums)
        ans = 0
        subsets = self.gensubsets(nums, n)
        for i in subsets:
            p = self.genor(i)
            if p == maxor:
                ans += 1
        return ans
