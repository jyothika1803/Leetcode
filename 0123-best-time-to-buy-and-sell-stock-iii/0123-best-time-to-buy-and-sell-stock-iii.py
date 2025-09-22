class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minIni=prices[0]
        dp1=[0]*len(prices)
        for i in range(len(prices)):
            minIni=min(minIni,prices[i])
            if i>0:
                dp1[i]=max(dp1[i-1],prices[i]-minIni)
            else:
                dp1[i]=0
        dp2=[0]*len(prices)
        maxIni=prices[-1]
        for j in range(len(prices)-1,-1,-1):
            maxIni=max(maxIni,prices[j])
            if j<len(prices)-1:
                dp2[j]=max(dp2[j+1],maxIni-prices[j])
            else:
                dp2[j]=0
        Max=0
        for i in range(len(prices)):
            Max=max(Max,dp1[i]+dp2[i])
        return Max


        