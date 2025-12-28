class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        total=sum(nums)
        maximum=float('-inf')
        minimum=float('inf')
        for i in range(len(nums)-1,0,-1):
            total-=nums[i]
            minimum=min(minimum,nums[i])
            maximum=max(maximum,total-minimum)
        return maximum
        