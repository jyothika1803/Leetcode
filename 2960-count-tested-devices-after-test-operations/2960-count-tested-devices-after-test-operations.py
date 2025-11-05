class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        sub=[1]*len(batteryPercentages)
        count=0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]==0:
                continue
            else:
                count+=1
                for j in range(i+1,len(batteryPercentages)):
                    batteryPercentages[j]=max(0,batteryPercentages[j]-1)
        return count
