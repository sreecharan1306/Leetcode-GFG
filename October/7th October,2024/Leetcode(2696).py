class Solution:
    def minLength(self, s: str) -> int:
        n=len(s)
        p=[]
        for i in s:
            if p and ((i=='B' and p[-1]=='A') or (i=='D' and p[-1]=='C')):
                p.pop()
            else:
                p.append(i)
        

        # while i+1<len(p):
        #     if (p[i]=='A' and p[i+1]=='B') or (p[i]=='C' and p[i+1]=='D'):
        #         p.pop(i+1)
        #         p.pop(i)
        #         i=0
        #         print(p)
        #     else:
        #         i+=1
        return len(p)
                
                