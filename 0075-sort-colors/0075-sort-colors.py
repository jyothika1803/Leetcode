class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a0 = nums.count(0)
        a1 = nums.count(1)
        a2 = nums.count(2)
        nums.clear()
        for i in range(a0) :
            nums.append(0)
        for i in range(a1) :
            nums.append(1)
        for i in range(a2) :
            nums.append(2)        