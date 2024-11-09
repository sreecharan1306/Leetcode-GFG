class Solution:
    def minEnd(self, n: int, x: int) -> int:
        p=bin(x)[2:].zfill(50)[::-1]

        # print(p)
        q=bin(n-1)[2:].zfill(50)[::-1]
        # print(q)
        j=0
        r=""
        for i in p:
            if i=='1':
                r+=i
                continue
            else:
                r+=q[j]
                j+=1
        # print(r[::-1])
        return int(r[::-1],2)