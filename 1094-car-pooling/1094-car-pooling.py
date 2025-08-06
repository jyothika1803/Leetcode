class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x:x[1])
        current_passengers=0
        min_heap=[]
        for num,start,end in trips:
            while min_heap and min_heap[0][0]<=start:
                drop,leaving=heapq.heappop(min_heap)
                current_passengers-=leaving
            current_passengers+=num
            if current_passengers>capacity:
                return False
            heapq.heappush(min_heap,(end,num))
        return True