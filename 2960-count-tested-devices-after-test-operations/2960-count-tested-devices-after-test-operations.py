class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count=0
        decrement=0
        for battery in batteryPercentages:
            curr=battery-decrement
            if curr>0:
                count+=1
                decrement+=1
        return count