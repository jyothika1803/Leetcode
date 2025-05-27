class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        minimum=0
        maximum=len(nums)
        while minimum<=maximum:
            mid=(minimum+maximum)//2
            count=0
            for num in nums:
                if num>=mid:
                    count+=1
            if count==mid:
                return mid
            elif count>=mid:
                minimum=mid+1
            else:
                maximum=mid-1
        return -1

        