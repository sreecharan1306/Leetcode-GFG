class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        dp=[[0]*n for _ in range(m)]
        for c in range(n-2,-1,-1):
            for r in range(m):
                if r-1>=0 and grid[r-1][c+1]>grid[r][c]:
                    dp[r][c]=max(dp[r][c],dp[r-1][c+1]+1)
                if grid[r][c+1]>grid[r][c]:
                    dp[r][c]=max(dp[r][c],1+dp[r][c+1])
                if r+1<m and grid[r+1][c+1]>grid[r][c]:
                    dp[r][c]=max(dp[r+1][c+1]+1,dp[r][c])
                if c==0:
                    ans=max(ans,dp[r][c])
        
        # print(dp)  
        return ans