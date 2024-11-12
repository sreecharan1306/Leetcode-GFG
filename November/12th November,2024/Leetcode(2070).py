class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def bs(arr,key):
            l,h=0,len(arr)-1
            while l<=h:
                m=(l+h)//2
                if arr[m]>key:
                    h=m-1
                else:
                    l=m+1
            return arr[l-1]

        ans=[]
        p=defaultdict(int)
        
        for i in items:
            if p[i[0]]:
                p[i[0]]=max(p[i[0]],i[1])
            else:
                p[i[0]]=i[1]
        q=list(p.keys())
        q.sort()
        for i in range(1,len(q)):
            if p[q[i]]<p[q[i-1]]:
                p[q[i]]=p[q[i-1]]
        for i in queries:
            if i>=q[-1]:
                ans.append(p[q[-1]])
                continue
            if i<q[0]:
                ans.append(0)
                continue
            x=bs(q,i)
            ans.append(p[x])

        return ans