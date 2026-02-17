class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for char in s:
            if char not in hashmap:
                hashmap[char]=1
            else:
                hashmap[char]+=1
        i=0
        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i
        return -1

        