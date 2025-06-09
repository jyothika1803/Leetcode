class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap={}
        for i in range(len(names)):
            hashmap[heights[i]]=names[i]
        sorted_heights=sorted(hashmap.keys(),reverse=True)
        sorted_names=[]
        for h in sorted_heights:
            sorted_names.append(hashmap[h])
        return sorted_names