class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        new_arr=[-1]*n
        for i in range(2*n):
            num=nums[i%len(nums)]
            while stack and nums[stack[-1]]<nums[i%n]:
                index=stack.pop()
                new_arr[index]=nums[i%n]
            if i<n:
                stack.append(i)
        return new_arr
 