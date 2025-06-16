class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap={}
        index=0
        for char in order:
            hashmap[char]=index
            index+=1
        sorted_s=sorted(s,key=lambda x:hashmap.get(x,float('inf')))
        return "".join(sorted_s)
