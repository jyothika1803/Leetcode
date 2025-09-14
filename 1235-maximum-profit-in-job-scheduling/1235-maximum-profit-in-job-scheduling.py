class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        time=[]
        for i in range(len(startTime)):
            time.append([startTime[i],endTime[i],profit[i]])
        time.sort(key=lambda x:x[1])
        n=len(profit)
        end=[0]*(n+1)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            start=time[i-1][0]
            ends=time[i-1][1]
            prof=time[i-1][2]
            end[i]=ends
            index=self.binarySearch(end,0,i,start)
            dp[i]=max(dp[i-1],dp[index]+prof)
        return dp[n]

    def binarySearch(self,arr,minimum,maximum,target):
        while minimum<=maximum:
            mid=(minimum+maximum)//2
            if arr[mid]<=target:
                minimum=mid+1
            else:
                maximum=mid-1
        return maximum
    
    

