class Solution:
    # def __init__(self):
    #     self.ans=0
    #     self.subs=set()
    # def solve(self,s:str,ind,n,t):
    #     if ind==n:
    #         self.ans=max(self.ans,len(self.subs))
    #         return
    #     for x in range(ind+1,n):
    #         if t in self.subs:
    #             continue 
    #         self.subs.add(t)
    #         self.solve(s,ind+x,n,s[ind:x+1])
    #         self.subs.remove(t)

    def maxUniqueSplit(self, s: str) -> int:
        n=len(s)
        t=""
        def dfs(i,st):
            if i==len(s):
                return 0
            res=0
            for j in range(i,len(s)):
                c=s[i:j+1]
                if c in st:
                    continue
                st.add(c)
                res=max(res,1+dfs(j+1,st))
                st.remove(c)
            return res
        return dfs(0,set())


