class Solution:
    def solve(self,a,b):
        ans1,ans2=0,0
        a=a.split(":")
        b=b.split(":")
        hour1=int(a[0])
        hour2=int(b[0])
        m1=int(a[1])
        m2=int(b[1])
        dh1=hour2-hour1
        if dh1<0:
            dh1+=24

        dm1=m2-m1
        if dm1<0:
            dh1-=1
        ans1+=(60*dh1)
        ans1+=dm1
        dh2=hour1-hour2
        if dh2<0:
            dh2+=24
        dm2=m1-m2
        if dm2<0:
            dm2+=60
            dh2-=1
        ans2+=(60*dh2)
        ans2+=dm2
        return min(ans1,ans2)


    def findMinDifference(self, tp: List[str]) -> int:
        tp.sort(key=lambda x:x[0] in x.split(":"))
        tp.sort(key=lambda x:int(x.split(":")[0])*60+int(x.split(":")[1]))
        # a=tp[0].split(":")
        # b=tp[1].split(":")
        # c=tp[-1].split(":")
        # print(a)
        # print(b)
        # print(c)
        # print(tp)
        # d1=self.solve(a,b)
        ans=self.solve(tp[0],tp[-1])
        for i in range(1,len(tp)):
            ans=min(ans,self.solve(tp[i],tp[i-1]))
        return ans