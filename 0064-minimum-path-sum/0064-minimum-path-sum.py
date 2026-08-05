class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for i in range(m)]

        def fun_dp(i,j):
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(i==0 and j==0):
                return grid[0][0]
            if(i<0 or j<0):
                return float('inf')
            up=grid[i][j]+fun_dp(i-1,j)
            left=grid[i][j]+fun_dp(i,j-1)
            dp[i][j]= min(up,left)
            return dp[i][j]
        
        return fun_dp(m-1,n-1)
                