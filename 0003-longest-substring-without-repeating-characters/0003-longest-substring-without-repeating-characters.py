class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        maxLength=0
        arr=[0]*128
        for end in range(len(s)):
            char=s[end]
            start=max(start,arr[ord(char)])
            maxLength=max(maxLength,end-start+1)
            arr[ord(char)]=end+1
        return maxLength