
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def flip(x):
            s=""
            for i in x:
                if i=='1':
                    s+='0'
                else:
                    s+='1'
            return s
        d=defaultdict(int)
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            s=""
            for j in range(n):
                s+=str(matrix[i][j])
            d[s]+=1
        ans=0
        print(d)
        q=sorted(d.items(),key=lambda x:(x[1]),reverse=True)
        for k,v in q:
            l=flip(k)
            ans=max(ans,d[k]+d[l])
        return ans
            

