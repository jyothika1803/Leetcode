class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq=Counter(barcodes)
        heap=[(-count,val) for val,count in freq.items()]
        heapq.heapify(heap)
        result=[]
        prev_count,prev_val=0,None
        while heap:
            count,val=heapq.heappop(heap)
            result.append(val)
            if prev_count<0:
                heapq.heappush(heap,(prev_count,prev_val))
            prev_count=count+1
            prev_val=val
        return result
