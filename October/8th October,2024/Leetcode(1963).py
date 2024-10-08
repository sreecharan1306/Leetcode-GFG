class Solution:
    def minSwaps(self, s: str) -> int:
        d=0
        for i,c in enumerate(s):
            if c=='[':
                d+=1
            else:
                if d>0:
                    d-=1
        return (d+1)//2