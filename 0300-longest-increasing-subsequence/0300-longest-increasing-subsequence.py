class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[float('inf')]*(n+1)
        dp[0]=float('-inf')
        maxLength=0
        for i in range(n):
            minimum=0
            maximum=maxLength
            index=0
            while minimum<=maximum:
                mid=(minimum+maximum)//2
                if dp[mid]<nums[i]:
                    index=mid
                    minimum=mid+1
                else:
                    maximum=mid-1
            if nums[i]<dp[index+1]:
                dp[index+1]=nums[i]
            if index+1>maxLength:
                maxLength=index+1
        return maxLength