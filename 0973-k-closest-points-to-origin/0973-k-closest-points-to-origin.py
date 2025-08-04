class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap=[]
        for x,y in points:
            distance=x*x+y*y
            heapq.heappush(maxheap,(-distance,[x,y]))
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        result=[]
        for distance,point in maxheap:
            result.append(point)
        return result
