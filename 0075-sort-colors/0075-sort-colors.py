class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a0=0
        a1=0
        a2=0
        for i in range(len(nums)):
            if nums[i]==0:
                a0+=1
            elif nums[i]==1:
                a1+=1
            else:
                a2+=1
        nums.clear()
        for i in range(a0):
            nums.append(0)
        for i in range(a1):
            nums.append(1)
        for i in range(a2):
            nums.append(2)
        