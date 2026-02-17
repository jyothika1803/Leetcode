class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr=[0]*26
        for char in s:
            arr[ord(char)-ord('a')]+=1
        i=0
        while i<len(s):
            ch=s[i]
            if arr[ord(ch)-ord('a')]==1:
                return i
            i+=1
        return -1
        