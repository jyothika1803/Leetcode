class Solution:
    def arrangeCoins(self, n: int) -> int:
        minimum=1
        maximum=n
        while minimum<=maximum:
            mid=(maximum+minimum)//2
            total=(mid*(mid+1))//2
            if total==n:
                return mid
            elif total>n:
                maximum=mid-1
            else:
                minimum=mid+1
        return maximum
        