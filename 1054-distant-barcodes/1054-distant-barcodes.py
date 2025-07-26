class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        hashmap={}
        for barcode in barcodes:
            hashmap[barcode]=hashmap.get(barcode,0)+1
        maxheap=[]
        for barcode,count in hashmap.items():
            maxheap.append((-count,barcode))
        heapq.heapify(maxheap)
        res=[0]*len(barcodes)
        i=0
        while maxheap:
            count,barcode=heapq.heappop(maxheap)
            count=-count
            for _ in range(count):
                if i>=len(barcodes):
                    i=1
                res[i]=barcode
                i+=2
        return res