class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        lis=[]
        for i in words:
            for j in range(len(i)):
                lis.append(i[:j+1])
        c=Counter(lis)
        ans=[]
        for i in words:
            temp=0
            for j in range(len(i)):
                temp+=c[i[:j+1]]
            ans.append(temp)
        return ans
