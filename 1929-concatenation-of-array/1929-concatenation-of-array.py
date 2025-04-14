class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(0, 2 * n):
            ans.append(nums[i % n])
        return ans