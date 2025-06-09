class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashmap={}
        for char in allowed:
            hashmap[char]=True
        count=0
        for word in words:
            flag=True
            for char in word:
                if char not in hashmap:
                    flag=False
                    break
            if flag:
                count+=1
        return count
        