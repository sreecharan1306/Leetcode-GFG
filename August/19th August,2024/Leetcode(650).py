class Solution:
    def minSteps(self, n: int) -> int:
        ans=0
        def lgpm(n)->int:
            ans=0
            largest_factor = 1
            while n % 2 == 0:
                largest_factor = 2
                ans+=2
                n //= 2
            factor = 3
            while factor * factor <= n:
                while n % factor == 0:
                    largest_factor = factor
                    ans+=factor
                    n //= factor
                factor += 2
            if n > 2:

                largest_factor = n
                ans+=largest_factor

            return ans
        # dp=[0]*n
        # dp[0]=0
        # dp[1]=2
        # for i in range(2,n):
        #     if lgpm(i)==n:
                
            # dp[i]=min(dp[i-1]+1,)
        if n==1:
            return 0
        return lgpm(n)