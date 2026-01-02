class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones=0
        max_ones=float('-inf')
        for i in range(len(nums)):
            if nums[i]==1:
                ones+=1
            else:
                max_ones=max(ones,max_ones)
                ones=0
        return max(ones,max_ones)

        