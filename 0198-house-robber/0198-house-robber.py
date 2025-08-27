class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        a=0
        b=nums[0]
        c=0
        for i in range(1,len(nums)):
            c=max(a+nums[i],b)
            a=b
            b=c
        return b

        