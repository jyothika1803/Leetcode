class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minimum=0
        maximum=len(nums)-1
        while minimum<=maximum:
            mid=(minimum+maximum)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<=target:
                minimum=mid+1
            else:
                maximum=mid-1
        return -1
        