class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        task=0
        total=0
        index=0
        for i in range(len(gas)):
            task+=gas[i]-cost[i]
            total+=gas[i]-cost[i]
            if task<0:
                index=i+1
                task=0
        if total>=0:
            return index
        else:
            return -1   