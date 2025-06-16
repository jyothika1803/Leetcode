class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for char in strs:
            sorted_char="".join(sorted(char))
            if sorted_char not in hashmap:
                hashmap[sorted_char]=[char]
            else:
                hashmap[sorted_char].append(char)
        return list(hashmap.values())

        