class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=[-1,0,1,0]
        c=[0,1,0,-1]
        m=len(grid)
        n=len(grid[0])
        visited=[]
        for _ in range(m):
            row=[False]*n
            visited.append(row)
        row=0
        col=0
        count=0
        def bfs(row,col):
            queue=deque()
            queue.append((row,col))
            visited[row][col]=True

            while queue:
                curr_row,curr_col=queue.popleft()
                for i in range(4):
                    nrow=curr_row+r[i]
                    ncol=curr_col+c[i]
                    if (0<=nrow<m and 0<=ncol<n and not visited[nrow][ncol] and grid[nrow][ncol] == '1'):
                        visited[nrow][ncol]=True
                        queue.append((nrow,ncol))

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    bfs(i,j)
                    count+=1

        return count

        