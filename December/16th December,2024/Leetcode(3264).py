class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            p=min(nums)
            q=nums.index(p)
            nums[q]=p*multiplier
        return nums
        
            
