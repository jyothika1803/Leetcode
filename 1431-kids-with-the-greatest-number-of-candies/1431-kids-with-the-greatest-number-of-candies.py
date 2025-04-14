class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        maxCandies=max(candies)
        for i in range(len(candies)):
            res.append(candies[i]+extraCandies>=maxCandies)
        return res


        