class Solution:
    def myPow(self, x: float, n: int) -> float:
        if  n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        t=self.myPow(x,n//2)
        if n%2!=0:
            return x*t*t
        if n%2==0:
            return t*t
        