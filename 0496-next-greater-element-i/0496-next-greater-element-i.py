class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        arr=[-1]*len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                index=stack.pop()
                arr[index]=nums2[i]
            stack.append(i)
        result=[]
        for num in nums1:
            index=nums2.index(num)
            result.append(arr[index])
        return result         

        