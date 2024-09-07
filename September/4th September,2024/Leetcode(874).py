class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y=0,0
        di=[[0,1],[1,0],[0,-1],[-1,0]]
        ind=0
        ans=0
        os=set(map(tuple,obstacles))
        for i in commands:
            if i==-1:
                ind+=1
                ind%=4
            elif i==-2:
                ind-=1
                ind%=4
            else:
                x1,y1=di[ind]
                while i and (x1+x,y1+y) not in os:
                    x+=x1
                    y+=y1
                    i-=1
                # x=x+(x1*i)
                # y=y+(y1*i)
            ans=max(ans,pow(x,2)+pow(y,2))
        return ans