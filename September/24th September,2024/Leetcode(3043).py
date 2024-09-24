class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans=0
        s=set()
        # p1=str(min(a1))
        # p2=str(min(a2))
        a1=map(str,arr1)
        a2=map(str,arr2)
        for i in a1:
            for t in range(len(i)):
                s.add(i[:t+1])
        for i in a2:
            for t in range(len(i)):
                if t>=ans:
                    if i[:t+1] in s:
                        ans=t+1
        return ans
        
