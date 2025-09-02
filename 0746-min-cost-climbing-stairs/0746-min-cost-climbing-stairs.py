class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        def helper(i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i]=cost[i]+min(helper(i+1),helper(i+2))
            return dp[i]
        return min(helper(0),helper(1))
        