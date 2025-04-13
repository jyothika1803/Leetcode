class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        total_sum=0
        prefix_sum=0
        result=[]
        for i in range(n):
            total_sum+=nums[i]

        for i in range(n):
            res=(nums[i]*i)-prefix_sum+(total_sum-prefix_sum)-((n-i)*nums[i])
            result.append(res)
            prefix_sum+=nums[i]
        return result
        