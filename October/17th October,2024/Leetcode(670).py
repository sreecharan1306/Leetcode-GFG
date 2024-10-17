class Solution:
    def maximumSwap(self, num: int) -> int:
        p=list(str(num))
        l=list(map(lambda x:int(x),p))
        q=[]
        n=len(l)
        lasind=dict()
        for i in range(n):
            lasind[l[i]]=i
        for i in range(n):
            q.append(max(l[i:]))
        for i in range(n):
            if l[i]==q[i]:
                continue
            else:
                temp=q[i]
                j=lasind[q[i]]
                x=l[i]
                l[i]=l[j]
                l[j]=x
                break
        ans=0
        for i in range(n):
            ans+=l[i]*pow(10,n-1-i)
        return ans


