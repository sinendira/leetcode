class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        g=[[0]*len(obstacleGrid[0]) for j in range(len(obstacleGrid))]
        for i in range(len(g[0])):
            if obstacleGrid[0][i]==1:
                break
            g[0][i]=1
        for i in range(len(g)):
            if obstacleGrid[i][0]==1:
                break
            g[i][0]=1

        for i in range(1,len(g)):
            for j in range(1,len(g[0])):
                if obstacleGrid[i][j]==1:
                    continue

                g[i][j]=g[i][j-1]+g[i-1][j]

        return g[-1][-1]