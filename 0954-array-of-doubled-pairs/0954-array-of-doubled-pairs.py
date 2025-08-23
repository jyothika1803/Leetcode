class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dp={}
        for num in arr:
            dp[num]=dp.get(num,0)+1
        arr.sort(key=abs)
        for x in arr:
            if dp.get(x,0)==0:
                continue
            if dp.get(2*x,0)==0:
                return False
            dp[x]-=1
            dp[2*x]-=1
        return True