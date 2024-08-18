class Solution:
    def nthUglyNumber(self, n: int) -> int:
        v2,v3,v5=0,0,0
        ug=[1]
        while len(ug)!=n:
            p=min(ug[v2]*2,ug[v3]*3,ug[v5]*5)
            if ug[v2]*2==p:
                v2+=1
            elif ug[v3]*3==p:
                v3+=1
            elif ug[v5]*5==p:
                v5+=1
            if p in ug:
                continue
            ug.append(p)
        print(ug)
        return ug[-1]


        