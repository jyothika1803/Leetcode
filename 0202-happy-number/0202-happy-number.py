class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        elif n<=6:
            return False
        square=0
        while n!=0:
            remainder=n%10
            square+=remainder*remainder
            n//=10
        return self.isHappy(square)

        