class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k==0:
            return 0
        minimum=1
        maximum=max(candies)
        best=0
        while minimum<=maximum:
            mid=(minimum+maximum)//2
            children=0
            for pile in candies:
                children+=pile//mid
            if children>=k:
                best=mid
                minimum=mid+1
            else:
                maximum=mid-1
        return best