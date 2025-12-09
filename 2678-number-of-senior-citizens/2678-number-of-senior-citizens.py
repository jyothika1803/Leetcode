class Solution:
    def countSeniors(self, details: List[str]) -> int:
        maxCount=0
        for d in details:
            age=int(d[11:13])
            if age>60:
                maxCount+=1
        return maxCount
