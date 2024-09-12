class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # p=Counter(allowed)
        ans=0
        p=set(allowed)
        for i in words:
            flag=True
            for j in i:
                if j not in p:
                    flag=False
                    break
            if flag:
                ans+=1
        return ans