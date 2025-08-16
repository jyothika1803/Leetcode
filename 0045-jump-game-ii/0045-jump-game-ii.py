class Solution:
    def jump(self, nums: List[int]) -> int:
        maxIndex=0
        Max=0
        minJumps=0
        for i in range(0,len(nums)-1):
            Max=max(Max,i+nums[i])
            if maxIndex==i:
                minJumps+=1
                maxIndex=Max
            if maxIndex>=len(nums)-1:
                return minJumps
        return minJumps # <-- handles cases like nums=[0] should return 0 as no jumps possible

        