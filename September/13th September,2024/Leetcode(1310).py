class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        prexor=[arr[0]]
        n=len(arr)
        for i in range(1,n):
            prexor.append(prexor[i-1]^arr[i])

        for i in queries:
            x=0
            if i[0]==0:
                ans.append(prexor[i[1]])
            else:
                ans.append(prexor[i[1]]^prexor[i[0]-1])
            # ans.append(x)
        # print(prexor)
        return ans
            