class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[0][0]==0:
            for i in range(m):
                if obstacleGrid[i][0]==1:
                    obstacleGrid[i][0]=0
                else:
                    if i==0:
                        obstacleGrid[i][0]=1
                    else:
                        obstacleGrid[i][0]=obstacleGrid[i-1][0]
            for j in range(1,n):
                if obstacleGrid[0][j]==1:
                    obstacleGrid[0][j]=0
                else:
                    obstacleGrid[0][j]=obstacleGrid[0][j-1]
            for i in range(1,m):
                for j in range(1,n):
                    if obstacleGrid[i][j]==1:
                        obstacleGrid[i][j]=0
                    else:
                        obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
                    
            