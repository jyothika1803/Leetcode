class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mp = {}
        cnt = 0
        
        for a in nums1:
            for b in nums2:
                sum = a + b
                mp[sum] = mp.get(sum, 0) + 1
        
        for c in nums3:
            for d in nums4:
                sum = c + d
                cnt += mp.get(-sum, 0)
        
        return cnt
       
        