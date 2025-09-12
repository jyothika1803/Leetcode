class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*26
        mL=0
        for i in range(len(s)):
            val=ord(s[i])-ord('a')
            left=max(0,val-k)
            right=min(25,val+k)
            dp[val]=max(dp[left:right+1])+1
            mL=max(mL,dp[val])
        return max(dp)

            
