class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m1,m2=pow(10,5),-1000000
        s=0
        for i in range(len(arrays)):
            m2=max(m2,max(arrays[i]))
            if m2==max(arrays[i]):
                s=i

        for i in range(len(arrays)):
            if i==s:
                continue
            m1=min(m1,min(arrays[i]))
        
        m3,m4=pow(10,5),-1000000
        t=0
        for i in range(len(arrays)):
            m3=min(m3,min(arrays[i]))
            if m3==min(arrays[i]):
                t=i

        for i in range(len(arrays)):
            if i==t:
                continue
            m4=max(m4,max(arrays[i]))
        return max(m2-m1,m4-m3)