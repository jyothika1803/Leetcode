class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n=len(plantTime)
        seeds=[]
        for i in range(n):
            seeds.append([plantTime[i],growTime[i]])
        seeds.sort(key=lambda x:-x[1])
        current_day=0
        max_bloom=0
        for plant,grow in seeds:
            current_day+=plant
            max_bloom=max(max_bloom,current_day+grow)
        return max_bloom
        