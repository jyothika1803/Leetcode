class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n] 
        
        """
        #recursion
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
        """

        """
        #iterative
        if n<=1:
            return n
        a=0
        b=1
        for _ in range(2,n+1):
            a,b=b,a+b #simultaneous update
        return b
        """