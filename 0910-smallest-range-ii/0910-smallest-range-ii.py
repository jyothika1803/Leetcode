class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=nums[-1]-nums[0]
        bestL=nums[0]+k
        bestR=nums[-1]-k
        for i in range(len(nums)-1):
            minimum=nums[i+1]-k
            maximum=nums[i]+k
            min1=min(minimum,bestL)
            max1=max(maximum,bestR)
            res=min(res,max1-min1)
        return res

        