class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sum_target=sum(target)
        delete=0
        maxheap=[]
        for t in target:
            heapq.heappush(maxheap,-t)
        while True:
            delete=-heapq.heappop(maxheap)
            sum_target-=delete
            if delete==1 or sum_target==1:
                return True
            elif sum_target==0 or sum_target>=delete or delete%sum_target==0:
                return False
            delete %= sum_target
            sum_target+=delete
            heapq.heappush(maxheap,-delete)
 

        