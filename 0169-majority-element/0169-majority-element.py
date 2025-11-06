class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        n=len(nums)
        for num,count in hashmap.items():
            if count>n//2:
                return num
        return -1

        