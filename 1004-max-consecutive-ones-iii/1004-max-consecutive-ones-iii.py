class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end=0
        max_length=0
        zero_count=0
        while end<len(nums):
            if nums[end]==0:
                zero_count+=1
            while zero_count>k:
                if nums[start]==0:
                    zero_count-=1
                start+=1
            max_length=max(max_length,end-start+1)
            end+=1
        return max_length