class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st=""
        for i in s:
            st+=(str(ord(i)-97+1))
        ans=0
        temp=st
        for _ in range(k):
            sum=0
            for i in st:
                sum+=(int(i))
            # print(sum)
            st=str(sum)
            ans=sum
            # print(st)
        return ans