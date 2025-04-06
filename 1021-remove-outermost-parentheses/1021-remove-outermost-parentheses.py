class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        stack=[]
        for bracket in s:
            if bracket=="(":
                if count>0:
                    stack.append(bracket)
                count+=1
            elif bracket==")":
                count-=1
                if count>0:
                    stack.append(bracket)
        return "".join(stack)

        