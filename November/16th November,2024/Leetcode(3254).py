class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def cons(arr):
            for i in range(1,len(arr)):
                if arr[i]-arr[i-1]!=1:
                    return False
            return True
        n=len(nums)
        if k==1:
            return nums
        ans=[0]*(n-k+1)
        prev=True
        i=0
        if not cons(nums[i:k]):
            ans[0]=-1
            prev=False
        else:
            prev=True
            ans[0]=nums[k-1]

        j=k
        print(i,j)
        for i in range(1,n-k+1):
            if prev:
                if nums[j]-nums[j-1]==1:
                    ans[i]=nums[j]
                    j+=1
                    continue
                else:
                    ans[i]=-1
                    prev=False
                    j+=1
                    continue
            else:
                if cons(nums[i:j+1]):
                    # print(nums[i:j+1])
                    prev=True
                    ans[i]=nums[j]
                    j+=1
                    continue
                else:
                    ans[i]=-1
                    j+=1

        return ans