class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[-1]*(len(nums)+1)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,len(nums)+1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[len(nums)]

        