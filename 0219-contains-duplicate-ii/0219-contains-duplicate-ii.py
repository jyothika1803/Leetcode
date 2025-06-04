class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result=set()
        for i in range(len(nums)):
            if nums[i] in result:
                return True
            result.add(nums[i])
            if len(result)>k:
                result.remove(nums[i-k])
        return False