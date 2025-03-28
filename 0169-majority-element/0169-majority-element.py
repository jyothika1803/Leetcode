class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=-1
        c=0
        for num in nums:
            if c==0:
                m=num
            if num==m:
                c+=1
            else:
                c-=1
        return m
        