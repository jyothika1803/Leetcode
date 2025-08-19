class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]
        """
        #recursion
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        """
        
        """
        #iterative
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        a=0
        b=1
        c=1
        for _ in range(3,n+1):
            a,b,c=b,c,a+b+c
        return c
        """