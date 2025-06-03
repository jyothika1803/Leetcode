class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        minimum=0
        maximum=len(nums)-1
        while minimum<maximum:
            mid=(maximum+minimum)//2
            if nums[mid]>nums[mid+1]:
                maximum=mid
            else:
                minimum=mid+1
        return minimum
