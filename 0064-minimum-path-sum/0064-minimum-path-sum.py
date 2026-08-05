class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,column=len(grid),len(grid[0])
        dp=[[0 for _ in range(column)] for _ in range(row)]
        dp[0][0]=grid[0][0]
        for pos_i in range(row):
            for pos_j in range(column):
                if pos_i==0 and pos_j==0:
                    pass
                elif pos_i==0:
                    dp[pos_i][pos_j]=grid[pos_i][pos_j]+dp[pos_i][pos_j-1]
                elif pos_j==0:        
                    dp[pos_i][pos_j]=grid[pos_i][pos_j]+dp[pos_i-1][pos_j]
                else:
                    min_val=min(dp[pos_i-1][pos_j],dp[pos_i][pos_j-1])
                    dp[pos_i][pos_j]=grid[pos_i][pos_j]+min_val
        return dp[row-1][column-1]            