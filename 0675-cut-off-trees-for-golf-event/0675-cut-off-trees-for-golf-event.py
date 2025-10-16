class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]: return -1
        rows, cols = len(forest), len(forest[0])
        trees = []
        for r in range(rows):
            for c in range(cols):
                if forest[r][c] > 1: heappush(trees, (forest[r][c], r, c))
        
        def bfs(sr, sc, tr, tc):
            visited = [[False]*cols for _ in range(rows)]
            q = deque([(sr, sc, 0)])
            visited[sr][sc] = True
            while q:
                r, c, steps = q.popleft()
                if r == tr and c == tc: return steps
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc] and forest[nr][nc]!=0:
                        visited[nr][nc] = True
                        q.append((nr, nc, steps+1))
            return -1
        
        total, cr, cc = 0, 0, 0
        while trees:
            _, tr, tc = heappop(trees)
            steps = bfs(cr, cc, tr, tc)
            if steps == -1: return -1
            total += steps
            cr, cc = tr, tc
        return total