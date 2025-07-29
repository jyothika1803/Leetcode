class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        minheap=[]
        max_perf=0
        speed_sum=0
        sort_eff=[]
        for i in range(len(speed)):
            sort_eff.append((speed[i],efficiency[i]))
        sort_eff.sort(key=lambda x:x[1],reverse=True)
        for spd,eff in sort_eff:
            heapq.heappush(minheap,spd)
            speed_sum+=spd
            if len(minheap)>k:
                speed_sum-=heapq.heappop(minheap)
            max_perf=max(max_perf,speed_sum*eff)
        return max_perf % (10**9+7)
