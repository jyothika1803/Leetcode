class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        max_num=max(hashmap.keys())
        dp=[0]*(max_num+1)
        for num in hashmap:
            dp[num]=num*hashmap[num]
        for i in range(2,max_num+1):
            dp[i]=max(dp[i-1],dp[i-2]+dp[i])
        return dp[max_num]