class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_val=float('inf')
        max_val=float('-inf')
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                min_val=min(min_val,nums[i])
        for j in range(len(nums)-2,-1,-1):
            if nums[j]>nums[j+1]:
                max_val=max(max_val,nums[j])
        if min_val==float('inf') and max_val==float(-inf):
            return 0
        i=0
        while i<len(nums) and nums[i]<=min_val:
            i+=1

        j=len(nums)-1
        while j>=0 and nums[j]>=max_val:
            j-=1
        return j-i+1


        