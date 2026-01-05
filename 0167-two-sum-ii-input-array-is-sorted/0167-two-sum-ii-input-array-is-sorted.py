class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remaining=0
        hashmap={}
        for i in range(len(numbers)):
            remaining=target-numbers[i]
            if remaining in hashmap:
                return [hashmap[remaining]+1,i+1]
            hashmap[numbers[i]]=i