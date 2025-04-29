class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        maxLength=0
        maxString=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                substring=s[i:j+1]
                if j-i+1>maxLength and substring==substring[::-1]:
                    maxLength=j-i+1
                    maxString=substring
        return maxString
        