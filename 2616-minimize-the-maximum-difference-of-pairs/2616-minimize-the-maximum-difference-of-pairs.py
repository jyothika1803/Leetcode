class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        minimum=0
        maximum=nums[-1]-nums[0]
        while minimum<maximum:
            mid=(minimum+maximum)//2
            pairs=0
            i=1
            while i<len(nums):
                if nums[i]-nums[i-1]<=mid:
                    pairs+=1
                    i+=1
                i+=1
            if pairs>=p:
                maximum=mid
            else:
                minimum=mid+1
        return minimum