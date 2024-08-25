class Solution:
    def findComplement(self, num: int) -> int:
        m=num
        cnt=0
        p=num
        while m!=0:
            p=p^(1<<cnt)

            cnt+=1
            m//=2
        return p
