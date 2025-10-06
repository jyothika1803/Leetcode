class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        mp = {0: -1}
        sum = 0
        maxLength = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            if sum in mp:
                maxLength = max(maxLength, i - mp[sum])
            else:
                mp[sum] = i
        
        return maxLength
       