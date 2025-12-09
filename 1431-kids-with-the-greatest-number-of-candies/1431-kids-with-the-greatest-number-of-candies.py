class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=max(candies)
        ans=[]
        for i in range(len(candies)):
            ans.append(candies[i]+extraCandies>=maxCandies)
        return ans