class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap={}
        for char in s:
            hashmap[char]=hashmap.get(char,0)+1
        maxheap=[]
        for char,count in hashmap.items():
            maxheap.append((-count,char))
        heapq.heapify(maxheap)
        res=[0]*len(s)   
        i=0
        while maxheap:
            count,char=heapq.heappop(maxheap)
            count=-count 
            for _ in range(count):
                if i>=len(s):
                    i=1
                res[i]=char
                i+=2
        for i in range(1,len(res)):
            if res[i]==res[i-1]:
                return ""
        return "".join(res)    