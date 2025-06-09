class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=[]
        for i in range(len(names)):
            people.append((names[i],heights[i]))
        people.sort(key=lambda x:x[1],reverse=True)
        result=[]
        for name,height in people:
            result.append(name)
        return result