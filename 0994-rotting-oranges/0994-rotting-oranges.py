class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=[-1,0,1,0]
        c=[0,1,0,-1]
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1
        time=0
        while queue:
            row,col,t=queue.popleft()
            time=max(time,t)
            for i in range(4):
                nrow=row+r[i]
                ncol=col+c[i]
                if 0<=nrow<m and 0<=ncol<n  and grid[nrow][ncol]==1:
                    grid[nrow][ncol]=2
                    fresh-=1
                    queue.append((nrow,ncol,t+1))
        if fresh==0:
            return time
        else:
            return -1