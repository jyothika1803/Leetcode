class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp=[0]*(query_row+1)
        dp[0]=poured
        for row in range(query_row+1):
            for col in range(row-1,-1,-1):
                if dp[col]>1:
                    val=(dp[col]-1)/2
                    dp[col]=val
                    dp[col+1]+=val
                else:
                    dp[col]=0
        return min(1,dp[query_glass])
                
