class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        minimum=max(nums)
        maximum=sum(nums)
        result=maximum
        while minimum<=maximum:
            mid=(minimum+maximum)//2
            if self.isPossible(nums,mid,k):
                result=mid
                maximum=mid-1
            else:
                minimum=mid+1
        return result
    
    def isPossible(self,nums,max_sum,k):
        count=1
        current_sum=0
        for num in nums:
            current_sum+=num
            if current_sum>max_sum:
                count+=1
                current_sum=num
                if count>k:
                    return False
        return True