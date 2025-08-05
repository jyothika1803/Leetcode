class Solution:
    def totalMoney(self, n: int) -> int:
        money=0
        start=0
        remainder=n%7
        while start <n//7:
            end=7+start
            money+=(end*(end+1)//2)-(start*(start+1)//2)
            start+=1
        return money+((remainder+start)*(remainder+start+1)//2)-(start*(start+1)//2)

        