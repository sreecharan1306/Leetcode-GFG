class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(s1,s2):
            if int(s1+s2)<int(s2+s1):
                return -1
            if int(s1+s2)>int(s2+s1):
                return 1
            return 0
        nums=[str(i) for i in nums]
        nums.sort(key=cmp_to_key(cmp),reverse=True)
        # print(nums)
        ans=''.join(nums)
        return "0" if ans[0]=='0' else ans