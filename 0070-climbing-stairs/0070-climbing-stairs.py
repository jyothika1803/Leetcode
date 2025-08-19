class Solution:
    def climbStairs(self, n: int) -> int:
        #dp
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
        
        """
        #recursion
        if n<=2:
            return n
        return self.climbStairs(n-2)+self.climbStairs(n-1)
        """
        """
        #iterative
        if n<=1:
            return 1
        a=1
        b=1
        for _ in range(2,n+1):
            a,b=b,a+b
        return b

        """