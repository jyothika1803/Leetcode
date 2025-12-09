class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ans=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                localValues=[]
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        localValues.append(grid[x][y])
                localMax=max(localValues)
                ans[i][j]=localMax
        return ans