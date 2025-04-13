class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum=0
        startValue=0
        for num in nums:
            prefix_sum+=num
            startValue=min(startValue,prefix_sum)
        return -(startValue)+1
        