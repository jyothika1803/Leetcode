class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        minheap=[]
        i=0
        while i<len(nums):
            heapq.heappush(minheap,(nums[i],i))
            if len(minheap)>k:
                heapq.heappop(minheap)
            i+=1
        minheap.sort(key=lambda x:x[1])
        result=[]
        for value,_ in minheap:
            result.append(value)
        return result
        
    
