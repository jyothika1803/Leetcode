class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashmap={}
        n=len(nums)//2
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
            if hashmap[num]==n:
                return num