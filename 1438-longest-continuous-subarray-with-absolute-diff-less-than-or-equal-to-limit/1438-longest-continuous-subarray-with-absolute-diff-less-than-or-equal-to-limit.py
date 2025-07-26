class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxheap=[]
        minheap=[]
        hashmap={}
        left=0
        ans=0
        for right in range(len(nums)):
            num=nums[right]
            hashmap[num]=hashmap.get(num,0)+1
            heapq.heappush(maxheap,-num)
            heapq.heappush(minheap,num)
            while abs(-maxheap[0]-minheap[0])>limit:
                hashmap[nums[left]]-=1
                while maxheap and hashmap[-maxheap[0]]==0:
                    heapq.heappop(maxheap)
                while minheap and hashmap[minheap[0]]==0:
                    heapq.heappop(minheap)
                left+=1
            ans=max(ans,right-left+1)
        return ans