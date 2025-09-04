class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD=10**9+7
        dp=[]
        for _ in range(n+1):    
            row=[-1]*(target+1)   
            dp.append(row)
        def helper(n,target):
            if n==0 and target >0:
                return 0
            if n==0 and target==0:
                return 1
            if target<0:
                return 0
            if dp[n][target]!=-1:
                return dp[n][target]

            ways=0
            for face in range(1,k+1):
                ways=(ways+helper(n-1,target-face))%MOD
            dp[n][target]=ways
            return ways
        return helper(n,target)

            

        