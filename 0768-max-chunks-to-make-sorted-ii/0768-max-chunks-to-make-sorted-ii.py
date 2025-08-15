class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        suffix_min=[0]*len(arr)
        suffix_min[-1]=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            suffix_min[i]=min(suffix_min[i+1],arr[i])
        Max=float('-inf')
        chunks=0
        for i in range(len(arr)-1):
            Max=max(Max,arr[i])
            if Max<=suffix_min[i+1]:
                chunks+=1
        chunks+=1
        return chunks

        