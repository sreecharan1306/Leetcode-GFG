class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        def bs(i,p):
            l=0
            h=len(p)
            while l<=h:
                m=(l+h)//2
                if p[m]==i:
                    h=m-1
                elif p[m]>i:
                    h=m-1
                else:
                    l=m+1
            return l
            
        p=sorted(list(set(arr)))#arr)
        x=0
        for i in arr:
            arr[x]=bs(i,p)+1
            x+=1
        return arr