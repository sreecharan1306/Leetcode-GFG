class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        p=[0,0,0]
        n=len(s)
        for i in s:
            p[ord(i)-ord('a')]+=1
        if min(p)<k:
            return -1
        ans=float("inf")
        i=0
        for j in range(n):
            p[ord(s[j])-ord('a')]-=1
            while min(p)<k:
                p[ord(s[i])-ord('a')]+=1
                i+=1
            ans=min(n-(j-i+1),ans)

        return -1 if ans==float("inf") else ans