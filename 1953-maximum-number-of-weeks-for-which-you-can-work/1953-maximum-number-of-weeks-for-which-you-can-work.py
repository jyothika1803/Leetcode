class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        Max=max(milestones)
        Sum=sum(milestones)-Max
        if Max>Sum:
            return Sum*2+1
        else:
            return Max+Sum
        