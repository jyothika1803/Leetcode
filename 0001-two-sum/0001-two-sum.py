class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}  # Dictionary to store the index of elements
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mp:  # Check if the complement exists in the dictionary
                return [mp[complement], i]  # Return the indices of the two numbers
            mp[nums[i]] = i  # Store the index of the current number in the dictionary
        return []  # Return an empty list if no solution is found
        