class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        n=len(coins)
        dp=[]
        for _ in range(n+1):    
            row=[-1]*(amount+1)   
            dp.append(row)
        def helper(amount,index):
            if amount==0:
                return 0
            if amount<0 or index>=n:
                return float("inf")
            if dp[index][amount]!=-1:
                return dp[index][amount]

            take=1+helper(amount-coins[index],index)
            skip=helper(amount,index+1)
            dp[index][amount]=min(take,skip)
            return dp[index][amount]
        answer=helper(amount,0)
        if answer==float("inf"):
            return -1
        else:
            return answer
        