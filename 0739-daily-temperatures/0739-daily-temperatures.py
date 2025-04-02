class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        arr=[0]*n
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                index=stack.pop()
                arr[index]=i-index  # Calculate the number of days until a warmer temperature
            stack.append(i)
        return arr


        