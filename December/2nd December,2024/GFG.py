#User function Template for python3

class Solution:
    def search(self, pat, txt):
        def genarr(pat):
            i,j=0,1
            n=len(pat)
            arr=[0]*n
            while j<n:
                if pat[i]==pat[j]:
                    i+=1
                    arr[j]=i
                    j+=1
                else:
                    if i!=0:
                        i=arr[i-1]
                        
                    else:
                        arr[j]=0
                        j+=1
            
            return arr
            
        # code here
        ans=[]
        p=len(pat)
        q=len(txt)
        lps=genarr(pat)
        i,j=0,0
        while i<q:
            if pat[j]==txt[i]:
                i+=1
                j+=1
            if j==p:
                ans.append(i-j)
                j=lps[j-1]
            elif i<q and txt[i]!=pat[j]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return ans



