class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        dp=[-1]*(n+1)
        def helper(index):
            if index>=len(days):
                return 0
            if dp[index]!=-1:
                return dp[index]
            one_day_pass=costs[0]+helper(index+1)
            seventh_day=days[index]+7
            idx=binarySearch(days,index,seventh_day)
            seven_day_pass=costs[1]+helper(idx)

            thirty_day=days[index]+30
            idx=binarySearch(days,index,thirty_day)
            thirty_day_pass=costs[2]+helper(idx)

            dp[index]=min(one_day_pass,seven_day_pass,thirty_day_pass)
            return dp[index]
        def binarySearch(days,minimum,search):
            maximum=len(days)-1
            while minimum<=maximum:
                mid=(minimum+maximum)//2
                if days[mid]>=search:
                    maximum=mid-1
                else:
                    minimum=mid+1
            return minimum
        return helper(0)