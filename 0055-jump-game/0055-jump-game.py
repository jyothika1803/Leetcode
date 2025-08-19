class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex=0
        Max=0
        minJumps=0
        if len(nums)==1:
            return True
        for i in range(0,len(nums)-1):
            Max=max(Max,i+nums[i])
            if maxIndex==i:
                minJumps+=1
                maxIndex=Max
            if maxIndex>=len(nums)-1:
                return True
        return False