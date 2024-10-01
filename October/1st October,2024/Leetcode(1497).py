class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        p=[]
        for i in arr:
            p.append(i%k)
        c=Counter(p)
        print(c)
        if c[0]%2==1:
            return False
        for i in range(1,k):
            if c[i]!=c[k-i]:
                return False
        return True