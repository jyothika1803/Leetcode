class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        arr=[0]*(max(nums)+len(nums))
        extra=0
        ans=0
        for num in nums:  # to count the frequency of each num in the nums and storing the count in arr
            arr[num]+=1
        for i in range(len(arr)):
            if arr[i]>1:
                extra= arr[i]-1
                ans=extra+ans
                arr[i+1]=arr[i+1]+extra
        return ans
        
        