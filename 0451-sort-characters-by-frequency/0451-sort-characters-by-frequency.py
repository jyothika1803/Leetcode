class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap={}
        for ch in s:
            if ch in hashmap:
                hashmap[ch]+=1
            else:
                hashmap[ch]=1
        max_heap=[]
        for ch,freq in hashmap.items():
            pair=(-freq,ch)
            max_heap.append(pair)
        heapq.heapify(max_heap)
        result=[]
        while max_heap:
            freq,ch=heapq.heappop(max_heap)
            result.extend([ch]*-freq)
        return "".join(result)

        