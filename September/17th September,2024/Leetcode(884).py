class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=s1.split()
        b=s2.split()
        d=a+b
        c=Counter(d)
        # for i in d:
        #     if c.get(i) is not None:
        #         c[i]+=1
        #     else:
        #         c[i]=1
        # print(c.keys())
        ans=[]
        for i in c.keys():
            if c[i]==1:
                ans.append(i)
        return ans
