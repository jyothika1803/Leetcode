class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greater={}
        for num in nums2:
            while len(stack)!=0 and num>stack[-1]:
                prev=stack.pop()
                next_greater[prev]=num
            stack.append(num)
        for num in stack:
            next_greater[num]=-1
        result=[]
        for num in nums1:
            result.append(next_greater[num])
        return result