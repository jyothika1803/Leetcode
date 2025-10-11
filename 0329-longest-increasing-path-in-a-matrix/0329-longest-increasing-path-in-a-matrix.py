class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows,cols=len(matrix),len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]
        def dfs(i:int,j:int)->int:
            if dp[i][j]!=0:
                return dp[i][j]
            max_len=1
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dx,dy in directions:
                x,y=i+dx,j+dy
                if 0<=x<rows and 0<=y<cols and matrix[x][y]>matrix[i][j]:
                    max_len=max(max_len,1+dfs(x,y))
            dp[i][j]=max_len
            return max_len
        max_path=0
        for i in range(rows):
            for j in range(cols):
                max_path=max(max_path,dfs(i,j))
        return max_path
     