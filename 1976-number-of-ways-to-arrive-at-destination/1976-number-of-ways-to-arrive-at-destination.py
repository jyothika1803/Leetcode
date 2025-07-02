class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9+7
        graph=[[] for _ in range(n)]
        for u,v,time in roads:
            graph[u].append((v,time))
            graph[v].append((u,time))
        dist=[float('inf')]*n
        ways=[0]*n
        dist[0]=0
        ways[0]=1
        min_heap=[(0,0)]  
        while min_heap:
            time_u,u=heapq.heappop(min_heap)
            if time_u>dist[u]:
                continue
            for v,edge_time in graph[u]:
                new_dist=time_u+edge_time
                if new_dist<dist[v]:
                    dist[v]=new_dist
                    ways[v]=ways[u]
                    heapq.heappush(min_heap,(new_dist, v))
                elif new_dist==dist[v]:
                    ways[v]=(ways[v]+ways[u])%MOD
        return ways[n-1]
   


