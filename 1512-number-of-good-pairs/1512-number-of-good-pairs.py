class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap={}
        count=0
        for i in range(len(nums)):
            if nums[i] in hashmap:
                count+=hashmap[nums[i]]
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        return count
        