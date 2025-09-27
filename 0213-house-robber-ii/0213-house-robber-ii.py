class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp1= [-1]*(n+1)
        dp1[0]=0
        dp1[1]=nums[0]
        for i in range(2,n+1):
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i-1])
        dp2=[-1]*(2*n+1)
        dp2[0]=0
        dp2[1]=nums[0]
        for i in range(2,2*n+1):
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums[(i-1)%n])
        return dp2[2*n]-dp1[n]    