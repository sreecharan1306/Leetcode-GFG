class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        p=[0]*32
        for i in candidates:
            for j in range(32):
                if (i>>j)&1:
                    p[j]+=1
        # print(p)
        return max(p)