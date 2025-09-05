class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[]
        for _ in range(n+1):    
            row=[-1]*(amount+1)   
            dp.append(row)
        def helper(amount,index):
            if amount==0:
                return 1
            if amount<0 or index>=n:
                return 0
            if dp[index][amount]!=-1:
                return dp[index][amount]

            take=helper(amount-coins[index],index)
            skip=helper(amount,index+1)
            dp[index][amount]=take+skip
            return dp[index][amount]
        return helper(amount,0)
        