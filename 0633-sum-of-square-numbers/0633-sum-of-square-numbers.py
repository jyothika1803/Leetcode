class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b=0
        while (b+1)*(b+1)<=c:
            b+=1
        a=0
        while a<=b:
            sum_of_squares=a*a+b*b
            if sum_of_squares==c:
                return True
            elif sum_of_squares<c:
                a+=1
            else:
                b-=1
        return False
        