class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        Sum=0
        diff=float('inf')
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j<k:
                Sum=nums[i]+nums[j]+nums[k]
                curr_diff=target-Sum

                if abs(curr_diff) < abs(diff):
                    diff = curr_diff
                if Sum<target:
                    j+=1
                elif Sum>target:
                    k-=1
                else:
                    return target

        return target - diff



