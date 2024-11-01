class Solution:
    def makeFancyString(self, s: str) -> str:
        i,j,k=0,1,2
        n=len(s)
        t=""
        if n<=2:
            return s
        while k<n:
            while k<n and s[i]==s[j] and s[j]==s[k]:
                i,j,k=i+1,j+1,k+1
            t+=s[i]
            i,j,k=i+1,j+1,k+1
        if i<n:
            t+=s[i]
        if j<n:
            t+=s[j]
        return t