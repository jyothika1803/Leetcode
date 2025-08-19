class Solution:
    def maxDiff(self, num: int) -> int:
        s=str(num)
        for digit in s:
            if digit != '9':
                a=int(s.replace(digit,'9'))
                break
        else:
            a=num
        first=s[0]
        if first !='1':
            b=int(s.replace(first,'1'))
        else:
            for digit in s[1:]:
                if digit != '0' and digit != '1':
                    b=int(s.replace(digit,'0'))
                    break
            else:
                b=num
        return abs(a-b)

                
        
        