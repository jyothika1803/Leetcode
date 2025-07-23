class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        max_heap=[]
        for num, freq in hashmap.items():
            pair=(-freq,num)
            max_heap.append(pair)
            heapq.heapify(max_heap)
        result=[]
        for _ in range(k):
            freq,num=heapq.heappop(max_heap)
            result.append(num)
        return result
        
        