class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        minimum=1
        maximum=x
        while minimum<=maximum:
            mid=(minimum+maximum)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                maximum=mid-1
            else:
                minimum=mid+1
        return maximum

        