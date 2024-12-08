class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s,e=0,0
        if start.count('L')!=target.count('L') or start.count('R')!=target.count('R'):
            return False
        n=len(start)
        while s<n and e<n:
            while s<n and start[s]=='_':
                s+=1
            while e<n and target[e]=='_':
                e+=1
            if s==n and e==n:
                return True
            if s==n or e==n:
                return False
            if start[s]!=target[e] or (start[s]=='L' and s<e) or (start[s]=='R' and e<s):
                return False
            s+=1
            e+=1
        return True