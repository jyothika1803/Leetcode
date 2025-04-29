class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        max_freq=max(freq.values())
        result=0
        for val in freq.values():
            if val==max_freq:
                result+=val
        return result