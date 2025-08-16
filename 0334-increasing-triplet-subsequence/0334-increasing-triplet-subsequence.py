class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a=float('inf')
        b=float('inf')
        for i in range(len(nums)):
            if nums[i]<=a:    # --> = to handle duplicates
                a=nums[i]
            elif nums[i]<=b:
                b=nums[i]
            else:
                return True
        return False