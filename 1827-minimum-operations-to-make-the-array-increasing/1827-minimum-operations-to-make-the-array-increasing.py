class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        prev=0
        for cur in nums:
            if cur<=prev:
                prev+=1
                count+=prev-cur
            else:
                prev=cur
        return count