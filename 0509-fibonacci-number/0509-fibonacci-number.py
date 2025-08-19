class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        a=0
        b=1
        for _ in range(2,n+1):
            a,b=b,a+b #simultaneous update
        return b
        