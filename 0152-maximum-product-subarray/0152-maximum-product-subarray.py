class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_product=1
        right_product=1
        result=float('-inf')
        n=len(nums)
        for i in range(0,len(nums)):
            if left_product==0:
                left_product=1
            if right_product==0:
                right_product=1
            left_product*=nums[i]
            right_product*=nums[n-1-i]
            result=max(result,max(left_product,right_product))
        return result
        