class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)
        ans=0
        wbi=0 #white balls index
        for i in range(n):
            if s[i]=='0':
                ans+=(i-wbi) #moving to wbi
                wbi+=1
        return ans
