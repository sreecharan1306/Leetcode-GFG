from collections import Counter
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        n=len(nums)
        ans=[]
        if n==0:
            return []
        cand1,cand2,cnt1,cnt2=0,0,0,0
        for i in nums:
            if i==cand1:
                cnt1+=1
            elif i==cand2:
                cnt2+=1
            elif cnt1==0:
                cand1,cnt1=i,1
            elif cnt2==0:
                cand2,cnt2=i,1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1,cnt2=0,0
        for i in nums:
            if i==cand1:
                cnt1+=1
            elif i==cand2:
                cnt2+=1
        if cnt1>n//3:
            ans.append(cand1)        
        if cnt2>n//3:
            ans.append(cand2)
        if len(ans)==0:
            return []
        return sorted(ans)
            
                





#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends