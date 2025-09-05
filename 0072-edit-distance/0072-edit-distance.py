class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[]
        for i in range(m+1):
            row=[0]*(n+1)
            dp.append(row)

        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[m][n]