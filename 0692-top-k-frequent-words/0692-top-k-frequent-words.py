class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap={}
        for word in words:
            hashmap[word]=hashmap.get(word,0)+1
        max_heap=[]
        for word,freq in hashmap.items():
            pair=(-freq,word)
            max_heap.append(pair)
        heapq.heapify(max_heap)
        result=[]
        for _ in range(k):
            freq,word=heapq.heappop(max_heap)
            result.append(word)
        return result
            